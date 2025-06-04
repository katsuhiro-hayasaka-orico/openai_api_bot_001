# openai_api_bot_001

This project provides a simple Streamlit application that works as a ChatGPT-like assistant using the OpenAI API. It demonstrates how to interact with the API in a streaming manner and how to handle basic conversation history within Streamlit.

## Setup

1. Clone this repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Configure your OpenAI API key using Streamlit's secrets. Create a file named `.streamlit/secrets.toml` and add the following:

```toml
[OpenAIAPI]
openai_api_key = "sk-..."
```

## Running the app

Execute the Streamlit app with:

```bash
streamlit run app.py
```

The chat interface will open in your browser. Enter your message and the bot will respond using the OpenAI API.
