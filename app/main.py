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
import openai

'''
Inits
'''
""" 
#Genai inits
client = None
genai.init(client, api_key='APIKEY')
chat = None
genai.start_chat(chat, 'gemini-2.5-flash', client)
chat_history = None """

#openai inits
client = openai.OpenAI(api_key='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')
chat_history = []

#audio inits
engine = init()
r = Recognizer()

'''
Tkinter inits
'''

""" root = Tk()
root.geometry('50x300')
root.title('TitanAI - The world\'s most powerful AI assistant')
canvas = Canvas(root, width=300, height=50, bg='black')

root.mainloop() """

#to be continued...

""" while True:
    audio_processed = audio.speech_to_text(r)
    if audio_processed==None:
        continue
    else:
        response = openai_lib.continue_conversation(audio_processed, chat_history, "gpt-5-nano", client)
        audio.text_to_speech(response, engine) """
        

#communication stuff

chat_history = [{"role":"developer", "content":"You are an ai voice assisstant that is trained to give commands to navigate the user's screen for them. In the next prompt, yoou will receive the instructions for the format of the instructions you will output to the system."}
                {"role":"developer", "content":"In the start of the response, you will respond with 7 variables. If a variable is not required, then you will replace it with 'None'. The 7 variables are: Action - it tells the system what to do  out of the vague category of actions, out of: 'mouse_click' (single click left mouse button), 'mouse_move' (moves the mouse cursor to another position), 'mouse_other_click' (double click or click and drag), 'keyboard_action' (press a key, type text, or perform a keyboard shortcut) "}]