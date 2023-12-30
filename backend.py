import os
import openai


class Chatbot:
    def __init__(self):
        api_key = os.getenv("CHATGPT_API_KEY")
        openai.api_key = api_key

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
