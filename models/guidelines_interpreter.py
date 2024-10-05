from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI

def interpret(all_guideline_docs):


  prompt = ChatPromptTemplate.from_messages(
    [
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
        (
            "user",
            "Given the pyspark coding guideline try to understand it in better way , this will be used for code optimization ",
        ),
    ]
  )

  llm_model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
  guidelines_chain = create_history_aware_retriever(llm_model, all_guideline_docs, prompt)

  return guidelines_chain