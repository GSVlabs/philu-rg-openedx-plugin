"""
Production settings variables required by the RG OeX Plugin.
"""
from subprocess import CalledProcessError, check_output

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration


def plugin_settings(settings):

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

    settings.INACTIVE_USER_URL = f'http{"s" if settings.HTTPS == "on" else ""}://{settings.CMS_BASE}'
