from vector_store import pyspark_loader
from vector_store import guidelines_loader
from vector_store import sparklogs_loader

from vector_store import db_persist

def run():

  pyspark_document = pyspark_loader.load()
  guidelines_document = guidelines_loader.load()
  logs_document = sparklogs_loader.load()


  db_persist.persist("code", pyspark_document)
  db_persist.persist("guidelines", guidelines_document)
  db_persist.persist("logs",logs_document)

