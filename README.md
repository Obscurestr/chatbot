# Chatbot with Memory

A simple Flask-based chatbot web app that learns new answers from users during conversation and remembers them for future use. Uses a JSON file to store question-answer pairs and supports session-based chat history.

## Features

- Chat with a bot using predefined question-answer pairs from a dataset
- Teach the bot new answers when it doesn’t know how to respond
- Persistently save learned answers to a JSON memory file
- Session-based chat history display
- Restart chat button to clear conversation history

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Obscurestr/chatbot.git
    cd your-repo
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows use: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install flask
    ```

4. Place your `dialogs.txt` file (tab-separated question-answer pairs) in the project root.

### Running the App

```bash
python main.py 
