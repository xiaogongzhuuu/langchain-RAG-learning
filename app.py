import streamlit as st
from qa_chain import smart_talk,ask_question
from vector_store import build_vectorstore_from_chunks
from doc_processor import process_markdown_doc,load_and_split_documents
import fitz
import os

st.set_page_config(page_title="rag文档回答助手", page_icon="📄")
st.title("智能文档问答助手")
st.markdown("上传你的文档或直接提问，系统将自动选择最合适的回答方式。")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

uploaded_file =st.file_uploader("上传你的文档pdf",type=["md"])

#if uploaded_file is not None:
#    temp_path = create_temp_file(uploaded_file.getvalue())  # 内存 → 磁盘
#   filepath = process_doc(temp_path)                         # 磁盘 → 处理
 #   delete_temp_file(temp_path) 
  #  chunks=process_markdown_doc(filepath)
   # vectorstore=build_vectorstore_from_chunks(chunks)


if uploaded_file is not None:
    temp_path = "temp.md"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getvalue())
        
    chunks=process_markdown_doc("temp.md")
    os.remove(temp_path)
    st.session_state.vectorstore=build_vectorstore_from_chunks(chunks)

question=st.text_input("请输入你的问题")

if question:
    st.write("正在思考中")
    try:
        answer=smart_talk(question,st.session_state.vectorstore)
        st.success("ai回答:")
        st.write(answer)
    except Exception as e:
        st.error("回答问题时出错")