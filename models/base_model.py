from models import code_interpreter
from models import guidelines_interpreter
from models import logs_interpreter
from utils import utilities
from langchain.chains import create_history_aware_retriever, create_retrieval_chain, SimpleSequentialChain, LLMChain
from langchain.chains.base import Chain
from langchain.retrievers.merger_retriever import MergerRetriever
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.retrievers import MergerRetriever



from langchain.chains.base import Chain
from langchain.chains import create_history_aware_retriever
from langchain.schema import Document



def execute(pyspark_results , all_guideline_docs , final_logs,question):

    lotr = MergerRetriever(retrievers=[pyspark_results, all_guideline_docs,final_logs])
    code_chain = code_interpreter.interpret(lotr)



    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the user's questions based on the below context:\n\n{context}",
                
            ),
            ("placeholder", "{chat_history}"),
            ("user", "{input}"),
        ]
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    document_chain = create_stuff_documents_chain(llm, prompt)

    qa = create_retrieval_chain(code_chain, document_chain)

    result = qa.invoke({"input": question})
    out = result["answer"].split("\n")
    print(out)

    return out
