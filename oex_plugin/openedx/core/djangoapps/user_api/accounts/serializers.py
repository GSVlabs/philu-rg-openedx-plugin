import logging

from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from common.djangoapps.student.models import PendingNameChange
from lms.djangoapps.badges.utils import badges_enabled
from openedx.core.djangoapps.user_api.accounts.utils import is_secondary_email_feature_enabled
from openedx.core.djangoapps.user_api.accounts.serializers import (
    AccountLegacyProfileSerializer,
    LanguageProficiencySerializer,
    SocialLinkSerializer,
    get_profile_visibility,
    get_extended_profile,
    _visible_fields,
)
from openedx.features.name_affirmation_api.utils import get_name_affirmation_service

PROFILE_IMAGE_KEY_PREFIX = 'image_url'
LOGGER = logging.getLogger(__name__)


def to_representation(original_func, self, user):  # lint-amnesty, pylint: disable=arguments-differ
    """
    Overwrite to_native to handle custom logic since we are serializing three models as one here
    :param user: User object
    :return: Dict serialized account
    
    Override description:
        Adding 'english_proficiency' field for account extension.
    """
    try:
        user_profile = user.profile
    except ObjectDoesNotExist:
        user_profile = None
        LOGGER.warning("user profile for the user [%s] does not exist", user.username)

    try:
        account_recovery = user.account_recovery
    except ObjectDoesNotExist:
        account_recovery = None

    try:
        activation_key = user.registration.activation_key
    except ObjectDoesNotExist:
        activation_key = None

    accomplishments_shared = badges_enabled()
    data = {
        "username": user.username,
        "url": self.context.get('request').build_absolute_uri(
            reverse('accounts_api', kwargs={'username': user.username})
        ),
        "email": user.email,
        "id": user.id,
        # For backwards compatibility: Tables created after the upgrade to Django 1.8 will save microseconds.
        # However, mobile apps are not expecting microsecond in the serialized value. If we set it to zero the
        # DRF JSONEncoder will not include it in the serialized value.
        # https://docs.djangoproject.com/en/1.8/ref/databases/#fractional-seconds-support-for-time-and-datetime-fields
        "date_joined": user.date_joined.replace(microsecond=0),
        "last_login": user.last_login,
        "is_active": user.is_active,
        "activation_key": activation_key,
        "bio": None,
        "country": None,
        "state": None,
        "profile_image": None,
        "language_proficiencies": None,
        "name": None,
        "gender": None,
        "goals": None,
        "year_of_birth": None,
        "level_of_education": None,
        "mailing_address": None,
        "requires_parental_consent": None,
        "accomplishments_shared": accomplishments_shared,
        "account_privacy": self.configuration.get('default_visibility'),
        "social_links": None,
        "extended_profile_fields": None,
        "phone_number": None,
        "pending_name_change": None,
        "verified_name": None,
        # Start of override
        "english_proficiency": None,
        "organization": None,
        # End of override
    }

    if user_profile:
        data.update(
            {
                "bio": AccountLegacyProfileSerializer.convert_empty_to_None(user_profile.bio),
                "country": AccountLegacyProfileSerializer.convert_empty_to_None(user_profile.country.code),
                "state": AccountLegacyProfileSerializer.convert_empty_to_None(user_profile.state),
                "profile_image": AccountLegacyProfileSerializer.get_profile_image(
                    user_profile, user, self.context.get('request')
                ),
                "language_proficiencies": LanguageProficiencySerializer(
                    user_profile.language_proficiencies.all().order_by('code'), many=True
                ).data,
                "name": user_profile.name,
                "gender": AccountLegacyProfileSerializer.convert_empty_to_None(user_profile.gender),
                "goals": user_profile.goals,
                "year_of_birth": user_profile.year_of_birth,
                "level_of_education": AccountLegacyProfileSerializer.convert_empty_to_None(
                    user_profile.level_of_education
                ),
                "mailing_address": user_profile.mailing_address,
                "requires_parental_consent": user_profile.requires_parental_consent(),
                "account_privacy": get_profile_visibility(user_profile, user, self.configuration),
                "social_links": SocialLinkSerializer(
                    user_profile.social_links.all().order_by('platform'), many=True
                ).data,
                "extended_profile": get_extended_profile(user_profile),
                "phone_number": user_profile.phone_number,
            }
        )
    # Start of override
    try:
        user_extended_profile = user.extended_profile
        data.update({"english_proficiency": user_extended_profile.english_proficiency})
        if user_org := user_extended_profile.organization:
            data.update({"organization": user_org.get_required_fields_for_account()})
    except AttributeError:
        pass
    # End of override

    try:
        pending_name_change = PendingNameChange.objects.get(user=user)
        data.update({"pending_name_change": pending_name_change.new_name})
    except PendingNameChange.DoesNotExist:
        pass

    name_affirmation_service = get_name_affirmation_service()
    if name_affirmation_service:
        verified_name_obj = name_affirmation_service.get_verified_name(user, is_verified=True)
        if verified_name_obj:
            data.update({"verified_name": verified_name_obj.verified_name})

    if is_secondary_email_feature_enabled():
        data.update(
            {
                "secondary_email": account_recovery.secondary_email if account_recovery else None,
                "secondary_email_enabled": True,
            }
        )

    if self.custom_fields:
        fields = self.custom_fields
    elif user_profile:
        fields = _visible_fields(user_profile, user, self.configuration)
    else:
        fields = self.configuration.get('public_fields')

    return self._filter_fields(
        fields,
        data
    )
