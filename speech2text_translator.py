# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:58:51 2021

@author: Michael Crofts
"""
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

#S2T API Key and URL
s2t_apikey="TJPzbKvz_MoWzlkeEg4CNIkP-dJXpSl_1T4-AaNJYcsH"
s2t_url="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/141bfe0a-375f-45ef-b660-76ff0fa8f693"

#Translator API Key and URL
t2t_apikey='2O-RcHCLZmLcHR8tvr_GqxQbbaIySxJZh_-blCoiTaJj'
t2t_url='https://api.us-south.language-translator.watson.cloud.ibm.com'

authenticator=IAMAuthenticator(s2t_apikey)
speech_to_text=SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url(s2t_url)

print("\n\nMike Crofts' Speech-to-Speech Translator\n")

with open(join(dirname(__file__), 'audio-file.flac'), #Replace 'audio-file.flac' with desired audio to translate (within the same directory)
          'rb') as audio_file: 
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/flac', #Change audio type if audio is type other than flac (ex: audio/wav)
        word_alternatives_threshold=0.9,
        keywords=['test','this','audio'],
        keywords_threshold=0.5
    ).get_result()

res=speech_recognition_results['results']
res=str(res)
result=list(res.split("'"))
print("\nInput Detected: ",result[7], "\n")

#IBM Watson authenticator
authenticator = IAMAuthenticator(t2t_apikey)
language_translator=LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
    )
language_translator.set_service_url(t2t_url)

#Identify user language input
user_language=(language_translator.identify(result[7]).get_result())
for language in user_language['languages']:
    l=user_language['languages']

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
user_language=input("Please select a language to translate to: ").lower()
if user_language == 'spanish':
    t = language_translator.translate(text=result[7],model_id='en-es').get_result()
elif user_language == 'german':
    t = language_translator.translate(text=result[7],model_id='en-de').get_result()
elif user_language == 'french':
    t = language_translator.translate(text=result[7],model_id='en-fr').get_result()
elif user_language == 'italian':
    t = language_translator.translate(text=result[7],model_id='en-it').get_result()
elif user_language == 'russian':
    t = language_translator.translate(text=result[7],model_id='en-ru').get_result()

translation_output=str(t)
tr=list(translation_output.split("'"))
print("\nTranslation: ",tr[5])
