"""
Devstack settings required by the RG OeX Plugin in context of LMS.
"""
from oex_plugin.settings.common.devstack import plugin_settings as common_devstack_settings


def plugin_settings(settings):
    """
    Overrides for the LMS's devstack.py settings.
    """
    common_devstack_settings(settings)
    # ======================================= General settings modifications ======================================= #
    settings.SOCIAL_PLATFORMS["twitter"] = {
        "display_name": "Twitter",
        "url_stub": "x.com/",
        "example": "https://www.x.com/username"
    }
    settings.SOCIAL_MEDIA_FOOTER_ACE_URLS["twitter"] = "https://x.com/edXOnline"
    # NOTE: we can't just use the original settings values like `settings.SOME_MFE_URL` because
    # they are defined after the plugin settings injection in the devstack settings.
    settings.CSRF_TRUSTED_ORIGINS = (
        'http://localhost:1999',  # AUTHN_MICROFRONTEND_URL,
        'http://localhost:1995',  # PROFILE_MICROFRONTEND_URL,
        'http://localhost:1996',  # ORDER_HISTORY_MICROFRONTEND_URL, LEARNER_HOME_MICROFRONTEND_URL,
        'http://localhost:1997',  # ACCOUNT_MICROFRONTEND_URL,
        'http://localhost:2000',  # LEARNING_MICROFRONTEND_URL,
        'http://localhost:1993',  # ORA_GRADING_MICROFRONTEND_URL,
        'http://localhost:1984',  # COMMUNICATIONS_MICROFRONTEND_URL,
        'http://localhost:2002',  # DISCUSSIONS_MICROFRONTEND_URL,
    )
    # ================================================== Overrides ================================================== #
    settings.OVERRIDE_GET_USER_COUNT = "oex_plugin.lms.djangoapps.grades.rest_api.v1.gradebook_view._get_user_count"
    settings.OVERRIDE_GET_NAME_VALIDATION_ERROR = (
        "oex_plugin.openedx.core.djangoapps.user_api.accounts.api.get_name_validation_error"
    )
    settings.OVERRIDE_GET_USERNAME_FOR_SOCIAL_LINK = (
        "oex_plugin.openedx.core.djangoapps.user_api.accounts.utils.get_username_from_social_link"
    )
