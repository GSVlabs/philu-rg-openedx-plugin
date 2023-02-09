"""
oex_plugin Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginSettings, PluginURLs

import oex_plugin.override_monkey.rg_xmodule  # NOTE: import is needed to invoke monkey overrides


class OexPluginConfig(AppConfig):
    """
    Configuration for the oex_plugin Django application.
    """

    name = 'oex_plugin'

    verbose_name = 'RG Open edX Plugin'

    plugin_app = {
        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'production': {
                    PluginSettings.RELATIVE_PATH: 'settings.production',
                },
                'devstack': {
                    PluginSettings.RELATIVE_PATH: 'settings.devstack',
                },
            },
        },
    }
