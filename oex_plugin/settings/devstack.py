"""
Devstack settings variables required by the RG OeX Plugin.
"""
from django.conf import settings

from oex_plugin.settings.production import *


try:
    from lms.envs.common import _make_mako_template_dirs
    from openedx.core.lib.derived import derive_settings
except ImportError:
    pass
else:
    ENABLE_COMPREHENSIVE_THEMING = True
    COMPREHENSIVE_THEME_DIRS = [
        "/edx/app/edx-themes/"
    ]
    DEFAULT_SITE_THEME = 'edx-theme'
    settings.TEMPLATES[1]["DIRS"] = _make_mako_template_dirs
    ELASTIC_SEARCH_CONFIG = [
        {
            'use_ssl': False,
            'host': 'elasticsearch7.devstack.edx',
            'port': 9200
        }
    ]
    derive_settings(__name__)
