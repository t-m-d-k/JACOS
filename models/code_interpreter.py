from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def interpret(pyspark_results):

  prompt = ChatPromptTemplate.from_messages(
    [
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
        (
            "user",
            "Given the pyspark code understand the file name and  logic written over here ",
        ),
    ]
  )

  llm_model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
  retriever_chain = create_history_aware_retriever(llm_model, pyspark_results, prompt)

  return retriever_chain

