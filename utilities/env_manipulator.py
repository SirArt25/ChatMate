def configure_environment():
    import os
    import openai
    import sys
    sys.path.append('../../..')
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())  # read local .env file

    openai.api_key = os.environ['OPENAI_API_KEY']