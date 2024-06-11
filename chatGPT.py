import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

class AI:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.client = OpenAI(
            api_key=os.environ.get('OPENAI_API_KEY'),
        )
        self.system_message = """
            You are a psychological counselor. 
            You need to empathize with the emotions of the person you are talking to. 
            Also, make the person you are talking to talk more specifically about their situation and emotions. 
            Do not say that you are a robot.
            Ask only 1 question at a time.
        """

    def get_response(self, user_input):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=1.0,
            max_tokens=500,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": user_input}
            ]
        )
        return completion.choices[0].message.content


if __name__ == "__main__":
    ai_instance = AI()
    while True:
        user_input = input('User:')
        if user_input.lower() in {'exit', 'quit'}:
            break
        print(ai_instance.get_response(user_input))

