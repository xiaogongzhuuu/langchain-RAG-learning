# 📚 LangChain RAG 学习项目

基于 LangChain 和 RAG 技术的文档问答系统，个人学习 AI 应用开发的实践项目。

## ✨ 核心功能

- 📄 **文档上传**：支持 Markdown/PDF 文档处理
- 🔍 **智能检索**：基于向量相似性的文档检索
- 💬 **问答系统**：RAG 增强回答 + 通用问答自动切换
- 🎯 **Web 界面**：Streamlit 可视化交互界面

## 🛠️ 技术栈

- **LangChain** + **OpenAI GPT-4** + **FAISS 向量数据库**
- **Streamlit Web 框架** + **Python**

## 🚀 快速启动

```bash
# 安装依赖
pip install -r requirements.txt

# 配置 API 密钥
echo "OPENAI_API_KEY=your_key" > .env

# 启动应用
streamlit run app.py
```

## 📁 项目结构

```
├── app.py              # 主应用界面
├── qa_chain.py         # 问答逻辑
├── doc_processor.py    # 文档处理
├── vector_store.py     # 向量存储
└── md/                 # 测试文档
```

## 🎯 技术要点

- **文档处理**：文本分块 + 向量化嵌入
- **检索增强**：相似性搜索 + GPT 生成
- **智能路由**：基于检索结果自动选择回答策略

---

💡 **学习成果**：掌握了 RAG 技术原理，熟悉 LangChain 框架应用，具备 AI 应用开发能力。