"""
Production settings required by the RG OeX Plugin in context of LMS.
"""
from oex_plugin.settings.common.production import plugin_settings as common_production_settings


def plugin_settings(settings):
    """
    Production settings overrides for LMS.
    """
    common_production_settings(settings)
    # ======================================= General settings modifications ======================================= #
    settings.SOCIAL_PLATFORMS["twitter"] = {
        "display_name": "Twitter",
        "url_stub": "x.com/",
        "example": "https://www.x.com/username"
    }
    # ================================================== Overrides ================================================== #
    settings.OVERRIDE_GET_USER_COUNT = "oex_plugin.lms.djangoapps.grades.rest_api.v1.gradebook_view._get_user_count"
    settings.OVERRIDE_GET_NAME_VALIDATION_ERROR = (
        "oex_plugin.openedx.core.djangoapps.user_api.accounts.api.get_name_validation_error"
    )
    settings.OVERRIDE_GET_USERNAME_FOR_SOCIAL_LINK = (
        "oex_plugin.openedx.core.djangoapps.user_api.accounts.utils.get_username_from_social_link"
    )
