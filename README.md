# LangChain RAG 学习项目

一个简单的文档问答系统，学习LangChain和RAG技术的入门项目。

## 功能

- 上传文档进行智能问答
- 支持普通问题回答
- 基于OpenAI GPT模型

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置API密钥
创建 `.env` 文件：
```env
OPENAI_API_KEY=你的OpenAI密钥
```

### 3. 运行程序
```bash
streamlit run app.py
```

## 项目文件

- `app.py` - 网页界面
- `qa_chain.py` - 问答功能
- `doc_processor.py` - 文档处理
- `vector_store.py` - 向量存储
- `docs/` - 示例文档

## 使用方法

1. 打开网页 http://localhost:8501
2. 输入问题
3. 查看AI回答

## 测试

运行测试文件：
```bash
python test_processor.py
```

## 注意事项

- 需要有效的OpenAI API密钥
- 目前支持 .md 和 .txt 文件
- 适合学习和实验使用

## 学习资源

- [LangChain文档](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs)

---

这是一个学习项目，欢迎提问和交流！