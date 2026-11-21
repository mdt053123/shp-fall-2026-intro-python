"""
05 - Serving a Machine Learning Model on the Web 🐧
Train a k-NN penguin classifier ONCE when the server starts (Day 9), then let anyone
predict a penguin's species by filling in a form -- or by calling the JSON API.

    GET  /                the form
    POST /predict         the form's result page (HTML)
    GET  /api/predict?bill_length=45&bill_depth=15&flipper_length=215&body_mass=5000   (JSON)

This is how real ML products work: a trained model behind a web API.

Run:  python -m uvicorn main:app --reload     then visit http://127.0.0.1:8000
"""

import os

import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

HERE = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(title="Penguin Classifier")
templates = Jinja2Templates(directory=os.path.join(HERE, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(HERE, "static")), name="static")

# ---- Train the model at startup ----
FEATURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
penguins = pd.read_csv(os.path.join(HERE, "penguins.csv")).dropna()
model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
model.fit(penguins[FEATURES], penguins["species"])
print(f"Model trained on {len(penguins)} penguins")

EMOJI = {"Adelie": "🐧", "Chinstrap": "⛑️🐧", "Gentoo": "🧡🐧"}


def predict_species(bill_length, bill_depth, flipper_length, body_mass):
    """Return (species, {species: probability}) for one penguin."""
    row = pd.DataFrame([[bill_length, bill_depth, flipper_length, body_mass]], columns=FEATURES)
    species = model.predict(row)[0]
    probs = {s: round(float(p), 2) for s, p in zip(model.classes_, model.predict_proba(row)[0])}
    return species, probs


@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    # Pre-fill the form with the average penguin
    defaults = penguins[FEATURES].mean().round(1).to_dict()
    return templates.TemplateResponse(request, "index.html", {"defaults": defaults})


@app.post("/predict", response_class=HTMLResponse)
def predict_page(request: Request,
                 bill_length: float = Form(), bill_depth: float = Form(),
                 flipper_length: float = Form(), body_mass: float = Form()):
    species, probs = predict_species(bill_length, bill_depth, flipper_length, body_mass)
    inputs = {"bill_length_mm": bill_length, "bill_depth_mm": bill_depth,
              "flipper_length_mm": flipper_length, "body_mass_g": body_mass}
    return templates.TemplateResponse(request, "result.html", {
        "species": species, "emoji": EMOJI[species], "probs": probs, "inputs": inputs})


@app.get("/api/predict")
def predict_api(bill_length: float, bill_depth: float, flipper_length: float, body_mass: float):
    species, probs = predict_species(bill_length, bill_depth, flipper_length, body_mass)
    return {"species": species, "probabilities": probs}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
