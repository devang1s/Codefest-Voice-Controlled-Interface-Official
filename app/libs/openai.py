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

def init(client):
    client = OpenAI()

'''
defs
'''

def generate_response(client, model, prompt):
    response = client.responses.create(model=model, prompt=prompt)
    return response.output_text

client = None
init(client)
print(generate_response(client, 'gpt-5-nano', 'Hi.'))