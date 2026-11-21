"""
Exercise 3 - Guess the Number, on the Web 🎯  (SOLUTION)
--------------------------------------------
Remember Guess the Number from Day 2? Rebuild it as a web app.

A web server doesn't "wait" inside a while loop for input. Each guess is a NEW
request, so the game's STATE (the secret number and the guesses so far) must be
stored between requests. We keep it in a global dict called `game`.

Routes to write:
  GET  /        show the game page (template given: game.html)
  POST /guess   form field "guess" (int). Record it and set a message:
                  - outside 1-100      -> "Pick a number from 1 to 100."  (don't record it)
                  - too low / too high -> "{guess} is too low!" / "{guess} is too high!"
                  - correct            -> "🎉 {guess} is right! You got it in {n} guesses."
                                          and set game["won"] = True
                Then show the game page again.
  POST /new     start a new game (new secret, empty guesses, won = False), show the page

Helper to write: new_game() resets the `game` dict.

Test: python check.py    Play: python -m uvicorn main:app --reload

Bonus: keep a "best score" (fewest guesses) across games, or add difficulty levels.
"""

import os
import random

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

HERE = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(title="Guess the Number")
templates = Jinja2Templates(directory=os.path.join(HERE, "templates"))

game = {"secret": 0, "guesses": [], "won": False, "message": "", "best": None}


def new_game():
    """Reset the game: a new random secret from 1 to 100, no guesses, not won.
    (Keep game["best"] -- that's the bonus!)"""
    game["secret"] = random.randint(1, 100)
    game["guesses"] = []
    game["won"] = False
    game["message"] = "I'm thinking of a number from 1 to 100..."


def render(request):  # given
    return templates.TemplateResponse(request, "game.html", {"game": game})


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return render(request)


@app.post("/guess", response_class=HTMLResponse)
def guess(request: Request, guess: int = Form()):
    if game["won"]:
        game["message"] = "You already won! Start a new game."
    elif not 1 <= guess <= 100:
        game["message"] = "Pick a number from 1 to 100."
    else:
        game["guesses"].append(guess)
        if guess < game["secret"]:
            game["message"] = f"{guess} is too low!"
        elif guess > game["secret"]:
            game["message"] = f"{guess} is too high!"
        else:
            n = len(game["guesses"])
            game["won"] = True
            game["message"] = f"🎉 {guess} is right! You got it in {n} guesses."
            if game["best"] is None or n < game["best"]:
                game["best"] = n
    return render(request)


@app.post("/new", response_class=HTMLResponse)
def new(request: Request):
    new_game()
    return render(request)


new_game()   # start the first game when the server starts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
