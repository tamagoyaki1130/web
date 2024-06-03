import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

from flask import Flask, session, render_template, request, redirect, url_for


#ChatGPT 사용 코드. -> AI(user_input)하면 답변 return 함. 
_=load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

system_message = """
    You are a psychological counselor. 
    You need to empathize with the emotions of the person you are talking to. 
    Also, make the person you are talking to talk more specifically about their situation and emotions. 
    Do not say that you are a robot.
"""
def AI(user_input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature = 1.0,
    max_tokens = 500,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]
    )
    return completion.choices[0].message.content