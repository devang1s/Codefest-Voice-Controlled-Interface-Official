'''
main logic
'''

'''
Imports

pip statements

pip install google-genai
pip install pyttsx3
pip install pyaudio
pip install SpeechRecognition
pip install pyautogui
'''

from google.genai import * # type: ignore
from pyttsx3 import *# type: ignore
from pyaudio import *# type: ignore
from speech_recognition import *# type: ignore
from pyautogui import *# type: ignore
import libs.google_genai as genai
import libs.pyautogui_lib as PAG
import libs.audio_lib as audio
from tkinter import *

'''
Inits
'''

#Genai inits
client = None
genai.init(client, api_key=APIkey)
chat = None
genai.start_chat(chat, 'gemini-2.5-flash', client)
chat_history = None

#audio inits
engine = None
r = None
audio.init(engine, r)

'''
Tkinter inits
'''

""" root = Tk()
root.geometry('50x300')
root.title('TitanAI - The world\'s most powerful AI assistant')
canvas = Canvas(root, width=300, height=50, bg='black')

root.mainloop() """

#to be continued...

while True:
    audio_processed = audio.speech_to_text(r)
    if audio_processed==None:
        continue
    else:
        response = genai.complete_chat(audio_processed, chat_history, chat)
        audio.text_to_speech(response, engine)
        