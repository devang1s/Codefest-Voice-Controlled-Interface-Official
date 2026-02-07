'''
Lib for audio functions
'''

'''
Imports

pip install statements

pip install pyttsx3
pip install pyaudio
pip install SpeechRecognition 
'''

from pyttsx3 import *
from pyaudio import *
import speech_recognition as sr

'''
Inits
'''

engine = init()
r = sr.Recognizer()

'''
Defs
'''

#Speech to text

def speech_to_text():

    #Initialise mic and capture audio

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Speak now...")
        audio = r.listen(source)

    #Process audio

    try:
        text = r.recognize_google(audio)
        output = text
    except sr.UnknownValueError:
        output = "Audio error - could not understand audio"
    except sr.RequestError as e:
        output = f"System error. Error type: API error: {e}"

    #Return output

    return output

#Text to speech

def text_to_speech(InputText, EngineVar):

    #Process text to speech
    EngineVar.say(InputText)

    #Speak the text
    EngineVar.runAndWait()