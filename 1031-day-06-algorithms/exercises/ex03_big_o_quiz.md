# Exercise 3: Big-O Quiz

For each snippet, give the Big-O running time in terms of `n` (the length of `nums`, or the number `n`) and **explain why in one sentence**. Answers are in [`solutions/ex03_big_o_quiz_answers.md`](solutions/ex03_big_o_quiz_answers.md).

**1.**
```python
def first(nums):
    return nums[0]
```

**2.**
```python
def total(nums):
    t = 0
    for x in nums:
        t += x
    return t
```

**3.**
```python
def total_and_max(nums):
    t = 0
    for x in nums:
        t += x
    m = nums[0]
    for x in nums:
        if x > m:
            m = x
    return t, m
```

**4.**
```python
def pairs(nums):
    for a in nums:
        for b in nums:
            print(a, b)
```

**5.**
```python
def halve(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
```

**6.**
```python
def first_ten(nums):
    for i in range(10):
        print(nums[i])
```

**7.**
```python
def triples(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                print(a + b + c)
```

**8.**
```python
def contains_any(nums, targets):     # assume len(targets) is also n
    for t in targets:
        if t in nums:                # nums is a LIST
            return True
    return False
```

**9.** Same as #8, but first do `nums = set(nums)`. (Converting a list to a set is O(n).)

**10.**
```python
def mystery(n):
    for i in range(n):
        j = 1
        while j < n:
            j = j * 2
```

**11.** Rank these from fastest-growing to slowest-growing:
`O(n²)`, `O(1)`, `O(n log n)`, `O(2ⁿ)`, `O(log n)`, `O(n)`

**12.** An algorithm takes 1 second for n = 1,000. Roughly how long for n = 2,000 if it is:
(a) O(n)? (b) O(n²)? (c) O(log n)?
