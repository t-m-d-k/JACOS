from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import Language


def load():
  code_path = "/home/ec2-user/environment/talk_to_code/resources/gitlab-code"


  loader = GenericLoader.from_filesystem(
      code_path,
      glob="**/*",
      suffixes=[".py"],  # Look for Python files
      exclude=["**/non-utf8-encoding.py"],  # Exclude specific files
      parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
  )

  documents = loader.load()
  python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
  )
  texts = python_splitter.split_documents(documents)
  return texts