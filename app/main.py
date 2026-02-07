'''
main logic
'''

'''
Imports

pip statements

pip install google-generativeai
pip install pyttsx3
pip install pyaudio
pip install SpeechRecognition
pip install pyautogui
'''

from google.generativeai import * # type: ignore
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
genai.init(client)

#audio inits
engine = None
r = None
audio.init(engine, r)

'''
Tkinter inits
'''

root = Tk()
root.geometry('50x300')
root.title('TitanAI - The world\'s most powerful AI assistant')


root.mainloop()