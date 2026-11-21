"""Checks for Exercise 1. Run:  python check.py   (from this folder)"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def check(label, get_actual, expected):
    try:
        actual = get_actual()
    except Exception as e:
        print(f"FAIL  {label}: crashed with {type(e).__name__}: {e}")
        return
    if actual == expected:
        print(f"PASS  {label}")
    else:
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("/is_prime/7", lambda: client.get("/is_prime/7").json(), {"n": 7, "is_prime": True})
check("/is_prime/9", lambda: client.get("/is_prime/9").json(), {"n": 9, "is_prime": False})
check("/is_prime/1", lambda: client.get("/is_prime/1").json(), {"n": 1, "is_prime": False})
check("/reverse", lambda: client.get("/reverse?text=hello").json(), {"original": "hello", "reversed": "olleh"})
check("/fizzbuzz/15", lambda: client.get("/fizzbuzz/15").json(), {"n": 15, "result": "FizzBuzz"})
check("/fizzbuzz/9", lambda: client.get("/fizzbuzz/9").json()["result"], "Fizz")
check("/fizzbuzz/7", lambda: client.get("/fizzbuzz/7").json()["result"], "7")
check("/stats", lambda: client.get("/stats?nums=4,8,15").json(), {"count": 3, "sum": 27, "mean": 9.0, "min": 4, "max": 15})
check("/stats bad input -> 400", lambda: client.get("/stats?nums=4,x").status_code, 400)
check("/word_count", lambda: client.post("/word_count", json={"text": "the cat the hat"}).json(),
      {"words": 4, "unique": 3, "most_common": "the"})
check("/caesar", lambda: client.get("/caesar?text=abc&shift=1").json(), {"result": "bcd"})
check("/caesar wraps", lambda: client.get("/caesar?text=Xyz!&shift=3").json(), {"result": "Abc!"})
