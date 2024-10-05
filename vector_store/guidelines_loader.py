from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import CharacterTextSplitter


def load():
  loader = Docx2txtLoader("/home/ec2-user/environment/talk_to_code/resources/guidelines/coding_guidelines.docx")

  data = loader.load()

  return  data