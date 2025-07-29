# OpenAI API Bot

This repository contains a simple Streamlit chatbot using the OpenAI API.

## Othello Game


The repository includes `othello.html`, an improved browser-based Othello game.
You can choose between Human vs. Human, Human vs. AI, or AI vs. AI modes.
The built-in AI uses a minimax search with alpha–beta pruning.
Open the file in your browser and click “新規ゲーム” to start.

## Lottery Roulette

`roulette.html` is a fully client-side lottery tool. Paste or load participant names from a `.txt` file, set the number of winners and click **START** to spin the slots. Names flash with short beeps until you press **STOP**, then the selected winners are highlighted in red with a small fanfare. Use **CLEAR** to reset the screen. Everything runs locally using plain HTML, CSS and JavaScript with the Web Audio API (audio gracefully falls back if unsupported).

## FAQ Prototype

A small FastAPI backend and simple HTML frontend are included for experimenting with a FAQ system.

### Running the backend

```
uvicorn faq_api:app --reload
```

### Using the frontend

Open `faq_frontend.html` in your browser. It allows you to search questions, post new questions and answers, and view existing answers using the API.
