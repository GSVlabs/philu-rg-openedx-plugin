"""
Devstack settings required by the RG OeX Plugin in context of LMS.
"""


def plugin_settings(settings):
    """
    Overrides for LMS's test settings.
    """
    # ======================================= General settings modifications ======================================= #
    settings.SOCIAL_MEDIA_FOOTER_ACE_URLS["twitter"] = "https://x.com/edXOnline"
    settings.SOCIAL_PLATFORMS["twitter"] = {
        "display_name": "Twitter",
        "url_stub": "x.com/",
        "example": "https://www.x.com/username"
    }
    settings.SOCIAL_MEDIA_FOOTER_ACE_URLS["twitter"] = "https://x.com/edXOnline"
    # ================================================== Overrides ================================================== #
    TEST_OVERRIDES_PATH = "oex_plugin.tests.overrides"
    ACCOUNTS_TESTS_PATH = "openedx.core.djangoapps.user_api.accounts.tests"
    SCHEDULES_TEST_RESOLVER_PATH = "openedx.core.djangoapps.schedules.tests.test_resolvers"

    settings.OVERRIDE_TEST_SOCIAL_LINK_INPUT = (
        f"{TEST_OVERRIDES_PATH}.{ACCOUNTS_TESTS_PATH}.test_utils.test_social_link_input"
    )
    settings.OVERRIDE_TEST_SET_MULTIPLE_SOCIAL_LINKS = (
        f"{TEST_OVERRIDES_PATH}.{ACCOUNTS_TESTS_PATH}.test_api.test_set_multiple_social_links"
    )
    settings.OVERRIDE_TEST_REMOVE_SOCIAL_LINK = (
        f"{TEST_OVERRIDES_PATH}.{ACCOUNTS_TESTS_PATH}.test_api.test_remove_social_link"
    )
    settings.OVERRIDE_TEST_ADD_SOCIAL_LINKS = (
        f"{TEST_OVERRIDES_PATH}.{ACCOUNTS_TESTS_PATH}.test_api.test_add_social_links"
    )
    settings.OVERRIDE_TEST_REPLACE_SOCIAL_LINKS = (
        f"{TEST_OVERRIDES_PATH}.{ACCOUNTS_TESTS_PATH}.test_api.test_replace_social_links"
    )
    settings.OVERRIDE_TEST_UPDATE_RESOLVER = (
        f"{TEST_OVERRIDES_PATH}.{SCHEDULES_TEST_RESOLVER_PATH}.test_schedule_context_update_resolver"
    )
    settings.OVERRIDE_TEST_NEXT_SECTION_RESOLVER = (
        f"{TEST_OVERRIDES_PATH}.{SCHEDULES_TEST_RESOLVER_PATH}.test_schedule_context_next_section_resolver"
    )
    settings.OVERRIDE_BRANDING_TEST_GET_FOOTER = (
        f"{TEST_OVERRIDES_PATH}.lms.djangoapps.branding.tests.test_api.test_get_footer"
    )
    settings.OVERRIDE_GET_USERNAME_FOR_SOCIAL_LINK = (
        "oex_plugin.openedx.core.djangoapps.user_api.accounts.utils.get_username_from_social_link"
    )
