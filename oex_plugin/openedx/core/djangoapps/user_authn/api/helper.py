
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


def _field_can_be_saved(original_func, self, field):
    """
    Adding fields for the registration form (creating an organization).
    
    Checks if the field exists in UserProfile Model fields or extended_profile configuration,
    if it exists, then the field is valid to save because the meta field in UserProfile model
    only stores those fields which are available in extended_profile configuration, so we only
    want to send those fields which can be saved.
    """
    return (field in self.user_profile_fields or
            field in configuration_helpers.get_value('extended_profile_fields', []) or
            field in [
                "terms_of_service",
                "honor_code",
                # Start of override
                "organization_type",
                "is_organization_registered",
                "organization_size",
                # End of override
            ])
