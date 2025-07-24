# LangChain RAG 学习笔记

个人学习LangChain和RAG技术的实践项目。

## 环境配置

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 创建 `.env` 文件，添加API密钥：
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 使用方法

运行Jupyter Notebook：
```bash
jupyter notebook
```

打开 `langchain.ipynb` 开始学习。

## 项目内容

- 基础LangChain使用
- 提示词模板设计
- 聊天机器人实现
- RAG技术实践

## 依赖包

主要使用的库：
- `langchain` - LLM应用框架
- `langchain-openai` - OpenAI集成
- `chromadb` - 向量数据库
- `python-dotenv` - 环境变量管理