'''
Lib for google_genai/google-genai

'''

'''
Imports

Pip statements

pip install google-generativeai
'''

import google.generativeai as genai

'''
Inits
'''

def init(client):
    client = genai.Client()
    return client

'''
Defs
'''

def generate_response(prompt, Client, Model):
    response = Client.models.generate_content(model=Model, contents=prompt)

def start_chat(ChatName, Model, Client):
    ChatName = Client.chats.create(model=Model)

def complete_chat(prompt, chat_history, chatVar):
    response = chatVar.send_message(prompt)
    return response.text