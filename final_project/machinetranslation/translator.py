import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version ='2018-05-01',
 authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(ENGLISH):
    """ This translate english to french """
    frenchtranslation = language_translator.translate(text = ENGLISH,
     model_id = 'en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(FRENCH):
    """ This translate french to english """
    englishtranslation = language_translator.translate(text = FRENCH,
     model_id = 'fr-en').get_result()
    return englishtranslation.get("translations")[0].get("translation")

