"""
Production settings required by the RG OeX Plugin in context of LMS.
"""
from oex_plugin.settings.common.production import plugin_settings as common_production_settings


def plugin_settings(settings):
    """
    Production settings overrides for LMS.
    """
    common_production_settings(settings)
    settings.SOCIAL_PLATFORMS["twitter"] = {
        "display_name": "Twitter",
        "url_stub": "x.com/",
        "example": "https://www.x.com/username"
    }
    settings.SOCIAL_MEDIA_FOOTER_ACE_URLS["twitter"] = "https://x.com/edXOnline"
