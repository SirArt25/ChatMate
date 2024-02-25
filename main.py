from chatbot_dir.chatbot_app import ChatbotApp
from chatbot_dir.chatbot_business import ChatbotEngine
from utilities.env_manipulator import configure_environment
# we are trying to initialize  backend functions here

if __name__ == "__main__":
    configure_environment()
    engine = ChatbotEngine.create_engine()
   # engine2 = ChatbotEngine()
    app = ChatbotApp(engine)
    app.show()