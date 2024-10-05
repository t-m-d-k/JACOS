import os
import openai
from langchain_openai import ChatOpenAI

def get_model():

  #set api key

  llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

  return llm

def set_model():

  #set api key

