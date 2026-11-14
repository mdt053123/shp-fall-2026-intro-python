"""
Exercise 2 - Linear Regression From Scratch  (SOLUTION)
-------------------------------------------
Build a simple linear regression toolkit, then use it to answer:
  "How well does the number of hours studied predict a test score?"
"""


def mean(values):
    """mean([1, 2, 3, 4]) -> 2.5"""
    return sum(values) / len(values)


def fit_line(xs, ys):
    """Return (m, b) for the least-squares line y = m*x + b.
        m = sum((x - x_mean)(y - y_mean)) / sum((x - x_mean)^2)
        b = y_mean - m * x_mean
    fit_line([1, 2, 3], [2, 4, 6]) -> (2.0, 0.0)
    """
    x_bar, y_bar = mean(xs), mean(ys)
    m = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys)) / sum((x - x_bar) ** 2 for x in xs)
    return m, y_bar - m * x_bar


def predict_all(m, b, xs):
    """Return a list of predictions m*x + b for every x."""
    return [m * x + b for x in xs]


def mean_absolute_error(ys, preds):
    """Average of |y - prediction|.   mean_absolute_error([1, 2], [2, 4]) -> 1.5"""
    return mean([abs(y - p) for y, p in zip(ys, preds)])


def r_squared(ys, preds):
    """1 - sum((y - pred)^2) / sum((y - y_mean)^2)"""
    y_bar = mean(ys)
    return 1 - sum((y - p) ** 2 for y, p in zip(ys, preds)) / sum((y - y_bar) ** 2 for y in ys)


def correlation(xs, ys):
    """Pearson correlation coefficient r (between -1 and 1):
        r = sum((x - x_mean)(y - y_mean)) / sqrt( sum((x - x_mean)^2) * sum((y - y_mean)^2) )
    Fun fact: for simple linear regression, R^2 == r^2 !"""
    x_bar, y_bar = mean(xs), mean(ys)
    num = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
    den = (sum((x - x_bar) ** 2 for x in xs) * sum((y - y_bar) ** 2 for y in ys)) ** 0.5
    return num / den


# ----------------------- Checks (don't change below) -----------------------
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


hours = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
scores = [52, 55, 61, 64, 68, 71, 75, 80, 84, 90]

check("mean", lambda: mean([1, 2, 3, 4]), 2.5)
check("fit_line perfect", lambda: fit_line([1, 2, 3], [2, 4, 6]), (2.0, 0.0))
check("predict_all", lambda: predict_all(2, 1, [0, 1, 2]), [1, 3, 5])
check("mean_absolute_error", lambda: mean_absolute_error([1, 2], [2, 4]), 1.5)
check("r_squared perfect", lambda: r_squared([1, 2, 3], [1, 2, 3]), 1.0)
check("r_squared = correlation^2",
      lambda: round(r_squared(scores, predict_all(*fit_line(hours, scores), hours)), 6) == round(correlation(hours, scores) ** 2, 6),
      True)

try:
    m, b = fit_line(hours, scores)
    print(f"\nscore = {m:.2f} * hours + {b:.2f}")
    print(f"Each extra hour of studying is worth about {m:.1f} points.")
    print(f"Predicted score for 10 hours: {m * 10 + b:.1f}")
    print(f"R^2 = {r_squared(scores, predict_all(m, b, hours)):.3f}, correlation = {correlation(hours, scores):.3f}")
    print("(Careful: 20 hours would predict", round(m * 20 + b), "-- over 100! Lines don't know when to stop.)")
except Exception:
    print("\nFinish the functions to see the study-hours results.")
