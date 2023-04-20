#!/usr/bin/env python3

import os
import openai
import re
import readline


import openai
import re
import readline
import os

# 设置 API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 设置 OpenAI GPT 模型引擎
engine="text-davinci-003",

# 设置历史记录文件路径
history_path = os.path.expanduser("~/.openai_history")

# 加载历史记录
history = []
if os.path.exists(history_path):
    with open(history_path) as f:
        history = [line.strip() for line in f.readlines()]

# 获取机器人回复
def get_bot_reply(prompt):
    # 将历史记录和当前输入拼接为一个文本
    text = "\n".join(history + [prompt])
    # 调用 OpenAI API 获取回复
    response = openai.Completion.create(
        engine=engine,
        prompt=text,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # 从回复中提取机器人的文本
    bot_reply = response.choices[0].text.strip()
    # 从机器人回复中去掉历史记录部分，只保留最后一条回复
    bot_reply = re.sub(r".*You:.*\n", "", bot_reply).strip()
    # 返回机器人回复
    return bot_reply

# 显示对话
while True:
    # 获取用户输入
    user_input = input("You: ")
    # 将用户输入加入历史记录
    history.append(user_input)
    # 获取机器人回复
    bot_reply = get_bot_reply(user_input)
    # 将机器人回复加入历史记录
    history.append(bot_reply)
    # 将历史记录写入文件
    with open(history_path, "w") as f:
        f.write("\n".join(history))
    # 显示机器人回复
    print("Bot:", bot_reply)

