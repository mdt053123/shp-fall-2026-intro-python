"""
03 - HTML Pages with Templates
APIs return JSON for PROGRAMS. For HUMANS, we return HTML pages.

Templates (in templates/) are HTML files with Jinja2 placeholders:
    {{ variable }}                     insert a value
    {% for x in items %}...{% endfor %}   loop
    {% if cond %}...{% endif %}          condition
    {% extends "base.html" %}          reuse a shared layout

Run:  python -m uvicorn main:app --reload     then visit http://127.0.0.1:8000
"""

import os
from datetime import date

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

HERE = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(HERE, "templates"))
# Files in static/ (CSS, images) are served as-is at /static/...
app.mount("/static", StaticFiles(directory=os.path.join(HERE, "static")), name="static")

PROJECTS = [
    {"slug": "mad-libs", "name": "Mad Libs", "day": 1, "description": "A story built from user input and f-strings."},
    {"slug": "guess", "name": "Guess the Number", "day": 2, "description": "Loops, conditionals, and random numbers."},
    {"slug": "hangman", "name": "Hangman", "day": 3, "description": "Strings and sets in a game loop."},
    {"slug": "gradebook", "name": "Gradebook", "day": 4, "description": "Classes that grow into a full web app."},
    {"slug": "knn", "name": "Penguin Classifier", "day": 9, "description": "k-nearest neighbors from scratch."},
]


# response_class=HTMLResponse tells FastAPI (and the /docs page) that this returns HTML.
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # TemplateResponse(request, template file, dict of variables for the template)
    return templates.TemplateResponse(request, "index.html", {
        "name": "Your Name Here",
        "today": date.today().strftime("%B %d, %Y"),
        "projects": PROJECTS,
    })


@app.get("/projects/{slug}", response_class=HTMLResponse)
def project(request: Request, slug: str):
    for p in PROJECTS:
        if p["slug"] == slug:
            return templates.TemplateResponse(request, "project.html", {"project": p})
    raise HTTPException(status_code=404, detail="Project not found")


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(request, "about.html", {
        "skills": ["Python", "NumPy", "pandas", "Machine learning", "FastAPI"],
        "hobbies": ["Chess", "Soccer", "Baking"],
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
