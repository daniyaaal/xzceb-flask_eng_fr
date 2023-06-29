""" This file is for translating english and french """

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """ This function is for translating english to french """

    text = english_text
    french_text = MyMemoryTranslator(source='en-GB', target='french').translate(text)
    return french_text


def french_to_english(french_text):
    """ This function is for translating french to english """

    text = french_text
    english_text = MyMemoryTranslator(source='french', target='english').translate(text)
    return english_text

