from common.djangoapps.edxmako.shortcuts import render_to_response
from django.contrib.sites.models import Site
from edx_info_pages.models import InfoPage


def info_page_render(original_render, request, template):
    current_site = Site.objects.get_current(request)
    page_name = template.split('.')[0]

    page = InfoPage.objects.filter(
        page__slug=page_name,
        site=current_site
    ).first()

    if page:
        return render_to_response('edx_info_pages/infopage.html', {'page': page})

    return original_render(request, template)
