import os
import openai
from langchain_openai import ChatOpenAI

def get_model():

  #openai 

  llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

  return llm

def set_model():

  #open ai api

