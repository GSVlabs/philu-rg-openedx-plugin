from modeltranslation.translator import translator, TranslationOptions
from .models import InfoPage


class InfoPageTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(InfoPage, InfoPageTranslationOptions)
