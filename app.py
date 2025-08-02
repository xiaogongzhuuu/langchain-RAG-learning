import streamlit as st
from qa_chain import smart_talk
from doc_processor import load_and_split_documents
from vector_store import build_vectorstore_from_chunks

st.set_page_config(page_title="rag文档回答助手", page_icon="📄")
st.title("智能文档问答助手")
st.markdown("上传你的文档或直接提问，系统将自动选择最合适的回答方式。")

vectorstore=None

uploaded_file =st.file_uploader("上传你的文档pdf",type=["pdf"])
if uploaded_file:
    st.warning("你已上传文件，但目前文档处理尚未开启")


question=st.text_input("请输入你的问题")

if question:
    st.write("正在思考中")
    answer=ask_question(question)
    st.success(answer)