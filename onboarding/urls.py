"""
The urls for on-boarding app.
"""
from django.urls import re_path

from onboarding import views


urlpatterns = [
    re_path(r"^onboarding/get-organizations/$", views.get_organizations, name="get_organizations"),
    re_path(r"^onboarding/organization/$", views.organization, name="organization"),
    re_path(r"^onboarding/save-organization/$", views.save_organization, name="save_organization"),
]
