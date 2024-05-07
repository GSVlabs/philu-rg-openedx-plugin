from django.apps import AppConfig

from edx_django_utils.plugins.constants import PluginURLs


class OnboardingConfig(AppConfig):
    name = 'onboarding'
    verbose_name = "Onboarding"

    plugin_app = {
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: 'onboarding',
                PluginURLs.APP_NAME: 'onboarding',
                PluginURLs.REGEX: '',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }
