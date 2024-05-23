"""
Registration related views.
"""

from django.conf import settings
from django.core.exceptions import NON_FIELD_ERRORS, PermissionDenied
from django.core.validators import ValidationError
from django.http import HttpResponseForbidden
from django.utils.translation import gettext as _


from common.djangoapps.student.helpers import AccountValidationError
from onboarding.models import UserExtendedProfile
from openedx.core.djangoapps.user_authn.views.register import create_account_with_params


def _create_account(original_func, self, request, data):
    """
    Extending standard registration by creating an instance UserExtendedProfile.
    """
    response, user = None, None
    try:
        user = create_account_with_params(request, data)
        # Start of override for custom registration
        UserExtendedProfile.objects.create(user=user)
        # End of override
    except AccountValidationError as err:
        errors = {
            err.field: [{"user_message": str(err)}]
        }
        response = self._create_response(request, errors, status_code=409, error_code=err.error_code)
    except ValidationError as err:
        # Should only get field errors from this exception
        assert NON_FIELD_ERRORS not in err.message_dict

        # Error messages are returned as arrays from ValidationError
        error_code = err.message_dict.get('error_code', ['validation-error'])[0]

        # Only return first error for each field
        errors = {
            field: [{"user_message": error} for error in error_list]
            for field, error_list in err.message_dict.items() if field != 'error_code'
        }
        response = self._create_response(request, errors, status_code=400, error_code=error_code)
    except PermissionDenied:
        response = HttpResponseForbidden(_("Account creation not allowed."))

    return response, user
