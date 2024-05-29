"""AppConfig of custom_fields app"""

from django.apps import AppConfig

from edx_django_utils.plugins.constants import PluginSettings


class CustomFieldsConfig(AppConfig):
    name = 'custom_fields'
    verbose_name = "Custom Fields"
    
    plugin_app = {
        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'common': 
                    {PluginSettings.RELATIVE_PATH: 'settings.common'},
            }
        }
    }
