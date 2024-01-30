from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class PageType(models.Model):
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug


class InfoPage(models.Model):
    page = models.ForeignKey(
        PageType,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="info_pages"
    )
    site = models.ForeignKey(
        Site,
        default=settings.SITE_ID,
        related_name="info_pages",
        help_text=_(
            'The Site that this provider configuration belongs to.'
        ),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    text = HTMLField()

    class Meta:
        unique_together = ["page", "site"]

    def __str__(self):
        return f'{self.site_display_name()} - {self.page.slug}'

    def site_display_name(self):
        return self.site and self.site.name or None
