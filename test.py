
import os
from openai import OpenAI

print("环境变量检测：")
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY")[:10] + "..." if os.getenv("OPENAI_API_KEY") else "未设置")
print("OPENAI_BASE_URL:", os.getenv("OPENAI_BASE_URL"))
print("OPENAI_API_BASE:", os.getenv("OPENAI_API_BASE"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com"),
)

try:
    print("\n正在测试连接 OpenAI API...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个测试助手"},
            {"role": "user", "content": "请告诉我，你现在是通过哪个 API base_url 工作的？"}
        ]
    )
    print("\nAPI 返回结果：", response.choices[0].message.content)
except Exception as e:
    print("\n❌ 出错了：", e)
