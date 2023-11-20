"""
Module for platform overrides.
"""

from django.utils.translation import gettext_lazy as _


def get_name_validation_error(prev_func, name):
    """
    Addition validation for allowed name length.
    """
    if name and len(name) > 255:
        return _("Full name can't be longer than 255 symbols")

    return prev_func(name)
