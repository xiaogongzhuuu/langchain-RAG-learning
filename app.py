import streamlit as st
from qa_chain import ask_question

st.title("智能文档问答助手")

uploaded_file =st.file_uploader("上传你的文档pdf",type=["pdf"])
if uploaded_file:
    st.warning("你已上传文件，但目前文档处理尚未开启")


question=st.text_input("请输入你的问题")

if question:
    st.write("正在思考中")
    answer=ask_question(question)
    st.success(answer)