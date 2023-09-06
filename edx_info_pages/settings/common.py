import os
from path import Path


def plugin_settings(settings):
    settings.INSTALLED_APPS.insert(0, 'modeltranslation')
    settings.INSTALLED_APPS.append('tinymce')

    # Supported translation languages
    settings.MODELTRANSLATION_LANGUAGES = getattr(
        settings,
        'MODELTRANSLATION_LANGUAGES',
        (settings.LANGUAGE_CODE, )
    )

    # Default language
    settings.MODELTRANSLATION_DEFAULT_LANGUAGE = settings.LANGUAGE_CODE

    # Plugin templates registration
    APP_ROOT = Path(__file__).parent.dirname()
    INFO_PAGES_TEMPLATE_DIR = os.path.join(APP_ROOT, 'templates')
    settings.MAKO_TEMPLATE_DIRS_BASE.append(INFO_PAGES_TEMPLATE_DIR)

    # TinyMCE settings
    settings.TINYMCE_DEFAULT_CONFIG = {
        'plugins': "table,spellchecker,paste,searchreplace,image,link",
        'theme': "silver",
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10,
        'style_formats': [
            {'title': 'Black text', 'inline': 'span', 'styles': {'color': '#000'}},
            {'title': 'Red text', 'inline': 'span', 'styles': {'color': '#f00'}},
            {'title': 'Yellow text', 'inline': 'span', 'styles': {'color': '#ff0'}},
            {'title': 'Green text', 'inline': 'span', 'styles': {'color': '#0f0'}},
            {'title': 'Cyan text', 'inline': 'span', 'styles': {'color': '#0ff'}},
            {'title': 'Blue text', 'inline': 'span', 'styles': {'color': '#00f'}},
            {'title': 'White text', 'inline': 'span', 'styles': {'color': '#fff'}},
            {'title': 'White background', 'inline': 'span', 'styles': {'background': '#fff'}},
            {'title': 'Blue background', 'inline': 'span', 'styles': {'background': '#00f'}},
            {'title': 'Cyan background', 'inline': 'span', 'styles': {'background': '#0ff'}},
            {'title': 'Green background', 'inline': 'span', 'styles': {'background': '#0f0'}},
            {'title': 'Yellow background', 'inline': 'span', 'styles': {'background': '#ff0'}},
            {'title': 'Red background', 'inline': 'span', 'styles': {'background': '#f00'}},
            {'title': 'Black background', 'inline': 'span', 'styles': {'background': '#000'}},
        ]
    }

    settings.OVERRIDE_INFO_PAGES_RENDER = ('edx_info_pages.views.info_page_render',)