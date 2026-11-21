# Day 10 (Sat 12/5): Web Apps with FastAPI

**Big idea:** Everything we've built so far runs only on *your* computer. A **web server** lets anyone with a browser, or any other program, use your Python code. Today we build JSON APIs and HTML websites with **FastAPI**, a modern web framework used at companies like Microsoft, Uber, and Netflix. We finish by putting a **machine-learning model** and the **Gradebook** on the web.

> **Setup:** `pip install fastapi uvicorn jinja2 python-multipart` (or use Thonny's package manager). See [SETUP.md](../SETUP.md).

## Learning goals
- [ ] Explain the client/server model, URLs, HTTP methods (GET/POST), status codes, and JSON
- [ ] Write FastAPI routes with path parameters, query parameters, and type hints
- [ ] Use the automatic `/docs` page to test an API
- [ ] Accept JSON request bodies with Pydantic models, and return errors with `HTTPException`
- [ ] Render HTML with Jinja2 templates (variables, loops, conditions, layout inheritance)
- [ ] Handle HTML forms (`Form()`), and redirect after a POST
- [ ] Serve a trained ML model behind a web page and an API

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Welcome back! Day 9 review, check in on M8 | |
| 0:10 | How the web works (HTTP, URLs, JSON) | notes below |
| 0:25 | Hello, API: routes and parameters, `/docs` | `01_hello_api/` |
| 0:45 | A JSON API: create/read/delete, 404s, Pydantic | `02_json_api/` |
| 1:05 | *Break* | |
| 1:15 | HTML templates and CSS | `03_html_pages/` |
| 1:40 | Forms: our Day 1–2 programs on the web | `04_forms/` |
| 2:00 | An ML model on the web 🐧 | `05_ml_app/` |
| 2:15 | Exercises / Gradebook M9 | `exercises/`, [project](../gradebook-project/m9-web-app/) |

### Running any app today
```bash
cd 1205-day-10-web-apps-fastapi/01_hello_api
python -m uvicorn main:app --reload
```
Then open **http://127.0.0.1:8000** in your browser. `--reload` restarts the server whenever you save a change. Stop it with **Ctrl+C**. (You can also press Run in Thonny, since every `main.py` ends with `uvicorn.run(...)`.)

---

## Lecture notes

### 1. How the web works
```
 Browser (client)  ── request:  GET /hello/Ada ──▶  Your Python server
                   ◀── response: 200 OK + data ───
```
- **URL:** `http://127.0.0.1:8000/add?a=3&b=4` breaks into these parts:
  - `127.0.0.1` is the host. It means "this computer," also called `localhost`.
  - `8000` is the port.
  - `/add` is the **path**.
  - `a=3&b=4` is the **query string**.
- **HTTP methods:** **GET** reads something (visiting a page). **POST** sends or creates something (submitting a form). **DELETE** removes something.
- **Status codes:**
  - **200** OK
  - **201** Created
  - **303** "go see another page" (a redirect)
  - **404** Not Found
  - **422** invalid input
  - **500** server crashed
- **JSON** is the web's data format. It looks just like Python dicts and lists.

### 2. Routes (`01_hello_api`)
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/hello/{name}")          # path parameter
def hello(name: str):
    return {"greeting": f"Hello, {name}!"}    # dict -> JSON

@app.get("/add")                   # query parameters: /add?a=3&b=4
def add(a: float, b: float = 0):   # type hints = automatic conversion + validation
    return {"sum": a + b}
```
Visit **`/docs`** for free interactive documentation.

### 3. JSON APIs (`02_json_api`)
```python
class FactIn(BaseModel):           # Pydantic describes the expected JSON body
    text: str
    topic: str = "general"

@app.post("/facts", status_code=201)
def create_fact(fact: FactIn): ...

raise HTTPException(status_code=404, detail="Not found")
```
Routes are matched **in order**, so `/facts/random` must come before `/facts/{fact_id}`.

### 4. HTML templates (`03_html_pages`)
```python
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"name": "Ada", "projects": PROJECTS})
```
```html
<h1>Hi, {{ name }}</h1>
{% for p in projects %} <li>{{ p.name }}</li> {% endfor %}
{% if p.day >= 7 %} ... {% endif %}
{% extends "base.html" %} / {% block content %}{% endblock %}
```
CSS goes in `static/`, which is served with `app.mount("/static", StaticFiles(directory="static"))`.

### 5. Forms (`04_forms`)
```html
<form action="/convert" method="post">
    <input type="number" name="temperature">   <!-- name must match the Python parameter -->
    <button type="submit">Convert</button>
</form>
```
```python
@app.post("/convert", response_class=HTMLResponse)
def convert(request: Request, temperature: float = Form()): ...
```
After a POST that *changes* data, **redirect** with `RedirectResponse(url, status_code=303)`. That way, refreshing the page doesn't submit the form twice.

### 6. ML on the web (`05_ml_app`)
Train the model **once** at startup, then call `model.predict(...)` inside a route. The same function serves both an HTML form and a JSON API. This is how real ML products work.

### 7. State
A web server handles many separate requests; it doesn't sit in a `while` loop waiting for `input()`. Anything the app must *remember* (a game's secret number, a gradebook) lives in a variable on the server, or better, in a **file or database** so it survives restarts.

---

## Common mistakes
- Running `uvicorn` from the wrong folder, which gives `Could not import module "main"`. `cd` into the app's folder first.
- `Address already in use`: another server is still running. Stop it, or use `--port 8001`.
- A form's `name="..."` not matching the Python parameter name, which gives a 422 error.
- Forgetting `python-multipart`, which makes form routes crash.
- Returning a plain string for HTML without `response_class=HTMLResponse`.
- Changing data on a GET request. Use POST for anything that changes data.

## Key terms

| Term | Meaning |
|------|---------|
| **client / server** | The program making requests / the program answering them |
| **HTTP** | The protocol (set of rules) that browsers and servers speak |
| **URL, path, query string** | A web address / the `/part` / the `?key=value` part |
| **GET / POST** | Read something / send or create something |
| **status code** | A number describing the result (200, 404...) |
| **API** | Application Programming Interface: a way for *programs* to use a service |
| **JSON** | JavaScript Object Notation: text data shaped like dicts and lists |
| **route / endpoint** | A URL + method handled by one function |
| **template** | HTML with placeholders filled in by Python |
| **redirect** | Telling the browser to go to another URL |

## Exercises → [`exercises/`](exercises/)
Each exercise folder has a `main.py` starter and a `check.py`. Run `python check.py` to test **without** starting a server.

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | API endpoints | path and query params, JSON bodies, 400 errors, reusing old functions |
| 2 | Solar System website 🪐 | templates, sorting, search, detail pages, 404s, a JSON API |
| 3 | Guess the Number on the web 🎯 | forms and server-side state |

## 📘 Gradebook Project, Milestone 9
Put your gradebook online: a class table, student pages with a **predicted final** (from your M8 model), forms to add students and scores, auto-saving, and a JSON API.
→ [gradebook-project/m9-web-app](../gradebook-project/m9-web-app/)

## Videos and reading
1. FastAPI official tutorial (excellent and beginner-friendly): https://fastapi.tiangolo.com/tutorial/
2. FastAPI templates guide: https://fastapi.tiangolo.com/advanced/templates/
3. Intro to HTML and CSS (MDN): https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website
4. How the web works (MDN): https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works

*Instructor note:* `python check_all.py` in this folder tests all 5 lecture apps at once.
