from django.apps import AppConfig

from edx_django_utils.plugins.constants import PluginSettings, PluginURLs


class EdxInfoPagesConfig(AppConfig):
    name = 'edx_info_pages'
    verbose_name = "Edx info pages"

    plugin_app = {
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: 'edx_info_pages',
                PluginURLs.APP_NAME: 'edx_info_pages',
                PluginURLs.REGEX: '',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'common': 
                    {PluginSettings.RELATIVE_PATH: 'settings.common'},
            }
        }
    }
