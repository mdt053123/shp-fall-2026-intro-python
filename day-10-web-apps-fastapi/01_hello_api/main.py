"""
01 - Hello, API!
A web SERVER waits for REQUESTS from clients (browsers, apps) and sends back RESPONSES.

Run it (from inside this folder):
    python -m uvicorn main:app --reload
(or just run this file in Thonny), then open in your browser:
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/hello/Ada
    http://127.0.0.1:8000/add?a=3&b=4
    http://127.0.0.1:8000/docs          <- FastAPI builds interactive docs for FREE!
Stop the server with Ctrl+C.
"""

import random

from fastapi import FastAPI

app = FastAPI()


# A DECORATOR (@...) connects a URL path to a Python function: a "route".
# When someone visits "/", FastAPI calls home() and sends back what it returns.
@app.get("/")
def home():
    return {"message": "Hello, World!", "course": "SHP Intro to Python"}
    # Returning a dict sends JSON: the universal data format of the web.


# PATH PARAMETERS: part of the URL becomes a function argument.
@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"Hello, {name}!"}


# Type hints matter: FastAPI converts "7" -> 7 and rejects /square/abc with a clear error.
@app.get("/square/{n}")
def square(n: int):
    return {"n": n, "square": n * n}


# QUERY PARAMETERS: anything after ? in the URL, like /add?a=3&b=4
@app.get("/add")
def add(a: float, b: float):
    return {"a": a, "b": b, "sum": a + b}


# Default values make query parameters optional: /roll or /roll?sides=20&count=3
@app.get("/roll")
def roll(sides: int = 6, count: int = 1):
    rolls = [random.randint(1, sides) for _ in range(count)]
    return {"rolls": rolls, "total": sum(rolls)}


# This lets you start the server by running the file (e.g. the Run button in Thonny).
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
