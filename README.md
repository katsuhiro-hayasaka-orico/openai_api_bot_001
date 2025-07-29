# OpenAI API Bot

This repository contains a simple Streamlit chatbot using the OpenAI API.

## Othello Game


The repository includes `othello.html`, an improved browser-based Othello game.
You can choose between Human vs. Human, Human vs. AI, or AI vs. AI modes.
The built-in AI uses a minimax search with alpha–beta pruning.
Open the file in your browser and click “新規ゲーム” to start.

## Lottery Roulette

The repository also provides `roulette.html`, a small local tool for picking random winners with a spinning wheel. Open the file in your browser, enter names line by line, and click "回す" to spin the wheel and reveal the winner. Audio cues are generated using the Web Audio API.

## FAQ Prototype

A small FastAPI backend and simple HTML frontend are included for experimenting with a FAQ system.

### Running the backend

```
uvicorn faq_api:app --reload
```

### Using the frontend

Open `faq_frontend.html` in your browser. It allows you to search questions, post new questions and answers, and view existing answers using the API.
