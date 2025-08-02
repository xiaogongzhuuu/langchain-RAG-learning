from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key=os.getenv("OPENAI_API_KEY")
openai_api_base=os.getenv("OPENAI_API_BASE")

os.environ["OPENAI_API_KEY"]=openai_api_key
os.environ["OPENAI_API_BASE"]=openai_api_base

#载入模型
embedding_model=OpenAIEmbeddings()

def build_vectorstore_from_chunks(chunks):
    vectorstore = FAISS.from_texts(chunks,embedding_model)
    return vectorstore