import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")
openai.api_base=os.getenv("OPENAI_API_BASE")

def ask_question(user_question):
    response=openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"你是一个善于回答问题的ai助手"},
            {"role":"user","content":user_question},
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()
