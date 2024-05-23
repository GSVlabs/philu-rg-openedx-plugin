
from django.conf import settings
from django.utils.translation import gettext as _
from openedx.core.djangoapps.user_authn.api.constants import SUPPORTED_FIELDS_TYPES
from onboarding.models import OrgSector, TotalEmployee


def add_organization_type_field(original_func, is_field_required=False):
    """
    Returns the organization type field description.
    
    This function is necessary to create a context for a custom field.
    """
    # Translators: This label appears above a dropdown menu used to select
    # the user's highest completed organization type.
    organization_type_label = _("- Select -")
    description = _("Please select the type of organization that you work for.")

    # pylint: disable=translation-of-non-string
    options = [(os.code, _(os.label)) for os in OrgSector.objects.all()]

    return {
        'name': 'organization_type',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': organization_type_label,
        'description': description,
        'options': options,
    }


def add_is_organization_registered_field(original_func, is_field_required=False):
    """
    Returns the is_organization_registered field description.
    
    This function is necessary to create a context for a custom field.
    """
    # Translators: This label appears above a dropdown menu used to select
    # is organization registered.
    is_organization_registered_label = _("- Select -")
    description = _("Is your organization registered as a 501c3?")

    # pylint: disable=translation-of-non-string
    options = [(is_reg, _(is_reg)) for is_reg in ("Yes", "No", "I don't know")]

    return {
        'name': 'is_organization_registered',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': is_organization_registered_label,
        'description': description,
        'options': options,
    }


def add_organization_size_field(original_func, is_field_required=False):
    """
    Returns the organization size field description.
    
    This function is necessary to create a context for a custom field.
    """
    # Translators: This label appears above a dropdown menu used to select
    # is organization size.
    organization_size_label = _("- Select -")
    description = _("Please select the number of employees in your organization.")

    # pylint: disable=translation-of-non-string
    options = [(total_empl.code, _(total_empl.label)) for total_empl in TotalEmployee.objects.all()]

    if settings.ENABLE_COPPA_COMPLIANCE:
        options = list(filter(lambda op: op[0] != 'el', options))

    return {
        'name': 'organization_size',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': organization_size_label,
        'description': description,
        'options': options,
    }
