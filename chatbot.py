# Python module for running an Ollama chatbot locally on my 3070.
# This module could be replaced with an existing purchased API such as with ChatGPT.
from config import config

import os
os.environ['OLLAMA_MODELS'] = config['CHATBOT']["cache"]

import ollama

def talk(messages):
  response = ollama.chat(model='llama3', messages=messages)
  return response['message']['content']
