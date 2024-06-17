from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response

from onboarding.models import EnglishProficiency, OrgSector, TotalEmployee
from openedx.core.djangoapps.user_api.accounts.api import get_account_settings
from openedx.core.djangoapps.user_api.errors import UserNotFound


def retrieve(original_func, self, request, username):
    """
    A method for retrieving user account settings by username.

    Override description:
        Extends account customization by adding an English proficiency level option.

    GET /api/user/v1/accounts/{username}/
    """
    try:
        account_settings = get_account_settings(
            request, [username], view=request.query_params.get('view'))
    except UserNotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Start of override
    english_proficiency_options = [
        {'value': eng_prof.code, 'label': eng_prof.label} for eng_prof in EnglishProficiency.objects.all()
    ]
    total_employee_options = TotalEmployee.objects.get_choices()
    org_type_options = OrgSector.objects.get_choices()
    is_org_registered_options = [(is_reg, _(is_reg)) for is_reg in ("Yes", "No", "I don't know")]

    account_settings[0].update({
        'english_proficiency_options': english_proficiency_options,
        'custom_fields': {
            'total_employee_options': total_employee_options,
            'org_type_options': org_type_options,
            'is_org_registered_options': is_org_registered_options,
        }
    })
    # End of override

    return Response(account_settings[0])
