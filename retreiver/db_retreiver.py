import numpy as np
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from retreiver import local_embedding
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.document import Document

def get_text_chunks_langchain(text):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    return docs


def get_db_data():
  openai_embed = OpenAIEmbeddings()

  code_db = Chroma(persist_directory="db/code", embedding_function=openai_embed)

  pyspark_retriever = code_db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
  )

  #pyspark_results = pyspark_retriever.get_relevant_documents(query)



  guidelines_db = Chroma(persist_directory="db/guidelines", embedding_function=openai_embed)
  all_guideline_docs = guidelines_db.as_retriever()
  #all_guideline_docs = all_guideline_docs.get_relevant_documents("get full document")

  logs_db = Chroma(persist_directory="db/logs", embedding_function=openai_embed)

  final_logs = logs_db.as_retriever()

  #final_logs = final_logs.get_relevant_documents(query)

  return pyspark_retriever , all_guideline_docs 

def get_logs_data(query):
  final_logs = local_embedding.get_logs(query)
  final_logs = get_text_chunks_langchain(final_logs)
  import chromadb.api

  chromadb.api.client.SharedSystemClient.clear_system_cache()
  db = Chroma.from_documents(final_logs, OpenAIEmbeddings())
  final_logs = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
    )

  return final_logs
