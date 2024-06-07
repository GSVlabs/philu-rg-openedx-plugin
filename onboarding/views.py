"""
Views for on-boarding app.
"""
import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

from onboarding.helpers import get_close_matching_orgs_with_suggestions
from onboarding.models import Organization


@csrf_exempt
@login_required
def get_organizations(request):
    """
    Get organizations.
    
    Filtering organizations by specified request.
    """
    query = request.GET.get('query', '')
    final_result = get_close_matching_orgs_with_suggestions(request, query)

    return JsonResponse(final_result)


@login_required
@require_GET
@transaction.atomic
def organization(request):
    """
    View for providing recommendations on adding data to an existing org.
    """
    organization_id = request.GET.get('id', '')
    organization = get_object_or_404(Organization, id=organization_id)

    context = {
        'organization_id': organization.id,
        'organization_label': organization.label,
        'organization_type': organization.org_type,
        'organization_size': organization.total_employees,
        'is_organization_registered': organization.is_organization_registered,
    }

    return JsonResponse(context)


@login_required
@require_POST
@transaction.atomic
def save_organization(request):
    """
    The view to save organization survey from the user.
    """
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

    if org_name := data.get("organization"):
        organization_data = {
            "label": org_name,
            "is_organization_registered": data.get("is_organization_registered"),
            "org_type": data.get("organization_type"),
            "total_employees": data.get("organization_size"),
        }

        user_extended_profile = request.user.extended_profile
        if org_id := data.get("organization_id"):
            try:
                organization = Organization.objects.get(id=org_id, label__iexact=organization_data["label"])
                organization_data.pop("label")
                update_fields = {k: v for k, v in organization_data.items() if v is not None}
                for attr, value in update_fields.items():
                    setattr(organization, attr, value)
                organization.save(update_fields=update_fields.keys())
            except Organization.DoesNotExist:
                return JsonResponse({"error": "Invalid organization data"}, status=400)
        else:
            length_org_name = len(org_name)
            if (
                Organization.objects.filter(label__iexact=org_name).exists() or
                length_org_name > 255 or length_org_name < 1
            ):
                return JsonResponse({"error": "Invalid organization data"}, status=400)
            organization = Organization.objects.create(
                **{k: v for k, v in organization_data.items() if v is not None}
            )

        user_extended_profile.organization = organization
        user_extended_profile.save()

    return JsonResponse({'redirect_url': reverse('dashboard'), 'success': True}, status=200)
