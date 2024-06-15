from chatbot_dir.chatbot_app import ChatbotApp
from chatbot_dir.chatbot_business import ChatbotEngine
from utilities.env_manipulator import configure_environment
from path_configurator import ROOT_DIR 
# we are trying to initialize  backend functions here

if __name__ == "__main__":
    configure_environment()
    engine = ChatbotEngine.create_engine(3, 3)
    app = ChatbotApp(engine)
    app.show()
