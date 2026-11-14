# Day 8 (Sat 11/14): Data Analysis with pandas and matplotlib

**Big idea:** Turn raw data into answers and pictures. **pandas** gives us spreadsheet-style tables (DataFrames) that we can filter, group, and summarize. **matplotlib** turns them into charts. We practice on two real datasets: **Antarctic penguins** 🐧 and **five years of stock prices** 📈.

Today is all in **Jupyter notebooks** (see Day 7). Open them with `python -m jupyter lab`, or upload them to Google Colab.

## Learning goals
- [ ] Load a CSV into a DataFrame and explore it (`head`, `shape`, `info`, `describe`, `isna`)
- [ ] Select columns, filter rows with boolean masks (`&`, `|`), and sort
- [ ] Count categories (`value_counts`), handle missing data, and create new columns (including with `.apply`)
- [ ] Summarize by group with `groupby` (split → apply → combine)
- [ ] Choose and make the right chart: line, scatter, bar, histogram, subplots
- [ ] Work with time series: date indexes, `pct_change`, `rolling`, normalizing
- [ ] Explain volatility, correlation, and why comparing raw prices is misleading

## Class schedule (~2.5 hrs)

| Time | Topic | Files |
|------|-------|-------|
| 0:00 | Warm-up: Day 7 review (NumPy masks, CSV), check in on M6 | |
| 0:15 | pandas basics with penguins | `01_pandas_basics.ipynb` |
| 1:00 | matplotlib: picking and making charts | `02_matplotlib.ipynb` |
| 1:25 | *Break* | |
| 1:35 | Stock market analysis | `03_stock_analysis.ipynb` |
| 2:15 | Exercises / Gradebook M7 | `exercises/`, [project](../gradebook-project/m7-analysis/) |

---

## Lecture notes

### 1. DataFrames (`01_pandas_basics.ipynb`)
A **DataFrame** is a table: rows plus named columns. Each column is a **Series**, which works like a NumPy array with labels.

```python
import pandas as pd
df = pd.read_csv("data/penguins.csv")
df.head(); df.shape; df.info(); df.describe(); df.isna().sum()

df["body_mass_g"]                           # one column -> Series
df[["species", "island"]]                   # several columns -> DataFrame (double brackets!)
df[df["body_mass_g"] > 5000]                # filter rows
df[(df["species"] == "Gentoo") & (df["sex"] == "MALE")]   # & | ~, with parentheses!
df.sort_values("body_mass_g", ascending=False)
df["species"].value_counts()
df["kg"] = df["body_mass_g"] / 1000         # new column (vectorized)
df["size"] = df["body_mass_g"].apply(lambda g: "big" if g > 4500 else "small")
df.groupby("species")["body_mass_g"].mean()  # average per group
df.dropna(); df.to_csv("out.csv")
```

**`loc` vs `iloc`:** `df.iloc[0]` selects by **position**. `df.loc[label, "col"]` selects by **label**.

### 2. Charts (`02_matplotlib.ipynb`)

| Question | Chart | Code |
|----------|-------|------|
| Change over time? | line | `plt.plot(x, y)` |
| Two variables related? | scatter | `plt.scatter(x, y)` |
| Compare categories? | bar | `plt.bar(labels, values)` |
| How are values spread? | histogram | `plt.hist(values, bins=20)` |

Every chart needs a **title**, **axis labels with units**, and a **legend** if there are several groups. Use `plt.subplots(1, 3)` for side-by-side charts, and `df.plot(kind=...)` as a shortcut.

### 3. Time series and stocks (`03_stock_analysis.ipynb`)
```python
aapl = pd.read_csv("data/AAPL.csv", parse_dates=["Date"], index_col="Date")
aapl.loc["2025-04"]                         # select by date
aapl["Close"].pct_change()                  # daily returns
aapl["Close"].rolling(50).mean()            # 50-day moving average
closes / closes.iloc[0] * 100               # normalize to "start = 100"
returns.std() * np.sqrt(252)                # annualized volatility
returns.corr()                              # correlation matrix
```
**Lessons from the data:**
- Most days are small moves, but a few days are huge (April 2025).
- Higher returns usually come with higher volatility.
- Stocks tend to move together.
- ⚠️ Not financial advice!

---

## Common mistakes
- `df["a", "b"]` instead of `df[["a", "b"]]`.
- Writing `and`/`or` instead of `&`/`|` in filters, or forgetting the parentheses: `(df.a > 1) & (df.b < 2)`.
- Forgetting that most methods return a **new** DataFrame. `df.dropna()` alone doesn't change `df`.
- `SettingWithCopyWarning`: use `.copy()` when you filter a DataFrame and then add columns to it.
- Charts with no labels. Always label!
- Comparing raw prices of different stocks instead of normalizing them.

## Key terms

| Term | Meaning |
|------|---------|
| **DataFrame / Series** | pandas' table / a single labeled column |
| **index** | The row labels (numbers, or dates for a time series) |
| **boolean mask** | A True/False Series used to filter rows |
| **groupby** | Split into groups → apply a function → combine the results |
| **missing value (NaN)** | "Not a Number": a missing entry |
| **time series** | Data indexed by time |
| **return** | Percentage change in price |
| **moving average** | The average of the last *n* values, recomputed every day |
| **volatility** | Standard deviation of returns: how "bumpy" the ride is |
| **correlation** | How strongly two variables move together (−1 to +1) |

## Exercises → [`exercises/exercises.ipynb`](exercises/exercises.ipynb)
There are 14 questions: 8 on penguins (grouping, filtering, fractions, charts) and 6 on stocks (yearly returns, big-move days, 2024 comparison, max drawdown, volume by weekday). Solutions: [`exercises/solutions/solutions.ipynb`](exercises/solutions/solutions.ipynb).

## 📘 Gradebook Project, Milestone 7
Analyze the 60-student class: weighted grades, letter distribution, the hardest assignment, missed homework, top 10, a histogram with cutoffs, and midterm vs final correlation.
→ [gradebook-project/m7-analysis](../gradebook-project/m7-analysis/)

## Data sources
- `data/penguins.csv`: Palmer Penguins (Gorman, Williams and Fraser, 2014; CC0), via the seaborn-data repository
- `data/{AAPL,MSFT,NVDA,KO,SPY}.csv`: daily adjusted prices from Yahoo Finance, 2021-09-01 to 2026-08-31

## Videos and reading
1. 10 minutes to pandas (official): https://pandas.pydata.org/docs/user_guide/10min.html
2. pandas tutorial series, part 1: https://www.youtube.com/watch?v=ZyhVh-qRZPA
3. matplotlib tutorial, part 1: https://www.youtube.com/watch?v=UO98lJQ3QGI
4. matplotlib quick start (official): https://matplotlib.org/stable/users/explain/quick_start.html
