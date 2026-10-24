# Day 1, Part 0: What is Programming? Where did Python come from?

*These notes are for the first ~30 minutes of Day 1, before we write any code.*

---

## 1. What is a program?

A **program** is a list of precise instructions that a computer follows, step by step.

Computers are extremely fast, but they are also extremely literal. They do *exactly* what you say, not what you *meant*. Much of learning to program is learning to say exactly what you mean.

> **Analogy: a recipe.** A recipe has ingredients (**data**) and steps (**instructions**). Some steps depend on conditions ("if the dough is sticky, add flour", which is a **conditional**). Some steps repeat ("stir until smooth", which is a **loop**). And some steps refer to other recipes ("make the frosting from page 12", which is a **function**). By Day 2 you'll know all four of these ideas in Python.

**An algorithm** is a step-by-step method for solving a problem. **A program** is an algorithm written in a language a computer can run.

---

## 2. How do computers actually run code?

Deep down, a computer's processor (the **CPU**) only understands **machine code**: long sequences of 1s and 0s that mean things like "add these two numbers" or "jump to this instruction."

Nobody wants to write programs as 1s and 0s, so over time people built layers of more human-friendly languages on top of machine code:

| Level | Example | Who reads it |
|-------|---------|--------------|
| **Machine code** | `10110000 01100001` | The CPU, directly |
| **Assembly** | `MOV AL, 61h` | Humans (barely); each line maps to one machine instruction |
| **High-level language** | `total = price * quantity` | Humans; a tool translates it for the CPU |

Python is a **high-level language**. You write something readable, and software translates it into something the CPU can run.

### Compiled vs interpreted

There are two main ways to do that translation:

- **Compiled** languages (C, C++, Rust, Go) are translated *all at once* into machine code before the program runs. The result is fast, but you have to compile again every time you change the code.
- **Interpreted** languages (Python, JavaScript, Ruby) are run by another program, the **interpreter**, which reads your code and carries it out as it goes. This is slower, but you can write a line and run it immediately.

**What actually happens when you run a Python file:**
1. The standard Python interpreter (called **CPython**, because it is written in C) reads your `.py` file.
2. It compiles your code into **bytecode**, a simpler set of instructions.
3. The **Python Virtual Machine** runs that bytecode one instruction at a time.

That's why you never have to "build" a Python program. You just press Run.

---

## 3. A (very) short history of programming languages

| Year | Milestone |
|------|-----------|
| 1843 | **Ada Lovelace** writes what's considered the first algorithm meant for a machine (Babbage's Analytical Engine) |
| 1940s | Early electronic computers are programmed by flipping switches and rewiring, then with machine code |
| 1957 | **FORTRAN** (IBM, led by John Backus), the first widely used high-level language, built for science and engineering |
| 1959 | **COBOL**, a business language shaped by **Grace Hopper**'s work on compilers |
| 1972 | **C** (Dennis Ritchie, Bell Labs). Operating systems and CPython itself are written in C |
| 1985 | **C++** adds "objects" to C |
| **1991** | **Python** is first released |
| 1995 | **Java** and **JavaScript** |
| 2010s | Newer languages like **Go**, **Rust**, and **Swift** |

Every language makes **trade-offs**: speed vs ease of writing, safety vs flexibility, and so on. There is no "best" language, only good fits for particular jobs.

---

## 4. The story of Python

- **December 1989:** **Guido van Rossum**, a programmer at the research institute CWI in Amsterdam, starts a hobby project over his Christmas break. He wants a language that is as easy to read as the teaching language **ABC** but practical enough for real work.
- **The name:** it comes from the British comedy show **Monty Python's Flying Circus**, not the snake. (Python documentation is full of Monty Python jokes, like using `spam` and `eggs` as example variable names.)
- **February 1991:** Python 0.9.0 is released to the public.
- **1994:** Python 1.0.
- **2000:** Python 2.0 adds features like list comprehensions (you'll learn these on Day 5).
- **2001:** The **Python Software Foundation (PSF)**, a non-profit, is created to manage Python. Python is **open source**: anyone can read, use, and help improve its code.
- **2008:** **Python 3.0** fixes old design mistakes but is *not backward compatible*, so Python 2 code doesn't always run in Python 3. (For example, `print "hi"` became `print("hi")`.) The migration took over a decade.
- **January 1, 2020:** Python 2 officially reaches end of life. **We use Python 3.**
- **2018:** Guido steps down as Python's "Benevolent Dictator For Life." Since 2019, an elected **Steering Council** guides the language.
- **Today:** a new version comes out every October (3.14 was released in October 2025). Python is one of the most popular programming languages in the world.

### How Python changes: PEPs
New features are proposed in **PEPs (Python Enhancement Proposals)**. Two famous ones:
- **PEP 8**, the style guide ("how Python code should look").
- **PEP 20**, *The Zen of Python*, a short poem about Python's design philosophy. Run `import this` to see it (we'll do it in `01_hello_world.py`). Some favorite lines:
  - *Beautiful is better than ugly.*
  - *Simple is better than complex.*
  - *Readability counts.*
  - *Errors should never pass silently.*

---

## 5. Why learn Python?

- **Readable.** Python code looks close to plain English, so you spend your energy on *problem solving* instead of fighting syntax.
- **Batteries included.** It has a huge built-in library for math, randomness, files, dates, and more.
- **An enormous ecosystem.** There are free libraries for nearly everything:
  - **Data science and AI:** NumPy, pandas, scikit-learn, PyTorch (Days 7–9)
  - **Web development:** FastAPI, Django, Flask (Day 10)
  - **Games and graphics:** pygame (Day 11)
  - **Science:** astronomy, biology, physics, and chemistry all use Python heavily
- **Used everywhere.** Examples include research labs, Instagram, YouTube, NASA and JPL, the tools used to create the first image of a black hole, and much of modern AI.

The trade-off: Python is **slower** than C or Rust. For most tasks that doesn't matter, and when it does, libraries like NumPy run fast C code behind the scenes (we'll measure this on Day 7).

---

## 6. How we'll write Python in this course

- **Thonny** (Days 1–6) is a simple editor with Python built in. See [SETUP.md](../SETUP.md).
- **Jupyter notebooks** (Days 7–9) mix code, text, and charts. Scientists use them a lot.
- **Scripts + terminal** (Days 10–11) are for running web servers and games.

Two ways to run Python code:
1. **The shell / REPL** (Read–Evaluate–Print Loop), marked by the `>>>` prompt. You type one line and see the result immediately. Great for experiments.
2. **Scripts** are `.py` files that run top to bottom. This is where real programs live.

---

## 7. Tips for learning to program

1. **Type the code yourself.** Don't just copy and paste; your fingers learn too.
2. **Predict, then run.** Before you press Run, guess what will happen. When you're wrong, you learn the most.
3. **Break things on purpose.** Delete a quote or misspell a name and read the error. Errors are clues, not failures.
4. **Small steps.** Write 2–3 lines, run, check. Repeat.
5. **Ask for help.** Email mfd2141@columbia.edu. Getting stuck is normal, even for professionals.

---

## Key terms

| Term | Meaning |
|------|---------|
| **program** | A precise list of instructions for a computer |
| **algorithm** | A step-by-step method for solving a problem |
| **CPU** | The processor that executes machine code |
| **machine code** | Binary instructions the CPU runs directly |
| **high-level language** | A human-readable language translated for the CPU (Python, Java, C...) |
| **compiler** | Translates a whole program to machine code *before* running it |
| **interpreter** | Runs a program by reading and executing it as it goes |
| **CPython** | The standard Python interpreter, written in C |
| **bytecode** | The intermediate instructions CPython compiles your code into |
| **open source** | Software whose source code anyone can read, use, and improve |
| **PEP** | Python Enhancement Proposal: how new Python features are designed |
| **REPL / shell** | Interactive prompt (`>>>`) that runs one line at a time |
| **script** | A saved `.py` file that runs top to bottom |
