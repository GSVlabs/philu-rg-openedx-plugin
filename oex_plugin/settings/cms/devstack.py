"""
Devstack settings required by the RG OeX Plugin in context of LMS.
"""
from oex_plugin.settings.common.devstack import plugin_settings as common_devstack_settings


def plugin_settings(settings):
    """
    Overrides for the LMS's devstack.py settings.
    """
    common_devstack_settings(settings)

    settings.CSRF_TRUSTED_ORIGINS = (
        settings.DISCUSSIONS_MICROFRONTEND_URL,
        settings.LIBRARY_AUTHORING_MICROFRONTEND_URL,
        settings.COURSE_AUTHORING_MICROFRONTEND_URL,
    )
