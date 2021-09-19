"""Translator module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('yopxMdteFYOjhmR78ImmpqgtMH9I3ySo95BzG-EJRAwg')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/77e9edfe-27bf-4362-a5a4-6c9e83087504')
def english_to_french(text1):
    """
    This funtion translates english to french
    """
    translation = language_translator.translate(
        text=text1,
        model_id='en-fr'
    ).get_result()
    frenchtranslation = translation.get("translation")[0].get("translation")
    return frenchtranslation

def french_to_english(text1):
    """
    This funtion translates french to english
    """
    translation = language_translator.translate(
        text=text1,
        model_id='fr-en'
    ).get_result()
    englishtranslation = translation.get("translation")[0].get("translation")
    return englishtranslation
