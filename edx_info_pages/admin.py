from .models import InfoPage, PageType
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


class InfoPageAdmin(TranslationAdmin):

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                'modeltranslation/css/tabbed_translation_fields.css',
            ),
        }


class PageTypeAdmin(admin.ModelAdmin):
    list_display = ('slug',)

admin.site.register(InfoPage, InfoPageAdmin)
admin.site.register(PageType, PageTypeAdmin)
