import os
from path import Path


def plugin_settings(settings):
    settings.INSTALLED_APPS.append('multiselectfield')

    # Plugin templates registration
    APP_ROOT = Path(__file__).parent.dirname()
    CUSTOM_FIELDS_DIR = os.path.join(APP_ROOT, 'templates')
    settings.MAKO_TEMPLATE_DIRS_BASE.append(CUSTOM_FIELDS_DIR)
