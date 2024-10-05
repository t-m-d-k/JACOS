import os
from langchain_community.document_loaders import TextLoader


def load():
    documents = []
    folder_path = "/home/ec2-user/environment/talk_to_code/resources/spark-logs/"
    # Traverse through each file in the folder
    for filename in os.listdir(folder_path):
        # Only process .txt files
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            # Use LangChain's TextLoader to load the document
            loader = TextLoader(file_path)
            document = loader.load()
            
            # Append loaded document to the documents list
            documents.extend(document)
    
    return documents