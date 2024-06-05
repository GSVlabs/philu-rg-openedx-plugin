"""
Module for platform overrides.
"""

from django.utils.translation import gettext_lazy as _

from openedx.core.djangoapps.user_api import errors
from openedx.core.djangoapps.user_api.accounts.api import (
    _get_old_language_proficiencies_if_updating,
    _get_user_and_profile,
    _notify_language_proficiencies_update_if_needed,
    _send_email_change_requests_if_needed,
    _store_old_name_if_needed,
    _update_extended_profile_if_needed,
    _update_preferences_if_needed,
    _update_state_if_needed,
    _validate_email_change,
    _validate_name_change,
    _validate_read_only_fields,
    _validate_secondary_email,
)
from openedx.core.djangoapps.user_api.accounts.serializers import (
    AccountLegacyProfileSerializer,
    AccountUserSerializer,
)
from openedx.core.lib.api.view_utils import add_serializer_errors


def get_name_validation_error(original_func, name):
    """
    Addition validation for allowed name length.
    """
    if name and len(name) > 255:
        return _("Full name can't be longer than 255 symbols")

    return original_func(name)


def update_account_settings(original_func, requesting_user, update, username=None):
    """
    Update user account information.

    Note:
        It is up to the caller of this method to enforce the contract that this method is only called
        with the user who made the request.

    Override description:
        Adding processing for extended profile fields.

    Arguments:
        requesting_user (User): The user requesting to modify account information. Only the user with username
            'username' has permissions to modify account information.
        update (dict): The updated account field values.
        username (str): Optional username specifying which account should be updated. If not specified,
            `requesting_user.username` is assumed.

    Raises:
        errors.UserNotFound: no user with username `username` exists (or `requesting_user.username` if
            `username` is not specified)
        errors.UserNotAuthorized: the requesting_user does not have access to change the account
            associated with `username`
        errors.AccountValidationError: the update was not attempted because validation errors were found with
            the supplied update
        errors.AccountUpdateError: the update could not be completed. Note that if multiple fields are updated at the
            same time, some parts of the update may have been successful, even if an errors.AccountUpdateError is
            returned; in particular, the user account (not including e-mail address) may have successfully been updated,
            but then the e-mail change request, which is processed last, may throw an error.
        errors.UserAPIInternalError: the operation failed due to an unexpected error.

    """
    # Get user
    if username is None:
        username = requesting_user.username
    if requesting_user.username != username:
        raise errors.UserNotAuthorized()
    user, user_profile = _get_user_and_profile(username)

    # Validate fields to update
    field_errors = {}
    _validate_read_only_fields(user, update, field_errors)

    user_serializer = AccountUserSerializer(user, data=update)
    legacy_profile_serializer = AccountLegacyProfileSerializer(user_profile, data=update)
    for serializer in user_serializer, legacy_profile_serializer:
        add_serializer_errors(serializer, update, field_errors)

    _validate_email_change(user, update, field_errors)
    _validate_secondary_email(user, update, field_errors)
    old_name = _validate_name_change(user_profile, update, field_errors)
    old_language_proficiencies = _get_old_language_proficiencies_if_updating(user_profile, update)

    if field_errors:
        raise errors.AccountValidationError(field_errors)

    # Save requested changes
    try:
        for serializer in user_serializer, legacy_profile_serializer:
            serializer.save()

        _update_preferences_if_needed(update, requesting_user, user)
        _notify_language_proficiencies_update_if_needed(update, user, user_profile, old_language_proficiencies)
        _store_old_name_if_needed(old_name, user_profile, requesting_user)
        _update_extended_profile_if_needed(update, user_profile)
        _update_state_if_needed(update, user_profile)
        # Start of override
        _update_additional_extended_profile_fields_if_needed(update, user)
        # End of override

    except errors.PreferenceValidationError as err:
        raise errors.AccountValidationError(err.preference_errors)  # lint-amnesty, pylint: disable=raise-missing-from
    except (errors.AccountUpdateError, errors.AccountValidationError) as err:
        raise err
    except Exception as err:
        raise errors.AccountUpdateError(  # lint-amnesty, pylint: disable=raise-missing-from
            f"Error thrown when saving account updates: '{str(err)}'"
        )

    _send_email_change_requests_if_needed(update, user)


def _update_additional_extended_profile_fields_if_needed(data, user):
    """
    Updating fields for an extended profile created in the Onboarding app.
    """
    if 'english_proficiency' in data:
        user.extended_profile.english_proficiency = data['english_proficiency']
        user.extended_profile.save()
