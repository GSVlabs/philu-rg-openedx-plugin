"""Override for user API tests"""
from openedx.core.djangoapps.user_api.accounts.api import get_account_settings, update_account_settings


def test_set_multiple_social_links(original_test, self):  # pylint: disable=unused-argument
    # twitter url changed to x.com
    social_links = [
        dict(platform="facebook", social_link=f"https://www.facebook.com/{self.user.username}"),
        dict(platform="twitter", social_link=f"https://www.x.com/{self.user.username}"),
    ]
    update_account_settings(self.user, {"social_links": social_links})
    account_settings = get_account_settings(self.default_request)[0]
    assert account_settings['social_links'] == social_links


def test_add_social_links(original_test, self):  # pylint: disable=unused-argument
    original_social_links = [
        dict(platform="facebook", social_link=f"https://www.facebook.com/{self.user.username}")
    ]
    update_account_settings(self.user, {"social_links": original_social_links})

    # twitter url changed to x.com
    extra_social_links = [
        dict(platform="twitter", social_link=f"https://www.x.com/{self.user.username}"),
        dict(platform="linkedin", social_link=f"https://www.linkedin.com/in/{self.user.username}"),
    ]
    update_account_settings(self.user, {"social_links": extra_social_links})

    account_settings = get_account_settings(self.default_request)[0]
    assert account_settings['social_links'] == \
        sorted((original_social_links + extra_social_links), key=(lambda s: s['platform']))


def test_replace_social_links(original_test, self):  # pylint: disable=unused-argument
    original_facebook_link = dict(platform="facebook", social_link="https://www.facebook.com/myself")
    # twitter url changed to x.com
    original_twitter_link = dict(platform="twitter", social_link="https://www.x.com/myself")
    update_account_settings(self.user, {"social_links": [original_facebook_link, original_twitter_link]})

    modified_facebook_link = dict(platform="facebook", social_link="https://www.facebook.com/new_me")
    update_account_settings(self.user, {"social_links": [modified_facebook_link]})

    account_settings = get_account_settings(self.default_request)[0]
    assert account_settings['social_links'] == [modified_facebook_link, original_twitter_link]


def test_remove_social_link(original_test, self):  # pylint: disable=unused-argument
    original_facebook_link = dict(platform="facebook", social_link="https://www.facebook.com/myself")
    # twitter url changed to x.com
    original_twitter_link = dict(platform="twitter", social_link="https://www.x.com/myself")
    update_account_settings(self.user, {"social_links": [original_facebook_link, original_twitter_link]})

    removed_facebook_link = dict(platform="facebook", social_link="")
    update_account_settings(self.user, {"social_links": [removed_facebook_link]})

    account_settings = get_account_settings(self.default_request)[0]
    assert account_settings['social_links'] == [original_twitter_link]
