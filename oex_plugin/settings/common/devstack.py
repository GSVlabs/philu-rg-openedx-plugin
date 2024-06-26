"""
Common Devstack settings required by the RG OeX Plugin.
"""
from lms.envs.common import _make_mako_template_dirs
from openedx.core.lib.derived import derive_settings

from oex_plugin.settings.common.production import plugin_settings as common_production_settings


def plugin_settings(settings):
    """
    Overrides for the devstack.py settings.
    """
    common_production_settings(settings)

    settings.COURSE_ABOUT_VISIBILITY_PERMISSION = 'see_about_page'
    settings.TEMPLATES[1]["DIRS"] = _make_mako_template_dirs
    settings.ELASTIC_SEARCH_CONFIG = [
        {
            'use_ssl': False,
            'host': 'elasticsearch710.devstack.edx',
            'port': 9200
        }
    ]
    derive_settings(settings.__name__)
