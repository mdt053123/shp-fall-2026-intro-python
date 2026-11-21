"""
Exercise 1 - API Endpoints
--------------------------
Add these JSON endpoints (each one is a small Python function you already know how to write!).
Test with:   python check.py          (no server needed)
Try it live: python -m uvicorn main:app --reload   ->  http://127.0.0.1:8000/docs

  GET  /is_prime/{n}             -> {"n": 7, "is_prime": true}
  GET  /reverse?text=hello       -> {"original": "hello", "reversed": "olleh"}
  GET  /fizzbuzz/{n}             -> {"n": 15, "result": "FizzBuzz"}   ("Fizz"/"Buzz"/"FizzBuzz"/the number as a string)
  GET  /stats?nums=4,8,15        -> {"count": 3, "sum": 27, "mean": 9.0, "min": 4, "max": 15}
                                    (nums arrives as ONE string -- split it on commas and convert!)
                                    If any value isn't a number, raise HTTPException(status_code=400, ...)
  POST /word_count               body: {"text": "the cat the hat"}
                                 -> {"words": 4, "unique": 3, "most_common": "the"}
  GET  /caesar?text=abc&shift=1  -> {"result": "bcd"}   (reuse your Day 3 Caesar cipher!)
"""

from collections import Counter

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Exercise 1")


class TextIn(BaseModel):  # given
    text: str


@app.get("/")
def home():  # given
    return {"message": "Exercise 1 API. Visit /docs to try the endpoints."}


@app.get("/is_prime/{n}")
def is_prime(n: int):
    # TODO
    pass


@app.get("/reverse")
def reverse(text: str):
    # TODO
    pass


@app.get("/fizzbuzz/{n}")
def fizzbuzz(n: int):
    # TODO
    pass


@app.get("/stats")
def stats(nums: str):
    # TODO
    pass


@app.post("/word_count")
def word_count(body: TextIn):
    # TODO
    pass


@app.get("/caesar")
def caesar(text: str, shift: int = 3):
    # TODO
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
