"""
02 - A JSON API: Create, Read, Delete
A tiny "fun facts" service. Other programs (a phone app, a website's JavaScript)
could use it to store and fetch facts.

    GET    /facts           list all facts
    GET    /facts/{id}      one fact (404 if missing)
    GET    /facts/random    a random fact
    POST   /facts           create a fact (send JSON in the request body)
    DELETE /facts/{id}      delete a fact

Run:  python -m uvicorn main:app --reload
Then use http://127.0.0.1:8000/docs to try every endpoint, including POST and DELETE
(click an endpoint -> "Try it out" -> "Execute").
"""

import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Fun Facts API")


# A Pydantic MODEL describes what data a request must contain.
# FastAPI checks it automatically and rejects bad requests with a helpful error.
class FactIn(BaseModel):
    text: str
    topic: str = "general"


# Our "database" is just a dict in memory (it resets when the server restarts).
facts = {
    1: {"id": 1, "text": "Python is named after Monty Python, not the snake.", "topic": "python"},
    2: {"id": 2, "text": "Octopuses have three hearts.", "topic": "animals"},
    3: {"id": 3, "text": "Honey never spoils.", "topic": "food"},
}
next_id = 4


@app.get("/facts")
def list_facts(topic: str = None):
    """All facts, optionally filtered: /facts?topic=animals"""
    results = list(facts.values())
    if topic is not None:
        results = [f for f in results if f["topic"] == topic]
    return results


# NOTE: /facts/random must come BEFORE /facts/{fact_id}, or "random" would be
# treated as an id! Routes are checked in order.
@app.get("/facts/random")
def random_fact():
    return random.choice(list(facts.values()))


@app.get("/facts/{fact_id}")
def get_fact(fact_id: int):
    if fact_id not in facts:
        # HTTP status codes: 200 OK, 201 Created, 404 Not Found, 422 bad input, 500 server error
        raise HTTPException(status_code=404, detail=f"No fact with id {fact_id}")
    return facts[fact_id]


@app.post("/facts", status_code=201)
def create_fact(fact: FactIn):
    global next_id
    new = {"id": next_id, "text": fact.text, "topic": fact.topic}
    facts[next_id] = new
    next_id += 1
    return new


@app.delete("/facts/{fact_id}")
def delete_fact(fact_id: int):
    if fact_id not in facts:
        raise HTTPException(status_code=404, detail=f"No fact with id {fact_id}")
    return facts.pop(fact_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
