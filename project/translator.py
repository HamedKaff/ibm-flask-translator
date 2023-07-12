import os
from deep_translator import MyMemoryTranslator


def english_to_french_translate(text):

    translated = MyMemoryTranslator(source='english',
                                    target='french').translate(text)
    return translated


def french_to_english_translate(text):

    translated = MyMemoryTranslator(source='french',
                                    target='english').translate(text)
    return translated
