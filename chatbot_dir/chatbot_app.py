import streamlit as st
from chatbot_dir.chatbot_business import ChatbotEngine

class ChatbotApp:
    __instance = None
    __member_called = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, engine: ChatbotEngine):
        self.__engine = engine

    def show(self):
        # Streamlit UI
        st.title("Chatbot")
        st.markdown("---")

        # Custom CSS styles
        st.markdown(
            """
            <style>
            /* Container for chat messages */
            .chat-container {
                max-width: 800px;
                margin-bottom: 20px;
                padding: 10px;
                border-radius: 10px;
                background-color: #f0f0f0;
            }
            /* User message style */
            .user-msg {
                background-color: #00b894;
                color: white;
                border-radius: 5px;
                padding: 10px;
                margin-bottom: 10px;
                align-self: flex-end;
            }
            /* Bot message style */
            .bot-msg {
                background-color: #0984e3;
                color: white;
                border-radius: 5px;
                padding: 10px;
                margin-bottom: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        # Chat container
        chat_container = st.empty()
        conversation = []

        # User input
        user_input: str | None = st.text_input("You:", "")

        if st.button("Send", key="send_button"):
            if user_input:
                conversation.append(("user", user_input))
                bot_response = self.__engine.invoke(question=user_input)
                conversation.append(("bot", bot_response))
                user_input = ""
            else:
                st.warning("Please enter a message.")

        # Display conversation
        for speaker, message in conversation:
            if speaker == "user":
                st.markdown(f'<div class="user-msg">{message}</div>', unsafe_allow_html=True)
            elif speaker == "bot":
                st.markdown(f'<div class="bot-msg">{message}</div>', unsafe_allow_html=True)