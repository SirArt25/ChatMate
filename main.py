import env_manipulator
from vectordb import MiniDB
from loader import  Loader
from chatbot_business import Chatbot

if __name__ == "__main__":
    env_manipulator.configure_environment()
    chatbot = Chatbot()
    print(chatbot.ask("Please tell me about git bisect"))




