#!/bin/sh

curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "如何用人工智能调用一个程序的api"}]  }'
