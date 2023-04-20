#!/usr/bin/env python3

import openai
import os

# 设置OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 设置GPT-3模型和参数
model_engine = "text-davinci-003"
prompt = "如何使用python交互chatgpt, 请给出完整代码"
# 执行API请求
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2048,
    top_p=1,
    temperature=0.5,
    frequency_penalty=0,
    presence_penalty=0
)

# 获取响应并输出
message = response.choices[0].text
print(message)
