# RAG 文档问答系统

基于 LangChain + OpenAI GPT-4 构建的智能文档问答应用，支持文档上传和智能检索问答。

## 🚀 在线体验

**[🎯 项目演示地址](https://huggingface.co/spaces/xiaogongzhuuu/rag)**

> 已部署到 Hugging Face Spaces，可直接在线体验完整功能

## 核心技术

- **RAG 架构**：检索增强生成，结合文档检索和 LLM 生成
- **向量检索**：FAISS 向量数据库 + OpenAI Embeddings
- **智能路由**：自动判断使用文档知识或通用知识回答
- **Web 界面**：Streamlit 构建用户交互界面

## 功能特性

- 📄 支持 Markdown/PDF 文档上传处理
- 🔍 基于语义相似性的智能文档检索
- 💬 RAG 增强回答 + 通用问答自动切换
- 🎯 简洁易用的 Web 交互界面

## 部署说明

**本地运行**：
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
echo "OPENAI_API_KEY=your_api_key" > .env
echo "OPENAI_API_BASE=your_api_base" >> .env  # 可选

# 3. 启动应用
streamlit run app.py
```

**在线体验**：
- 项目已部署至 [Hugging Face Spaces](https://huggingface.co/spaces/xiaogongzhuuu/rag)
- 支持实时文档上传和问答交互

## 项目架构

```
├── app.py              # Streamlit 主界面
├── modules/
│   ├── qa_chain.py         # 问答链逻辑
│   ├── doc_processor.py    # 文档处理与分块
│   └── vector_store.py     # 向量存储管理
└── temp/               # 临时文档目录
```

## 技术实现

**文档处理流程**：
1. 文档上传 → 文本提取 → 分块处理
2. 向量化嵌入 → FAISS 索引构建
3. 用户提问 → 相似性检索 → GPT-4 生成回答

**智能问答策略**：
- 有相关文档：使用 RAG 模式回答
- 无相关文档：切换到通用 GPT 问答

---

*项目展示了 RAG 技术在实际应用中的完整实现，涵盖文档处理、向量检索、智能问答等核心环节。*
