"""
oex_plugin Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginSettings, PluginURLs


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
            'cms.djangoapp': {
                'production': {
                    PluginSettings.RELATIVE_PATH: 'settings.production',
                },
                'devstack': {
                    PluginSettings.RELATIVE_PATH: 'settings.devstack',
                },
            },
        },
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: 'oex_plugin',
                PluginURLs.APP_NAME: 'oex_plugin',
                PluginURLs.REGEX: '',
                PluginURLs.RELATIVE_PATH: 'lms.urls',
            },
            'cms.djangoapp': {
                PluginURLs.NAMESPACE: 'oex_plugin',
                PluginURLs.APP_NAME: 'oex_plugin',
                PluginURLs.REGEX: '',
                PluginURLs.RELATIVE_PATH: 'cms.urls',
            },
        },
    }
