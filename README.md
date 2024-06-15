# ChatMate

ChatMate is an intuitive web application designed to interact with document, offering precise answers based on the document's content.

## Overview

ChatMate showcases an elegant conversational interface built with [Python](https://www.python.org/) and [Langchain](https://www.langchain.com/), designed to provide insightful responses based on the content of documents.

## Installation

1. Clone the repository:

    ```
    git clone git@github.com:SirArt25/ChatMate.git
    ```

2. Install the required dependencies:

    ```
    pip3 install pipreqs
    pipreqs --force
    pip3 install -r requirements.txt
    pip3 install chromadb
    ```
    ---
    **NOTE** 

    - Please use Python 3.10 for ChatMate.
    
    - That if you use a virtual environment (venv), you should add the venv directory to the ignore list in the pipreqs command.
    ---
## Usage

1. Specify the Document's Actual Location

    Set the actual path of the document in config/manual.json under the "full-path" key.

2. Run the chatbot:

    ```
    streamlit run main.py
    ```

2. Start interacting with the chatbot through the command line interface.

## Features

- Basic conversational interface
- Responds to predefined prompts
- Minimalistic design

## UML Diagram

To view the UML diagram of the project, please follow these steps:

1. Install PlantUML:

    ```
    pip3 install plantuml
    ```
   
2. Generate PNG from project.puml

    ```
    python3 -m plantuml uml_diagrams/project.puml
    ```
After following these steps, you should have a PNG image generated 
from the project.puml file, 
which contains the UML diagram of the project. 
You can then view this image to understand the project's
structure and relationships.

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.
