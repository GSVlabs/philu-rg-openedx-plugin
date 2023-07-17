"""
Production settings variables required by the RG OeX Plugin.
"""
from django.conf import settings


AUTH_TOKENS = getattr(settings, 'AUTH_TOKENS', {})

if AUTH_TOKENS.get('RG_SENTRY_DSN', None):
    import sentry_sdk
    import subprocess
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.celery import CeleryIntegration

    try:
        platform_git_commit = subprocess.check_output(['git', 'describe', '--always']).strip()
    except (subprocess.CalledProcessError, OSError):
        platform_git_commit = ''
    sentry_sdk.init(
            AUTH_TOKENS.get('RG_SENTRY_DSN'),
            auto_enabling_integrations=False,
            integrations=[DjangoIntegration(), CeleryIntegration()],
            environment=settings.ENV_TOKENS.get('RG_SENTRY_ENVIRONMENT', ''),
            release=platform_git_commit,
            send_default_pii=True
            )

INACTIVE_USER_URL = f'http{"s" if settings.HTTPS == "on" else ""}://{settings.CMS_BASE}'
