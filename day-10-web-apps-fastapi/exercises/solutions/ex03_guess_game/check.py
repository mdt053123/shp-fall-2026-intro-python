"""Checks for Exercise 3. Run:  python check.py   (from this folder)"""

from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


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


def fresh_game_with_secret(secret):
    main.new_game()
    main.game["secret"] = secret


check("new_game() picks 1-100", lambda: (main.new_game(), 1 <= main.game["secret"] <= 100)[1], True)
check("new_game() clears guesses", lambda: (main.new_game(), main.game["guesses"])[1], [])
check("home page", lambda: client.get("/").status_code, 200)

fresh_game_with_secret(42)
check("too low", lambda: "10 is too low!" in client.post("/guess", data={"guess": 10}).text, True)
check("too high", lambda: "90 is too high!" in client.post("/guess", data={"guess": 90}).text, True)
check("out of range not recorded", lambda: ("1 to 100" in client.post("/guess", data={"guess": 500}).text, main.game["guesses"]), (True, [10, 90]))
check("correct", lambda: "You got it in 3 guesses" in client.post("/guess", data={"guess": 42}).text, True)
check("won flag", lambda: main.game["won"], True)
check("new game resets", lambda: (client.post("/new"), main.game["guesses"], main.game["won"])[1:], ([], False))
