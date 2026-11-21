"""
Exercise 2 - A Solar System Website 🪐
--------------------------------------
Build a small website from a list of dicts (data from NASA's planetary fact sheet).

Routes to write:
  GET /                        HTML: table of all planets (given template: planets.html)
                               Optional ?sort=diameter_km (or any numeric key) sorts the table, largest first.
  GET /planet/{name}           HTML: one planet's page (YOU write templates/planet.html).
                               Case-insensitive ("mars" or "Mars"). 404 if not found.
  GET /search?q=gas            HTML: planets.html showing only planets whose name, type, or
                               fact contains q (case-insensitive).
  GET /api/planets             JSON: the whole list
  GET /api/planets/{name}      JSON: one planet (404 if not found)
  GET /api/biggest?n=3         JSON: names of the n largest planets by diameter

Test with:   python check.py
Run live:    python -m uvicorn main:app --reload
"""

import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

HERE = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(title="Solar System")
templates = Jinja2Templates(directory=os.path.join(HERE, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(HERE, "static")), name="static")

PLANETS = [
    {"name": "Mercury", "type": "rocky", "order": 1, "diameter_km": 4879, "distance_million_km": 57.9,
     "day_hours": 4222.6, "year_days": 88.0, "fact": "Temperatures swing from about 430°C by day to -180°C at night."},
    {"name": "Venus", "type": "rocky", "order": 2, "diameter_km": 12104, "distance_million_km": 108.2,
     "day_hours": 2802.0, "year_days": 224.7, "fact": "It spins backwards, and a day there is longer than its year."},
    {"name": "Earth", "type": "rocky", "order": 3, "diameter_km": 12756, "distance_million_km": 149.6,
     "day_hours": 24.0, "year_days": 365.2, "fact": "The only planet known to have life (and Python programmers)."},
    {"name": "Mars", "type": "rocky", "order": 4, "diameter_km": 6792, "distance_million_km": 228.0,
     "day_hours": 24.7, "year_days": 687.0, "fact": "Home to Olympus Mons, the tallest volcano in the solar system."},
    {"name": "Jupiter", "type": "gas giant", "order": 5, "diameter_km": 142984, "distance_million_km": 778.5,
     "day_hours": 9.9, "year_days": 4331.0, "fact": "Its Great Red Spot is a storm wider than Earth."},
    {"name": "Saturn", "type": "gas giant", "order": 6, "diameter_km": 120536, "distance_million_km": 1432.0,
     "day_hours": 10.7, "year_days": 10747.0, "fact": "It is less dense than water; it would float in a giant bathtub."},
    {"name": "Uranus", "type": "ice giant", "order": 7, "diameter_km": 51118, "distance_million_km": 2867.0,
     "day_hours": 17.2, "year_days": 30589.0, "fact": "It rotates on its side, tilted about 98 degrees."},
    {"name": "Neptune", "type": "ice giant", "order": 8, "diameter_km": 49528, "distance_million_km": 4515.0,
     "day_hours": 16.1, "year_days": 59800.0, "fact": "It has the fastest winds in the solar system."},
]


def find_planet(name):
    """Return the planet dict whose name matches (ignoring case), or None."""
    # TODO
    pass


@app.get("/", response_class=HTMLResponse)
def planet_list(request: Request, sort: str = None):
    # TODO
    pass


@app.get("/planet/{name}", response_class=HTMLResponse)
def planet_page(request: Request, name: str):
    # TODO
    pass


@app.get("/search", response_class=HTMLResponse)
def search(request: Request, q: str = ""):
    # TODO
    pass


@app.get("/api/planets")
def api_planets():
    # TODO
    pass


@app.get("/api/planets/{name}")
def api_planet(name: str):
    # TODO
    pass


@app.get("/api/biggest")
def api_biggest(n: int = 3):
    # TODO
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
