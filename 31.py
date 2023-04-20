#!/usr/bin/env python2.7
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


response = openai.Completion.create(
	model="gpt-3.5-turbo",
	message=[
		{"role":"user", "content":"hi"},
	]
)

print(response)
