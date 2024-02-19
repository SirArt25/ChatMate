from chatbot_app import ChatbotApp
from chatbot_business import ChatbotEngine
from env_manipulator import configure_environment
# we are trying to initialize  backend functions here

if __name__ == "__main__":
    configure_environment()
    engine = ChatbotEngine.create_engine()
    app = ChatbotApp(engine)
    app.show()



