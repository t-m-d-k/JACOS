from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI

def interpret(final_logs):


  prompt = ChatPromptTemplate.from_messages(
    [
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
        (
            "user",
            "Given the pyspark logs understand the content on file name and its size",
        ),
    ]
  )

  llm_model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
  logs_chain = create_history_aware_retriever(llm_model, final_logs, prompt)

  return logs_chain