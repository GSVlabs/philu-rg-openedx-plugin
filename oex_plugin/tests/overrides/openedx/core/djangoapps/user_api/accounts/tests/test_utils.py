"""Override for test utils"""

MODIFIED_PLATFORMS = ['twitter']

MODIFIED_TEST_DATA = [
    ('twitter', 'https://www.x.com/edX/', 'https://www.x.com/edX', True),
    ('twitter', 'https://www.x.com/edX/123s', None, False),
    ('twitter', 'x.com/edX', 'https://www.x.com/edX', True),
    ('twitter', 'x.com/edX?foo=bar', 'https://www.x.com/edX?foo=bar', True),
    ('twitter', 'x.com/test.user', 'https://www.x.com/test.user', True),
]


def test_data_generator():
    for data in MODIFIED_TEST_DATA:
        yield data

    yield None


platform_data_generator = test_data_generator()


def test_social_link_input(original_test, self, platform_name, link_input, formatted_link_expected, is_valid_expected):
    """
    Verify that social links are correctly validated and formatted.
    """

    if platform_name in MODIFIED_PLATFORMS:
        test_data = next(platform_data_generator, None)
        if test_data:
            original_test(self, *test_data)
    else:
        original_test(self, platform_name, link_input, formatted_link_expected, is_valid_expected)
