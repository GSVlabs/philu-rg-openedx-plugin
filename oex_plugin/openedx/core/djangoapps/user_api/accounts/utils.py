"""
Module for platform overrides.
"""

import re

from django.conf import settings


# lint-amnesty, pylint: disable=unused-argument
def get_username_from_social_link(prev_func, platform_name, new_social_link):
    """
    Returns the username given a social link.

    The override changes regex to allow url with params.

    Uses the following logic to parse new_social_link into a username:
    1) If an empty string, returns it as the username.
    2) Given a URL, attempts to parse the username from the url and return it.
    3) Given a non-URL, returns the entire string as username if valid.
    4) If no valid username is found, returns None.
    """
    # Blank social links should return '' or None as was passed in.
    if not new_social_link:
        return new_social_link

    # start OeX override
    url_stub = re.escape(settings.SOCIAL_PLATFORMS[platform_name]['url_stub'])
    username_match = re.search(r'(www\.)?' + url_stub + r'(?P<username>.+?)(?:/)?$', new_social_link, re.IGNORECASE)
    # end OeX override

    if username_match:
        username = username_match.group('username')
    else:
        username = new_social_link

    # Ensure the username is a valid username.
    if '/' in username:
        return None

    return username
