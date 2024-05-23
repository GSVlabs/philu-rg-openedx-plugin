"""
Common Production settings required by the RG OeX Plugin.
"""
import logging
from subprocess import CalledProcessError, check_output

try:
    import sentry_sdk
    from sentry_sdk.integrations.celery import CeleryIntegration
    from sentry_sdk.integrations.django import DjangoIntegration
except ImportError:
    logger = logging.getLogger(__name__)
    logger.warning(
        "Unable to import sentry_sdk! It's ok for the devstack env though."
    )


def plugin_settings(settings):
    """
    Production settings overrides.
    """
    if RG_SENTRY_DSN := settings.AUTH_TOKENS.get('RG_SENTRY_DSN', None):
        try:
            platform_git_commit = check_output(['git', 'describe', '--always']).strip()
        except (CalledProcessError, OSError):
            platform_git_commit = ''

        sentry_sdk.init(
            RG_SENTRY_DSN,
            auto_enabling_integrations=False,
            integrations=[DjangoIntegration(), CeleryIntegration()],
            environment=settings.ENV_TOKENS.get('RG_SENTRY_ENVIRONMENT', ''),
            release=platform_git_commit,
            send_default_pii=True
        )

    settings.COURSE_ABOUT_VISIBILITY_PERMISSION = 'see_about_page'
    settings.INACTIVE_USER_URL = f'http{"s" if settings.HTTPS == "on" else ""}://{settings.CMS_BASE}'
    settings.OVERRIDE_GET_NAME_VALIDATION_ERROR = (
        'oex_plugin.openedx.core.djangoapps.user_api.accounts.api.get_name_validation_error'
    )
    settings.OVERRIDE_GET_USER_COUNT = 'oex_plugin.lms.djangoapps.grades.rest_api.v1.gradebook_view._get_user_count'
    settings.OVERRIDE_CREATE_ACCOUNT = 'oex_plugin.openedx.core.djangoapps.user_authn.views.register._create_account'
    settings.OVERRIDE_FIELD_CAN_BE_SAVED = 'oex_plugin.openedx.core.djangoapps.user_authn.api.helper._field_can_be_saved'
    settings.OVERRIDE_ADD_ORG_TYPE_FIELD = 'oex_plugin.openedx.core.djangoapps.user_authn.api.form_fields.add_organization_type_field'
    settings.OVERRIDE_ADD_IS_ORG_REGISTERED_FIELD = 'oex_plugin.openedx.core.djangoapps.user_authn.api.form_fields.add_is_organization_registered_field'
    settings.OVERRIDE_ADD_ORG_SIZE_FIELD = 'oex_plugin.openedx.core.djangoapps.user_authn.api.form_fields.add_organization_size_field'
