"""
Override for schedules resolvers tests.
"""


def test_schedule_context_update_resolver(original_test, self):  # pylint: disable=unused-argument
    resolver = self.create_resolver()
    schedules = list(resolver.schedules_for_bin())
    apple_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/store_apple_229x78.jpg'
    google_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/store_google_253x78.jpg'
    apple_store_url = 'https://itunes.apple.com/us/app/edx/id945480667?mt=8'
    google_store_url = 'https://play.google.com/store/apps/details?id=org.edx.mobile'
    facebook_url = 'http://www.facebook.com/EdxOnline'
    linkedin_url = 'http://www.linkedin.com/company/edx'
    # twitter url changed to x.com
    twitter_url = 'https://x.com/edXOnline'
    reddit_url = 'http://www.reddit.com/r/edx'
    facebook_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_1_fb.png'
    linkedin_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_3_linkedin.png'
    twitter_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_2_twitter.png'
    reddit_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_5_reddit.png'
    expected_context = {
        'contact_email': 'info@example.com',
        'contact_mailing_address': '123 Sesame Street',
        'course_ids': [str(self.course.id)],
        'course_name': self.course.display_name,
        'course_url': f'http://learning-mfe/course/{self.course.id}/home',
        'dashboard_url': '/dashboard',
        'homepage_url': '/',
        'mobile_store_logo_urls': {
            'apple': apple_logo_url,
            'google': google_logo_url
        },
        'mobile_store_urls': {
            'apple': apple_store_url,
            'google': google_store_url
        },
        # Override change caused by RG customization for branded template context.
        # Check the `get_base_template_context` method for more info.
        'logo_url': 'http://localhost:8000/static/None/images/',
        'platform_name': '\xe9dX',
        'show_upsell': False,
        'site_configuration_values': {},
        'social_media_logo_urls': {
            'facebook': facebook_logo_url,
            'linkedin': linkedin_logo_url,
            'reddit': reddit_logo_url,
            'twitter': twitter_logo_url
        },
        'social_media_urls': {
            'facebook': facebook_url,
            'linkedin': linkedin_url,
            'reddit': reddit_url,
            'twitter': twitter_url
        },
        'template_revision': 'release',
        'unsubscribe_url': None,
        'week_highlights': ['good stuff'],
        'week_num': 1,
    }
    assert schedules == [(self.user, None, expected_context)]


def test_schedule_context_next_section_resolver(original_test, self):  # pylint: disable=unused-argument
    resolver = self.create_resolver()
    # NOTE: original test checks agains 38 queries, but has actually 39 queries on Devstack
    with self.assertNumQueries(39):
        sc = resolver.get_schedules()
        schedules = list(sc)
    apple_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/store_apple_229x78.jpg'
    google_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/store_google_253x78.jpg'
    apple_store_url = 'https://itunes.apple.com/us/app/edx/id945480667?mt=8'
    google_store_url = 'https://play.google.com/store/apps/details?id=org.edx.mobile'
    facebook_url = 'http://www.facebook.com/EdxOnline'
    linkedin_url = 'http://www.linkedin.com/company/edx'
    # twitter url changed to x.com
    twitter_url = 'https://x.com/edXOnline'
    reddit_url = 'http://www.reddit.com/r/edx'
    facebook_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_1_fb.png'
    linkedin_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_3_linkedin.png'
    twitter_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_2_twitter.png'
    reddit_logo_url = 'http://email-media.s3.amazonaws.com/edX/2021/social_5_reddit.png'
    expected_context = {
        'contact_email': 'info@example.com',
        'contact_mailing_address': '123 Sesame Street',
        'course_ids': [str(self.course.id)],
        'course_name': self.course.display_name,
        'course_url': f'http://learning-mfe/course/{self.course.id}/home',
        'dashboard_url': '/dashboard',
        'homepage_url': '/',
        'mobile_store_logo_urls': {
            'apple': apple_logo_url,
            'google': google_logo_url
        },
        'mobile_store_urls': {
            'apple': apple_store_url,
            'google': google_store_url
        },
        # Override change caused by RG customization for branded template context.
        # Check the `get_base_template_context` method for more info.
        'logo_url': 'http://localhost:8000/static/None/images/',
        'platform_name': '\xe9dX',
        'show_upsell': False,
        'site_configuration_values': {},
        'social_media_logo_urls': {
            'facebook': facebook_logo_url,
            'linkedin': linkedin_logo_url,
            'reddit': reddit_logo_url,
            'twitter': twitter_logo_url
        },
        'social_media_urls': {
            'facebook': facebook_url,
            'linkedin': linkedin_url,
            'reddit': reddit_url,
            'twitter': twitter_url
        },
        'template_revision': 'release',
        'unsubscribe_url': None,
        'week_highlights': ['good stuff 2'],
        'week_num': 2,
    }
    assert schedules == [(self.user, None, expected_context)]
