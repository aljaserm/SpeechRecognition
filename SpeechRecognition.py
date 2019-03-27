# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:23:52 2019

@author: aljaser

### Speech Recognition System ###

Need active Internet connection
pip install SpeechRecognition
pip install PyAudio
"""

import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hey there !! Say Something !!!")
    audio = r.listen(source)
    
try:
    print("Google thinks you said:\n" + r.recognize_google(audio))
     
except:
    pass