import openai
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_community.document_loaders import TextLoader

def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )

    return response.data[0].embedding
def get_local_response(question, local_data, local_embeddings):
    question_embedding = np.array(get_embedding(question)).reshape(1, -1)
    cosine_similarities = cosine_similarity(question_embedding, local_embeddings).flatten()
    most_similar_index = cosine_similarities.argmax()
    return local_data[most_similar_index]

def generate_local_embeddings(local_data):
    return np.array([get_embedding(text) for text in local_data])

def get_combined_response(question, local_data, local_embeddings):
    local_response = get_local_response(question, local_data, local_embeddings)
    
    
    
    return local_response

def load_local_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def get_logs(question):
  
  local_data = load_local_data('/home/ec2-user/environment/talk_to_code/resources/spark-logs/logs.txt')

  local_embeddings = generate_local_embeddings(local_data)
  response = get_combined_response(question, local_data, local_embeddings)
  return response