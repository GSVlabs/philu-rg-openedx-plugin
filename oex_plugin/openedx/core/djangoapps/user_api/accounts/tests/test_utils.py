"""
Tests for the utils module.
"""

import pytest
from django.conf import settings

from oex_plugin.openedx.core.djangoapps.user_api.accounts.utils import get_username_from_social_link

SOCIAL_PLATFORMS = settings.SOCIAL_PLATFORMS


@pytest.mark.parametrize("platform_name", SOCIAL_PLATFORMS.keys())
def test_get_username_from_social_link_valid_url(platform_name):
    """
    Test the positive flow with correct links.
    """
    platform_info = SOCIAL_PLATFORMS[platform_name]
    result = get_username_from_social_link(None, platform_name, platform_info["example"])
    assert result == "username"


@pytest.mark.parametrize("platform_name", SOCIAL_PLATFORMS.keys())
def test_get_username_from_social_link_url_with_params(platform_name):
    """
    Test positive flow for links with parameters.
    """
    platform_info = SOCIAL_PLATFORMS[platform_name]
    result = get_username_from_social_link(None, platform_name, f"{platform_info['url_stub']}edX?foo=bar")
    assert result == "edX?foo=bar"


@pytest.mark.parametrize("platform_name", SOCIAL_PLATFORMS.keys())
def test_get_username_from_social_link_invalid_characters(platform_name):
    """
    Test for links with invalid username.

    The username is invalid when it has `/` in it and we should receive None as a result.
    """
    platform_info = SOCIAL_PLATFORMS[platform_name]
    result = get_username_from_social_link(None, platform_name, f"{platform_info['url_stub']}/us/er/name")
    assert result is None


@pytest.mark.parametrize("platform_name", SOCIAL_PLATFORMS.keys())
def test_get_username_from_social_link_no_match(platform_name):
    """
    Test result when there is no regex match for username.
    """
    platform_info = SOCIAL_PLATFORMS[platform_name]
    result = get_username_from_social_link(None, platform_name, f"{platform_info['url_stub']}")
    assert result is None


@pytest.mark.parametrize("platform_name", SOCIAL_PLATFORMS.keys())
def test_get_username_from_social_link_no_link(platform_name):
    """
    Test result when no link is provided.
    """
    result = get_username_from_social_link(None, platform_name, None)
    assert result is None
