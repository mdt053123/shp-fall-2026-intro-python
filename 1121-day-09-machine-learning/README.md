# Day 9 (Sat 11/21): Machine Learning

**Big idea:** Machine learning means **learning patterns from examples** instead of writing the rules by hand. We build two classic algorithms **from scratch**, k-nearest neighbors (classification) and linear regression, so there's no magic. Then we use **scikit-learn** to do it properly and learn how to evaluate models honestly.

This day brings together much of the course: distance (tuples, Day 3), sorting with keys (Day 5), counting with dicts/`Counter`, NumPy (Day 7), and pandas (Day 8).

## Learning goals
- [ ] Explain supervised learning: features, labels, training, prediction
- [ ] Tell classification (predicting a category) apart from regression (predicting a number)
- [ ] Implement Euclidean distance, 1-NN, and k-NN with majority vote
- [ ] Evaluate with a train/test split, accuracy, and a **baseline**
- [ ] Explain why feature scaling matters for distance-based models
- [ ] Implement least-squares linear regression, and evaluate it with MAE and R²
- [ ] Use the scikit-learn API (`fit` / `predict` / `score`), pipelines, and cross-validation
- [ ] Recognize overfitting and data leakage

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 8 review (penguin clusters!), check in on M7 | |
| 0:10 | What is ML? Distance and similarity | `01` |
| 0:20 | Nearest neighbor; k-NN | `02`, `03` |
| 0:45 | Train/test split, accuracy, scaling (real penguins) | `04` |
| 1:05 | *Break* | |
| 1:15 | Linear regression from scratch | `05` |
| 1:35 | scikit-learn: pipelines, cross-validation, trees, regression | `06_sklearn.ipynb` |
| 2:05 | Can ML predict stocks? Baselines and leakage | `07_stock_prediction.ipynb` |
| 2:20 | Exercises / Gradebook M8 | `exercises/`, [project](../gradebook-project/m8-prediction/) |

---

## Lecture notes

### 1. What is machine learning?
**Traditional programming:** rules + data → answers. **Machine learning:** data + answers → *rules* (a model).

In **supervised learning**, each training example has **features** (inputs, `X`) and a **label** (the answer, `y`). The model learns from the examples, then **predicts** labels for new inputs.

| | Classification | Regression |
|--|---------------|------------|
| Predicts | a category (species, spam or not) | a number (mass, price) |
| Example model | k-NN, decision tree | linear regression |
| Metric | accuracy, confusion matrix | MAE, R² |

### 2. k-Nearest Neighbors (`01`–`03`)
```
distance(p, q) = sqrt(sum((a - b)^2 for a, b in zip(p, q)))
to classify a point: sort the training data by distance, take the k closest, majority vote
```
- **k = 1** is sensitive to noise. A **bigger k** is smoother but blurrier. Use an **odd k** for 2 classes.
- There's no training step: the "model" *is* the data. Prediction is slow for huge datasets.
- ⚠️ **Scale your features!** Grams (thousands) swamp millimeters (tens). Standardize each feature: `(x - mean) / std`, using **training** statistics.

### 3. Evaluating honestly (`04`)
1. **Split** the data. Train on about 80%, test on about 20% that the model has **never seen**.
2. **Accuracy** = correct predictions / total.
3. **Compare with a baseline**, e.g. "always guess the most common class."
4. **Choose settings** (like k) with **cross-validation** on the training set, not by peeking at the test set.

### 4. Linear regression (`05`)
The best-fit line minimizes the squared errors:
```
m = sum((x - x̄)(y - ȳ)) / sum((x - x̄)²)
b = ȳ - m·x̄
```
- **MAE** is the average size of the error, in real units.
- **R²** is the fraction of variation explained: 1 is perfect, and 0 means no better than guessing the mean.
- ⚠️ Lines don't know when to stop. Don't **extrapolate** far beyond your data.

### 5. scikit-learn (`06_sklearn.ipynb`)
```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
model.fit(X_train, y_train)
model.score(X_test, y_test)
cross_val_score(model, X_train, y_train, cv=5).mean()
```
Also covered: `DecisionTreeClassifier` (with readable rules), `LinearRegression` with several features, and the confusion matrix.

### 6. Lessons from the stock market (`07_stock_prediction.ipynb`)
- A model predicting "tomorrow's price" scores R² ≈ 0.97, **exactly as good as "tomorrow = today."** It learned nothing new.
- Predicting up/down gets about the same accuracy as "always guess up."
- **Time series:** split by time (no shuffling!). Otherwise you **leak** the future into training.
- **Overfitting:** a model that memorizes the training data scores great on training and worse on test.

---

## Common mistakes
- Testing on the training data, which gives fake-high accuracy.
- Forgetting to scale features for k-NN.
- Fitting the scaler on **all** the data (that's leakage). Fit it on the training data only. A pipeline does this for you.
- Reporting accuracy without a baseline.
- Passing a 1D `X` to scikit-learn. Use `df[["col"]]` (double brackets) for one feature.
- Shuffling time-series data before splitting.

## Key terms

| Term | Meaning |
|------|---------|
| **feature / label** | An input variable / the answer to predict |
| **training / test set** | The data the model learns from / the held-out data used to evaluate it |
| **classification / regression** | Predict a category / predict a number |
| **k-NN** | Predict by majority vote of the k closest training examples |
| **baseline** | The simplest reasonable prediction, to compare against |
| **accuracy** | The fraction of correct predictions |
| **confusion matrix** | A table of true vs predicted classes |
| **feature scaling** | Putting features on comparable scales (standardizing) |
| **cross-validation** | Rotating which part of the training data is held out, to choose settings fairly |
| **MAE / R²** | Average absolute error / the fraction of variance explained |
| **overfitting** | Memorizing the training data instead of learning general patterns |
| **data leakage** | Information from the test set (or the future) sneaking into training |

## Exercises → [`exercises/`](exercises/)

| # | Exercise | Practices |
|---|----------|-----------|
| 1 | Build your own k-NN (8 functions, auto-checked) | distance, voting, splitting, scaling, accuracy on a wheat-seeds dataset |
| 2 | Linear regression from scratch (6 functions) | fitting, MAE, R², correlation |
| 3 | scikit-learn in practice (notebook) | breast cancer diagnosis: baseline, scaling, choosing k, confusion matrix, overfitting; penguin regression |

## 📘 Gradebook Project, Milestone 8
Predict final exam scores from the midterm and homework, beat a baseline, find who "beat the prediction," and **save the model** for next week's web app.
→ [gradebook-project/m8-prediction](../gradebook-project/m8-prediction/)

## Videos and reading
1. But what is a neural network? (3Blue1Brown, a peek at where ML goes next): https://www.youtube.com/watch?v=aircAruvnKk
2. k-NN explained (StatQuest): https://www.youtube.com/watch?v=HVXime0nQeI
3. Linear regression, clearly explained (StatQuest): https://www.youtube.com/watch?v=7ArmBVF2dCs
4. scikit-learn "Getting Started": https://scikit-learn.org/stable/getting_started.html
5. Machine learning fundamentals: bias and variance (StatQuest): https://www.youtube.com/watch?v=EuBBz3bI-aA

**Next week (after Thanksgiving, 12/5):** we put the gradebook and its model on the web with FastAPI!
