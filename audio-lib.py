'''
lib for audio functions
'''

'''
imports

pip install statements

pip install pyttsx3
pip install pyaudio
pip install SpeechRecognition 
'''

from pyttsx3 import *
from pyaudio import *
import speech_recognition as sr

#inits

engine = init()
r = sr.Recognizer()

#functions

def speech_to_text():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        output = text
    except sr.UnknownValueError:
        output = "Audio error - could not understand audio"
    except sr.RequestError as e:
        output = f"System error. API error: {e}"

    return output

print(speech_to_text())