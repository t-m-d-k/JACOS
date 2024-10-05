import argparse
from vector_store import transform
from utils import utilities
from retreiver import db_retreiver
from models import base_model

def run(mode):

  utilities.set_model()
  if mode.lower().strip() == "load":
    transform.run()
  if mode.lower().strip() == "retrieve":
    pyspark_results , all_guideline_docs = db_retreiver.get_db_data()
    final_logs = db_retreiver.get_logs_data("whats file size of sales_data.csv in script1.py ?")
    base_model.execute(pyspark_results , all_guideline_docs , final_logs,"whats file size of sales_data.csv in script1.py ?")

if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument('--mode', required=True)
  args = parser.parse_args()

  mode = args.mode
  run(mode)