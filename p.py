#!/usr/bin/env python3
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:"

engine_name = "text-davinci-003"
temperature = 0.7
max_tokens = 2048
top_p = 1
frequency_penalty = 0
presence_penalty = 0.6
stop = [" Human:", " AI:"]

while True:
    user_input = input("Human: ")
    if user_input.strip() == "":
        continue
    prompt += f"\nHuman: {user_input}\nAI:"
    response = openai.Completion.create(
        engine=engine_name,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
    )
    message = response.choices[0].text.strip()
    prompt += message + "\nHuman:"
    print("AI:", message)
    with open("conversation.txt", "w") as f:
        f.write(prompt)
