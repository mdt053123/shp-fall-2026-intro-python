"""
04 - Forms: Getting Input From Users on the Web
The web version of input(): an HTML <form>. When submitted, the browser sends the
values to our server, which computes a result and returns a new page.

  GET  /convert     show the empty form
  POST /convert     receive the form data, show the result

Form fields arrive as function parameters declared with Form().
(Needs: pip install python-multipart)

Run:  python -m uvicorn main:app --reload     then visit http://127.0.0.1:8000
"""

import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

HERE = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(HERE, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(HERE, "static")), name="static")


# ---- Our old Python functions from Days 1-2, now on the web! ----
def f_to_c(f):
    return (f - 32) * 5 / 9


def c_to_f(c):
    return c * 9 / 5 + 32


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


# ---- Temperature converter ----
@app.get("/convert", response_class=HTMLResponse)
def convert_form(request: Request):
    return templates.TemplateResponse(request, "convert.html")


@app.post("/convert", response_class=HTMLResponse)
def convert(request: Request, temperature: float = Form(), direction: str = Form()):
    if direction == "f_to_c":
        result = f"{temperature}°F = {f_to_c(temperature):.1f}°C"
    else:
        result = f"{temperature}°C = {c_to_f(temperature):.1f}°F"
    return templates.TemplateResponse(request, "convert.html", {"result": result})


# ---- Grade calculator ----
@app.get("/grades", response_class=HTMLResponse)
def grades_form(request: Request):
    return templates.TemplateResponse(request, "grades.html")


@app.post("/grades", response_class=HTMLResponse)
def grades(request: Request, name: str = Form(), scores: str = Form()):
    # The form sends ONE string like "90, 85, 77" -- we parse it ourselves (Day 3 + Day 5 skills!)
    try:
        numbers = [float(s) for s in scores.replace(",", " ").split()]
        if not numbers:
            raise ValueError("no scores")
    except ValueError:
        return templates.TemplateResponse(request, "grades.html",
                                          {"error": "Please enter numbers separated by commas or spaces."})
    average = sum(numbers) / len(numbers)
    return templates.TemplateResponse(request, "grades.html", {
        "name": name,
        "scores": numbers,
        "average": round(average, 2),
        "letter": letter_grade(average),
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
