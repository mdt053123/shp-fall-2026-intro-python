"""
Quick self-test for the lecture apps (instructor use): python check_all.py
Uses FastAPI's TestClient, so no server needs to be running.
"""
import importlib.util
import os
import sys

from fastapi.testclient import TestClient

HERE = os.path.dirname(os.path.abspath(__file__))


def load(folder):
    path = os.path.join(HERE, folder, "main.py")
    spec = importlib.util.spec_from_file_location(folder, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return TestClient(module.app)


def expect(label, condition):
    print(("PASS  " if condition else "FAIL  ") + label)
    return condition


c = load("01_hello_api")
expect("01 /", c.get("/").json()["message"] == "Hello, World!")
expect("01 /hello/Ada", c.get("/hello/Ada").json() == {"greeting": "Hello, Ada!"})
expect("01 /square/abc -> 422", c.get("/square/abc").status_code == 422)
expect("01 /add", c.get("/add?a=3&b=4").json()["sum"] == 7)
expect("01 /roll", len(c.get("/roll?count=3").json()["rolls"]) == 3)

c = load("02_json_api")
expect("02 list", len(c.get("/facts").json()) == 3)
expect("02 filter", len(c.get("/facts?topic=food").json()) == 1)
expect("02 random", "text" in c.get("/facts/random").json())
expect("02 404", c.get("/facts/99").status_code == 404)
r = c.post("/facts", json={"text": "Test fact", "topic": "test"})
expect("02 create", r.status_code == 201 and r.json()["id"] == 4)
expect("02 bad body -> 422", c.post("/facts", json={"topic": "x"}).status_code == 422)
expect("02 delete", c.delete("/facts/4").status_code == 200 and c.get("/facts/4").status_code == 404)

c = load("03_html_pages")
expect("03 home", "Mad Libs" in c.get("/").text)
expect("03 project", "Hangman" in c.get("/projects/hangman").text)
expect("03 project 404", c.get("/projects/nope").status_code == 404)
expect("03 about", "Soccer" in c.get("/about").text)
expect("03 css", c.get("/static/style.css").status_code == 200)

c = load("04_forms")
expect("04 home", "Temperature" in c.get("/").text)
expect("04 convert", "100.0°C" in c.post("/convert", data={"temperature": "212", "direction": "f_to_c"}).text)
expect("04 grades", "85.0 → B" in c.post("/grades", data={"name": "Ada", "scores": "90, 80"}).text)
expect("04 grades bad", "Please enter numbers" in c.post("/grades", data={"name": "Ada", "scores": "abc"}).text)

c = load("05_ml_app")
expect("05 form", "Which penguin" in c.get("/").text)
expect("05 predict page", "Gentoo" in c.post("/predict", data={"bill_length": 49, "bill_depth": 15,
                                                               "flipper_length": 220, "body_mass": 5400}).text)
expect("05 api", c.get("/api/predict?bill_length=39&bill_depth=18.5&flipper_length=190&body_mass=3700").json()["species"] == "Adelie")
expect("05 api chinstrap", c.get("/api/predict?bill_length=49&bill_depth=18.5&flipper_length=196&body_mass=3700").json()["species"] == "Chinstrap")
