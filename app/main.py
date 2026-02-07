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

# from google.genai import * # type: ignore
from pyttsx3 import *# type: ignore
from pyaudio import *# type: ignore
from speech_recognition import *# type: ignore
from pyautogui import *# type: ignore
# import libs.google_genai as genai
import libs.pyautogui_lib as PAG
import libs.audio_lib as audio
from tkinter import *
import libs.openai as openai_lib

'''
Inits
'''
""" 
#Genai inits
client = None
genai.init(client, api_key=APIkey)
chat = None
genai.start_chat(chat, 'gemini-2.5-flash', client)
chat_history = None """

#openai inits
client = NONE
openai_lib.init(client, "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")
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
        response = openai_lib.continue_conversation(audio_processed, chat_history, "gpt-5-nano", client)
        audio.text_to_speech(response, engine)
        