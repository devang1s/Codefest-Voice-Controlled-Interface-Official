'''
openai api lib
'''

'''
Imports

pip statements

pip install openai
'''

from openai import *

'''
inits
'''

def init(client, api_KY):
    client = OpenAI(api_key=api_KY)

'''
defs
'''

def generate_response(client, model, prompt):
    response = client.responses.create(model=model, input=prompt)
    return response.output_text

def continue_conversation(prompt, chat_history, model, client):
    chat_history = chat_history + [{"role":"user", "content":prompt}]
    response1 = client.chat.completions.create(model=model, messages=chat_history)
    response = response1.choices[0].message.content.strip()
    if response!=None:
        chat_history = chat_history + [{"role":"assistant", "content":response}]
        return response