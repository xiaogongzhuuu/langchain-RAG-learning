import streamlit as st
from qa_chain import smart_talk
from vector_store import build_vectorstore_from_chunks
from doc_processor import process_markdown_doc
import os
import time
st.set_page_config(page_title="rag文档回答助手", page_icon="📄")
st.title("智能文档问答助手")
st.markdown("上传你的文档或直接提问，系统将自动选择最合适的回答方式。")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "uploaded" not in st.session_state:
    st.session_state.uploaded = None

uploaded_file =st.file_uploader("上传你的文档",type=["md","pdf"])

if uploaded_file is not None and uploaded_file.name != st.session_state.get("last_uploaded_filename"):

    ext = os.path.splitext(uploaded_file.name)[1]
    temp_path = f"temp{ext}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    with st.spinner("正在读取文档并构建知识库..."):   
        chunks=process_markdown_doc(temp_path)
        os.remove(temp_path)
        st.session_state.vectorstore=build_vectorstore_from_chunks(chunks)
    status = st.success("文档上传成功")
    time.sleep(1.5)
    status.empty()
    st.session_state.uploaded = True 
    st.session_state["last_uploaded_filename"] = uploaded_file.name


question=st.text_input("请输入你的问题")

if question:
    answer_placeholder = st.empty()
    with st.spinner("正在思考中"):
        try:
            answer=smart_talk(question,st.session_state.vectorstore)
            st.success("ai回答:")
            st.write(answer)
        except Exception as e:
            st.error(f"出错了：{e}")