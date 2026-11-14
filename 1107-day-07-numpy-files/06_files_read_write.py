"""
06 - Reading and Writing Text Files
Variables disappear when a program ends. FILES let data survive.

    with open(path, mode) as f:
        ...                      # the file closes automatically after this block

Modes: "r" read (default), "w" write (ERASES the file first!), "a" append
"""

import os

# Paths are relative to the folder you RUN the program from.
# This line makes paths relative to THIS FILE's folder instead, so it works from anywhere:
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("output", exist_ok=True)          # make an output/ folder if needed

# ---- Write ----
with open("output/hello.txt", "w") as f:
    f.write("Hello, file!\n")                # write() does NOT add a newline for you
    f.write("Second line\n")
    for i in range(1, 4):
        f.write(f"{i} squared is {i * i}\n")

# ---- Read the whole file as one string ----
with open("output/hello.txt") as f:
    content = f.read()
print(content)

# ---- Read line by line (best for big files) ----
with open("output/hello.txt") as f:
    for line in f:
        print(repr(line))                    # repr shows the hidden \n at the end
print()

# ---- .strip() removes that \n ----
with open("output/hello.txt") as f:
    lines = [line.strip() for line in f]
print(lines)

# ---- Append ----
with open("output/hello.txt", "a") as f:
    f.write("Appended at the end!\n")

print()

# ---- A real example: analyze a poem ----
with open("data/poem.txt") as f:
    text = f.read()

words = text.lower().split()
cleaned = [w.strip('.,;:!?-"\'') for w in words]
cleaned = [w for w in cleaned if w]          # drop empty strings
print("Lines:", text.count("\n"), " Words:", len(cleaned), " Unique:", len(set(cleaned)))

counts = {}
for w in cleaned:
    counts[w] = counts.get(w, 0) + 1
top = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:5]
print("Most common:", top)

# ---- Errors: what if the file doesn't exist? ----
try:
    with open("data/missing.txt") as f:
        f.read()
except FileNotFoundError:
    print("Couldn't find data/missing.txt")
