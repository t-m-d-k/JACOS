from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def persist(mode, document):

  openai_embed = OpenAIEmbeddings()

  if mode == "code":

    PERSIST_DIRECTORY = "db/code"
    chroma_db = Chroma.from_documents(documents=document, embedding=openai_embed, persist_directory=PERSIST_DIRECTORY)
    chroma_db.persist()
  elif mode == "guidelines":

    PERSIST_DIRECTORY = "db/guidelines"
    chroma_db = Chroma.from_documents(documents=document, embedding=openai_embed, persist_directory=PERSIST_DIRECTORY)
    chroma_db.persist()

