"""Test name validation"""
from unittest.mock import MagicMock

from oex_plugin.openedx.core.djangoapps.user_api.accounts.api import get_name_validation_error


def test_get_name_validation_error():
    """
    The positive case when name length satisfies the validation.
    """
    prev_func_mock = MagicMock()
    prev_func_mock.return_value = None

    result = get_name_validation_error(prev_func_mock, "John Doe")

    assert result is None


def test_get_name_validation_error_too_long():
    """
    Test validation error when the name is too long.
    """
    prev_func_mock = MagicMock()
    prev_func_mock.return_value = None

    result = get_name_validation_error(prev_func_mock, "A" * 256)

    assert result == "Full name can't be longer than 255 symbols"
