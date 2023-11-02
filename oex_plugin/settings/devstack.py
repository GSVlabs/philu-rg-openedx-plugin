"""
Devstack settings variables required by the RG OeX Plugin.
"""
import logging

from lms.envs.common import _make_mako_template_dirs
from openedx.core.lib.derived import derive_settings

log = logging.getLogger(__name__)


def plugin_settings(settings):

    settings.ENABLE_COMPREHENSIVE_THEMING = True
    settings.COMPREHENSIVE_THEME_DIRS = [
        "/edx/app/edx-themes/"
    ]
    settings.COURSE_ABOUT_VISIBILITY_PERMISSION = 'see_about_page'
    settings.DEFAULT_SITE_THEME = 'edx-theme'
    settings.TEMPLATES[1]["DIRS"] = _make_mako_template_dirs
    settings.ELASTIC_SEARCH_CONFIG = [
        {
            'use_ssl': False,
            'host': 'elasticsearch7.devstack.edx',
            'port': 9200
        }
    ]
    derive_settings(settings.__name__)

    settings.INACTIVE_USER_URL = f'http{"s" if settings.HTTPS == "on" else ""}://{settings.CMS_BASE}'
