import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

openai_api_key=os.getenv("OPENAI_API_KEY")
openai_api_base=os.getenv("OPENAI_API_BASE")

os.environ["OPENAI_API_KEY"]=openai_api_key
os.environ["OPENAI_API_BASE"]=openai_api_base

#载入模型
embedding_model=OpenAIEmbeddings()

#文档加载
def load_and_split_documents(filepath):
    if not filepath.endswith((".md",".txt")):
        print("当前只支持markdown或者txt文本文件")
        return[]
    
    with open(filepath,"r",encoding="utf-8") as f:
        text=f.read()
#拆分成段落
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = splitter.split_text(text)
    print(f"文件拆分完成，共{len(chunks)}段")
    return chunks
#文档向量化处理(利用上述load and split documents函数)
def process_markdown_doc(filepath):
    chunks=load_and_split_documents(filepath)
    if not chunks:
        return []
    print("嵌入向量生成完成")
    return chunks