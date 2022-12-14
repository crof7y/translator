# -*- coding: utf-8 -*-
"""

Created on Sun Jun 20 10:42:19 2021

@author: Michael Crofts

"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#IBM Watson API
api_key='2O-RcHCLZmLcHR8tvr_GqxQbbaIySxJZh_-blCoiTaJj'
api_url='https://api.us-south.language-translator.watson.cloud.ibm.com'

print("\nWelcome to the IBM Watson Translator!")

#Get user input to translate
user_text=input("Enter text to translate: ")

#IBM Watson authenticator
authenticator = IAMAuthenticator(api_key)
language_translator=LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
    )
language_translator.set_service_url(api_url)

#Identify user language input
user_language=(language_translator.identify(user_text).get_result())
for language in user_language['languages']:
    l=user_language['languages']
print(json.dumps(l[0],indent=2),'\n')

lang=l[0]['language']
if lang == "en":
    print("Langauge Detected: English\n")
elif lang == "es":
    print("Language Detected: Spanish\n")
elif lang == "de":
    print("Language Detected: German\n")
elif lang == "fr":
    print("Language Detected: French\n")
elif lang == "it":
    print("Language Detected: Italian\n")
elif lang == "ru":
    print("Language Detected: Russian\n")

#User input to translate to desired language
print("Available Languages:\n1. Spanish\n2. German\n3. French\n4. Italian\n5. Russian")
user_language=input("Please select a language to translate to (please type full language name): ").lower()
if user_language == 'spanish':
    t = language_translator.translate(text=user_text,model_id='en-es').get_result()
elif user_language == 'german':
    t = language_translator.translate(text=user_text,model_id='en-de').get_result()
elif user_language == 'french':
    t = language_translator.translate(text=user_text,model_id='en-fr').get_result()
elif user_language == 'italian':
    t = language_translator.translate(text=user_text,model_id='en-it').get_result()
elif user_language == 'russian':
    t = language_translator.translate(text=user_text,model_id='en-ru').get_result()

result=t['translations']

print('\n',result)
