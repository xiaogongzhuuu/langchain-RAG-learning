import os
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
import openai
import streamlit as st
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")
openai.api_base=os.getenv("OPENAI_API_BASE")
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
#用gpt4回答无文档问题
def ask_question(user_question):
    try:
        response=openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role":"system","content":"你是一个善于回答问题的ai助手"},
                {"role":"user","content":user_question},
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "回答问题时出错"

#自动判断是否使用vector store的问答函数

def smart_talk(question, vectorstore=None):
    if vectorstore is None:
        print("未加载文档,使用gpt通识回答")
        return ask_question(question)
    
    docs = vectorstore.similarity_search(question,k=3)

    if not docs :
        print("文档未检索到相关问题,使用GPT通识回答")
        return ask_question(question)

    chain=load_qa_chain(llm,chain_type="stuff")
    return chain.run(input_documents=docs,question=question)
