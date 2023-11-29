"""Override for Branding API tests"""
from django.conf import settings
from lms.djangoapps.branding.api import get_footer


def test_get_footer(original_test, self):  # pylint: disable=unused-argument
    actual_footer = get_footer(is_secure=True)
    business_url = 'https://business.edx.org/?utm_campaign=edX.org+Referral&utm_source=edX.org&utm_medium=Footer'
    facebook_url = 'http://www.facebook.com/EdxOnline'
    linkedin_url = 'http://www.linkedin.com/company/edx'
    # twitter url changed to x.com
    twitter_url = 'https://x.com/edXOnline'
    reddit_url = 'http://www.reddit.com/r/edx'
    expected_footer = {
        'copyright': '\xa9 \xe9dX.  All rights reserved except where noted. '
                     ' edX, Open edX and their respective logos are '
                     'registered trademarks of edX Inc.',
        'navigation_links': [
            {'url': 'https://edx.org/about-us', 'name': 'about', 'title': 'About'},
            {'url': 'https://business.edx.org', 'name': 'enterprise', 'title': '\xe9dX for Business'},
            {'url': 'https://edx.org/edx-blog', 'name': 'blog', 'title': 'Blog'},
            {'url': 'https://edx.org/news-announcements', 'name': 'news', 'title': 'News'},
            {'url': 'https://example.support.edx.org/hc/en-us', 'name': 'help-center', 'title': 'Help Center'},
            {'url': '/support/contact_us', 'name': 'contact', 'title': 'Contact'},
            {'url': 'https://edx.org/careers', 'name': 'careers', 'title': 'Careers'},
            {'url': 'https://edx.org/donate', 'name': 'donate', 'title': 'Donate'}
        ],
        'business_links': [
            {'url': 'https://edx.org/about-us', 'name': 'about', 'title': 'About'},
            {'url': business_url, 'name': 'enterprise', 'title': '\xe9dX for Business'},
            {'url': 'https://edx.org/affiliate-program', 'name': 'affiliates', 'title': 'Affiliates'},
            {'url': 'https://open.edx.org', 'name': 'openedx', 'title': 'Open edX'},
            {'url': 'https://edx.org/careers', 'name': 'careers', 'title': 'Careers'},
            {'url': 'https://edx.org/news-announcements', 'name': 'news', 'title': 'News'},

        ],
        'more_info_links': [
            {'url': 'https://edx.org/edx-terms-service',
                'name': 'terms_of_service_and_honor_code',
                'title': 'Terms of Service & Honor Code'},
            {'url': 'https://edx.org/edx-privacy-policy', 'name': 'privacy_policy', 'title': 'Privacy Policy'},
            {'url': 'https://edx.org/accessibility',
                'name': 'accessibility_policy',
                'title': 'Accessibility Policy'},
            {'url': 'https://edx.org/trademarks', 'name': 'trademarks', 'title': 'Trademark Policy'},
            {'url': 'https://edx.org/sitemap', 'name': 'sitemap', 'title': 'Sitemap'},

        ],
        'connect_links': [
            {'url': 'https://edx.org/edx-blog', 'name': 'blog', 'title': 'Blog'},
            # pylint: disable=line-too-long
            {'url': f'{settings.LMS_ROOT_URL}/support/contact_us', 'name': 'contact', 'title': 'Contact Us'},
            {'url': 'https://example.support.edx.org/hc/en-us', 'name': 'help-center', 'title': 'Help Center'},
            {'url': 'https://edx.org/media-kit', 'name': 'media_kit', 'title': 'Media Kit'},
            {'url': 'https://edx.org/donate', 'name': 'donate', 'title': 'Donate'}
        ],
        'legal_links': [
            {'url': 'https://edx.org/edx-terms-service',
                'name': 'terms_of_service_and_honor_code',
                'title': 'Terms of Service & Honor Code'},
            {'url': 'https://edx.org/edx-privacy-policy', 'name': 'privacy_policy', 'title': 'Privacy Policy'},
            {'url': 'https://edx.org/accessibility',
                'name': 'accessibility_policy',
                'title': 'Accessibility Policy'},
            {'url': 'https://edx.org/sitemap', 'name': 'sitemap', 'title': 'Sitemap'},
            {'name': 'media_kit',
                'title': 'Media Kit',
                'url': 'https://edx.org/media-kit'}
        ],
        'social_links': [
            {'url': facebook_url, 'action': 'Like \xe9dX on Facebook', 'name': 'facebook',
                'icon-class': 'fa-facebook-square', 'title': 'Facebook'},
            {'url': twitter_url, 'action': 'Follow \xe9dX on Twitter', 'name': 'twitter',
                'icon-class': 'fa-twitter-square', 'title': 'Twitter'},
            {'url': linkedin_url, 'action': 'Follow \xe9dX on LinkedIn', 'name': 'linkedin',
                'icon-class': 'fa-linkedin-square', 'title': 'LinkedIn'},
            {'url': '#', 'action': 'Follow \xe9dX on Instagram', 'name': 'instagram',
                'icon-class': 'fa-instagram', 'title': 'Instagram'},
            {'url': reddit_url, 'action': 'Subscribe to the \xe9dX subreddit',
                'name': 'reddit', 'icon-class': 'fa-reddit-square', 'title': 'Reddit'}
        ],
        'mobile_links': [],
        # NOTE: logo_image is changed comparing to the original test because of RG branding customization
        'logo_image': 'https://edx.org/static/images/logo.png',
        'openedx_link': {
            'url': 'https://open.edx.org',
            'image': 'https://logos.openedx.org/open-edx-logo-tag.png',
            'title': 'Powered by Open edX'
        },
        'edx_org_link': {
            'url': 'https://www.edx.org/?'
                   'utm_medium=affiliate_partner'
                   '&utm_source=opensource-partner'
                   '&utm_content=open-edx-partner-footer-link'
                   '&utm_campaign=open-edx-footer',
            'text': 'Take free online courses at edX.org',
        },
    }
    assert actual_footer == expected_footer
