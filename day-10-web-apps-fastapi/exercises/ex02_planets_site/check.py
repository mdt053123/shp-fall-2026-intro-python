"""Checks for Exercise 2. Run:  python check.py   (from this folder)"""

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


def rows_in_order(html, names):
    """True if the planet names appear in this order in the HTML."""
    positions = [html.find(n) for n in names]
    return -1 not in positions and positions == sorted(positions)


check("find_planet('mars')", lambda: __import__("main").find_planet("mars")["name"], "Mars")
check("find_planet('pluto')", lambda: __import__("main").find_planet("pluto"), None)
check("home lists planets", lambda: rows_in_order(client.get("/").text, ["Mercury", "Venus", "Earth", "Neptune"]), True)
check("home sorted by diameter", lambda: rows_in_order(client.get("/?sort=diameter_km").text, ["Jupiter", "Saturn", "Uranus"]), True)
check("planet page", lambda: "Olympus Mons" in client.get("/planet/mars").text, True)
check("planet page shows times_earth", lambda: "0.53" in client.get("/planet/Mars").text, True)
check("planet page 404", lambda: client.get("/planet/pluto").status_code, 404)
check("search 'giant'", lambda: sum(n in client.get("/search?q=giant").text for n in ["Jupiter", "Saturn", "Uranus", "Neptune", "Mars"]), 4)
check("api list", lambda: len(client.get("/api/planets").json()), 8)
check("api one", lambda: client.get("/api/planets/SATURN").json()["type"], "gas giant")
check("api 404", lambda: client.get("/api/planets/vulcan").status_code, 404)
check("api biggest", lambda: client.get("/api/biggest?n=2").json(), ["Jupiter", "Saturn"])
