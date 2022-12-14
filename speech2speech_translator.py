# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 21:58:51 2021

@author: Michael Crofts
"""

from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
import os
import time

#S2T API Key and URL
s2t_apikey="TJPzbKvz_MoWzlkeEg4CNIkP-dJXpSl_1T4-AaNJYcsH"
s2t_url="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/141bfe0a-375f-45ef-b660-76ff0fa8f693"

#Translator API Key and URL
t2t_apikey='2O-RcHCLZmLcHR8tvr_GqxQbbaIySxJZh_-blCoiTaJj'
t2t_url='https://api.us-south.language-translator.watson.cloud.ibm.com'

#T2S API Key and URL
t2s_apikey='YeVN88F--qH6zCEPBUVxcvompTd1qzAMp7ZHKE0VsdWt'
t2s_url='https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/b2895eef-4fba-44d0-a7fd-528292f57429'

authenticator1=IAMAuthenticator(s2t_apikey)
speech_to_text=SpeechToTextV1(
    authenticator=authenticator1
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
reslt=list(res.split("'"))
result=reslt[7]
print("\nInput Detected: ",result, "\n")
print("\nPlaying Audio Input...\n")
os.system("start audio-file.flac")
time.sleep(3)

#IBM Watson authenticator
authenticator2 = IAMAuthenticator(t2t_apikey)
language_translator=LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator2
    )
language_translator.set_service_url(t2t_url)

#Identify language input
user_language=(language_translator.identify(result).get_result())
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

print("Translating to German...\n")

t = language_translator.translate(text=result,model_id='en-de').get_result()

translation_output=str(t)
tra=list(translation_output.split("'"))
tr=tra[5]
print("Translation: ",tr)

from ibm_watson import TextToSpeechV1

authenticator3=IAMAuthenticator(t2s_apikey)
text_to_speech=TextToSpeechV1(
    authenticator=authenticator3
)

text_to_speech.set_service_url(t2s_url)

with open('s2s_output.wav','wb') as audio_file:
    tts=text_to_speech.synthesize(tr,
                                  accept='audio/wav',
                                  voice='de-DE_ErikaV3Voice').get_result()
    audio_file.write(tts.content)

os.system("start s2s_output.wav")
