# translator
translation program using IBM Watson's API

These programs (three contained in this repository--text2text_translator.py, speech2text_translator.py and speech2speech_translaor.py) 
have similar but different functions.

text2text_translator.py will ask for user input (a simple string) and then ask what language the user would like to translate the text to.
The user is given a choice between 5 languages (Spanish, German, French, Italian, and Russian. It will then output the translated text on the screen.

speech2text_translator.py will take an audio file (hard coded into the code. An example file--audio.flac--has been included here for demonstration purposes.
However any audio file with a clear voice will work, as long as the audio file is in the same directory as the .py file and the 'audio.flac' gets changed 
in the code itself, as well as the file-type, which is currently set to 'audio/flac'. These potential changes are noted within the file itself with user comments) 
and ask the user what language to translate to--again, 5 choices of Spanish, German, French, Italian, and Russian are given, and the program outputs the desired
translation from the audio file as text on the screen.

speech2speech_translator.py will take an audio file (hard coded into the code. An example file--audio.flac--has been included here for demonstration purposes.
However any audio file with a clear voice will work, as long as the audio file is in the same directory as the .py file and the 'audio.flac' gets changed 
in the code itself, as well as the file-type, which is currently set to 'audio/flac'. These potential changes are noted within the file itself with user comments),
play the file using your computer's media player, translate the audio into German text (although, as is noted in the code, you can change the desired output language,
German is just hard-coded in because I speak German!), then synthesize an A.I. voice and create an audio file ('s2s_output.wav') and save it to the local directory.
The program then plays the translated audio file using your computer's media player.
