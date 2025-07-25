from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path
import time
import difflib

DATA_FILE = Path("data.json")

def load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {"questions": [], "answers": []}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


data = load_data()

app = FastAPI(title="FAQ Prototype")


class Question(BaseModel):
    text: str
    tags: List[str] = []


class Answer(BaseModel):
    question_id: int
    answer: str


@app.post("/question")
def post_question(q: Question):
    new_id = (data["questions"][-1]["id"] + 1) if data["questions"] else 1
    entry = {
        "id": new_id,
        "text": q.text,
        "tags": q.tags,
        "created_at": time.time(),
    }
    data["questions"].append(entry)
    save_data(data)
    return entry


@app.post("/answer")
def post_answer(a: Answer):
    if not any(q["id"] == a.question_id for q in data["questions"]):
        raise HTTPException(status_code=404, detail="Question not found")
    entry = {
        "question_id": a.question_id,
        "answer": a.answer,
        "timestamp": time.time(),
    }
    data["answers"].append(entry)
    save_data(data)
    return entry


def search_questions(query: str):
    matches = []
    for q in data["questions"]:
        ratio = difflib.SequenceMatcher(None, query.lower(), q["text"].lower()).ratio()
        if ratio > 0.3:
            matches.append((ratio, q))
    matches.sort(reverse=True, key=lambda x: x[0])
    return [q for _, q in matches]


@app.get("/search")
def search(query: str):
    return search_questions(query)


@app.get("/answers/{question_id}")
def get_answers(question_id: int):
    ans = [a for a in data["answers"] if a["question_id"] == question_id]
    ans.sort(key=lambda x: x["timestamp"])
    return ans
