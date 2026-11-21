"""
Exercise 1 - API Endpoints  (SOLUTION)
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
    if n < 2:
        return {"n": n, "is_prime": False}
    d = 2
    while d * d <= n:
        if n % d == 0:
            return {"n": n, "is_prime": False}
        d += 1
    return {"n": n, "is_prime": True}


@app.get("/reverse")
def reverse(text: str):
    return {"original": text, "reversed": text[::-1]}


@app.get("/fizzbuzz/{n}")
def fizzbuzz(n: int):
    if n % 15 == 0:
        result = "FizzBuzz"
    elif n % 3 == 0:
        result = "Fizz"
    elif n % 5 == 0:
        result = "Buzz"
    else:
        result = str(n)
    return {"n": n, "result": result}


@app.get("/stats")
def stats(nums: str):
    try:
        values = [float(x) for x in nums.split(",") if x.strip()]
    except ValueError:
        raise HTTPException(status_code=400, detail="nums must be numbers separated by commas")
    if not values:
        raise HTTPException(status_code=400, detail="no numbers given")
    values = [int(v) if v.is_integer() else v for v in values]
    return {"count": len(values), "sum": sum(values), "mean": sum(values) / len(values),
            "min": min(values), "max": max(values)}


@app.post("/word_count")
def word_count(body: TextIn):
    words = body.text.lower().split()
    most = Counter(words).most_common(1)[0][0] if words else None
    return {"words": len(words), "unique": len(set(words)), "most_common": most}


@app.get("/caesar")
def caesar(text: str, shift: int = 3):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        elif ch.isupper():
            result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += ch
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
