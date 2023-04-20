#!/usr/bin/env python3
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

# 输入文本
text = "请问你会哪些编程语言？"

# 选择使用的ChatGPT模型
model = "text-davinci-002"

# 生成的回复文本长度
length = 50

# 控制生成文本的随机程度
temperature = 0.7

# 控制生成文本的多样性和可预测性
top_p = 0.9

# 生成多个回复文本的数量
n = 3

# 设置生成文本的终止条件
stop_sequence = "。"

# 控制ChatGPT模型生成回复时考虑的历史文本长度
max_history = 2

# 在生成回复时考虑的个人资料或上下文信息
persona = {
    "name": "小明",
    "age": 25,
    "occupation": "程序员",
    "interests": ["编程", "音乐", "读书"],
    "location": "北京"
}

# 控制生成回复的情感倾向
emotion = {
    "type": "joy",
    "strength": 0.8,
    "happy": 0.9,
    "sad": 0.1,
    "angry": 0,
    "fearful": 0,
    "disgusted": 0,
    "surprised": 0
}

# 控制生成回复时所依据的知识库或知识图谱
knowledge = {
    "entities": [
        {"type": "programming language", "name": "Python"},
        {"type": "programming language", "name": "Java"},
        {"type": "framework", "name": "Django"},
        {"type": "framework", "name": "Spring"},
        {"type": "database", "name": "MySQL"}
    ],
    "topics": [
        {"name": "Python 编程基础", "score": 0.8},
        {"name": "Java 编程基础", "score": 0.7},
        {"name": "Django Web 开发", "score": 0.6},
        {"name": "Spring Boot 开发", "score": 0.5},
        {"name": "MySQL 数据库管理", "score": 0.4}
    ]
}

# 调用OpenAI API生成回复
response = openai.Completion.create(
    engine=model,
    prompt=text,
    temperature=temperature,
    max_tokens=length,
    top_p=top_p,
    n=n,
    stop=stop_sequence,
    context=persona,
    max_history=max_history,
    knowledge_graph=knowledge,
    emotion=emotion
)

# 输出生成的回复文本
for i in range(n):
    print("回复" + str(i+1) + ": " + response.choices[i].text.strip())

