#streamlit run app.py
import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")
openai.api_base=os.getenv("OPENAI_API_BASE")

st.title("第一性原理对话助手")
with st.expander("📘 使用指南（点我展开）", expanded=False):
    st.markdown("""
### 🎯 功能简介
这是一个帮助你用 **第一性原理** 重新思考问题的聊天机器人。

每当你输入一个问题、想法或困惑，它会：

- 揭示你潜在的假设
- 引导你回到事实和底层逻辑
- 用提问推动你从本质重新思考

### ✅ 使用方式
1. 在下方输入你正在思考的问题或计划  
2. 尽量具体，比如：“我想转专业，但很害怕失败”
3. 机器人不会直接给建议，而是用问题反问你，让你看清底层逻辑
4. 每一次回答，都是为了帮助你突破“惯性思维”

### 🧠 什么是第一性原理？
第一性原理是物理学中常见的一种分析方法，意思是：
> **不依赖他人观点、社会共识，从最基本事实出发重新建构理解**

---
""")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("你最近在思考什么问题")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 👇 生成 Prompt
    prompt = f"""
你是一个“第一性原理认知助手”。

用户说了：{user_input}

请按如下方式回应：
1. 揭示其隐藏假设；
2. 提出本质性反问，引导用户重新拆解；
3. 简洁、深刻，最好用提问的方式，引导而非给建议；
4. 回复不超过150字。
"""

    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "你是一个擅长第一性原理提问的认知教练。"},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response.choices[0].message["content"]
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})