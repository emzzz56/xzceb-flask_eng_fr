"""Translate text From English to French and vise versa"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translate Text From English to French"""
    if english_text is None:
        french_text = None
    elif english_text == '':
        french_text = ''
    else:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text = french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate Text From French to English"""
    if french_text is None:
        english_text = None
    elif french_text == '':
        english_text = ''
    else:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = english_text['translations'][0]['translation']
    return english_text
