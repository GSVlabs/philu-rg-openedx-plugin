from rest_framework import status
from rest_framework.response import Response

from onboarding.models import EnglishProficiency
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
    account_settings[0]['english_proficiency_options'] = english_proficiency_options
    # End of override

    return Response(account_settings[0])
