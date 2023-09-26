from cms.urls import urlpatterns as patterns
from django.urls import re_path

from oex_plugin.openedx.core.djangoapps.common_views.branding import FaviconRedirectView

# Add our URL path at the beggining so we'll use our view instead of the original one
patterns.insert(0, re_path(r'^favicon\.ico$', FaviconRedirectView.as_view()))

urlpatterns = [
    # add the plugin URLs here
]
