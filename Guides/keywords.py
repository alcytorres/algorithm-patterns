# Python Keywords Cheat Sheet
# Reserved words with special meaning — cannot be used as variable names.

"""
Ranked by frequency in real code (most → least common).

  Rank  Keyword(s)             Category
  ----  --------------------   ----------------
   1    if, elif, else         Conditionals
   2    def, return            Functions
   3    for, in                Loops
   4    import, from, as       Imports
   5    and, or, not           Logic
   6    True, False, None      Values
   7    class                  Classes
   8    while                  Loops
   9    try, except            Error Handling
  10    with                   Context Manager
  11    break, continue, pass  Loop Control
  12    is                     Identity
  13    raise, finally         Error Handling
  14    del                    Deletion
  15    global, nonlocal       Scope
  16    yield                  Generators
  17    lambda                 Anonymous Func
  18    assert                 Debugging
"""


# ======================================================================
# 1. Conditionals — if, elif, else

x = 10

if x > 10:
    print("big")
elif x == 10:
    print("ten")      # → "ten"
else:
    print("small")

# Rule: only ONE branch runs — the first True condition wins.


# ======================================================================
# 2. Functions — def, return

def add(a, b):
    return a + b      # stops the function, sends back the value

result = add(3, 4)    # → 7

# return with no value → returns None
# no return at all    → also returns None


# ======================================================================
# 3. Loops — for, in

nums = [1, 2, 3]

for num in nums:      # in  →  iterates over any iterable
    print(num)        # → 1, 2, 3

# Works on: list, string, dict, set, range, tuple
for ch in "abc":
    print(ch)         # → a, b, c


# ======================================================================
# 4. Imports — import, from, as

import math                        # full module
from math import sqrt              # specific name
import collections as col          # alias

print(math.pi)                     # → 3.14159…
print(sqrt(9))                     # → 3.0
print(col.defaultdict)


# ======================================================================
# 5. Logic — and, or, not

# and  → True if BOTH sides are True
# or   → True if AT LEAST ONE side is True
# not  → flips True ↔ False

print(True and False)   # → False
print(True or False)    # → True
print(not True)         # → False

# Short-circuit: and stops at first False, or stops at first True
x = None
if x is not None and x > 0:   # safe — won't evaluate x > 0 if x is None
    print(x)


# ======================================================================
# 6. Built-in Values — True, False, None

flag = True
empty = None

if empty is None:       # always use  is  to check None (not ==)
    print("nothing")    # → "nothing"

# None  →  absence of a value (like null in other languages)
# False →  boolean false
# True  →  boolean true


# ======================================================================
# 7. Classes — class

class Dog:
    def __init__(self, name):   # constructor
        self.name = name

    def bark(self):
        return f"{self.name} says woof"

d = Dog("Rex")
print(d.bark())     # → "Rex says woof"


# ======================================================================
# 8. While Loop — while

count = 0
while count < 3:
    print(count)    # → 0, 1, 2
    count += 1

# Use while when you don't know how many iterations upfront.
# for  →  iterate over a collection
# while→  repeat until a condition is False


# ======================================================================
# 9. Error Handling — try, except, raise, finally

try:
    x = 1 / 0
except ZeroDivisionError:
    print("can't divide by zero")   # → runs this
finally:
    print("always runs")            # → always runs

# raise  →  manually trigger an error
def check(n):
    if n < 0:
        raise ValueError("must be positive")


# ======================================================================
# 10. Context Manager — with

with open("file.txt", "w") as f:    # auto-closes file when block ends
    f.write("hello")

# with  guarantees cleanup (close, release) even if an error occurs.
# Most common use: files, locks, database connections.


# ======================================================================
# 11. Loop Control — break, continue, pass

for i in range(5):
    if i == 3:
        break           # stops the loop entirely → exits at 3
    print(i)            # → 0, 1, 2

for i in range(5):
    if i == 2:
        continue        # skips rest of THIS iteration → skips 2
    print(i)            # → 0, 1, 3, 4

def todo():
    pass                # placeholder — does nothing, avoids syntax error

#  break     →  exit loop now
#  continue  →  skip to next iteration
#  pass      →  do nothing (placeholder)


# ======================================================================
# 12. Identity — is

x = None

if x is None:       # checks if same object in memory (not just equal value)
    print("null")

# is      →  same object?   (use for None, True, False)
# ==      →  same value?    (use for everything else)

a = [1, 2]
b = [1, 2]
print(a == b)       # → True   (same value)
print(a is b)       # → False  (different objects)


# ======================================================================
# 13. Deletion — del

nums = [1, 2, 3]
del nums[0]         # removes element at index 0
print(nums)         # → [2, 3]

d = {"a": 1, "b": 2}
del d["a"]          # removes key "a"
print(d)            # → {"b": 2}

# del also works on variables: del x  (removes the variable entirely)


# ======================================================================
# 14. Scope — global, nonlocal

count = 0

def increment():
    global count        # modify the variable in global scope
    count += 1

increment()
print(count)            # → 1


def outer():
    x = 10
    def inner():
        nonlocal x      # modify x in the enclosing (outer) scope
        x += 1
    inner()
    print(x)            # → 11

outer()

# global   →  reach module-level variable from inside a function
# nonlocal →  reach enclosing function's variable from nested function


# ======================================================================
# 15. Generators — yield

def countdown(n):
    while n > 0:
        yield n         # pauses here, returns n, resumes on next call
        n -= 1

for val in countdown(3):
    print(val)          # → 3, 2, 1

# yield turns a function into a generator — lazy, memory-efficient.
# Use when producing a sequence you don't need all at once.


# ======================================================================
# 16. Anonymous Functions — lambda

double = lambda x: x * 2
print(double(5))        # → 10

nums = [3, 1, 2]
nums.sort(key=lambda x: -x)
print(nums)             # → [3, 2, 1]

# lambda  →  one-line function, one expression, no return statement needed
# Best for short callbacks (sort key, map, filter) — not complex logic


# ======================================================================
# 17. Assertions — assert

def divide(a, b):
    assert b != 0, "b must not be zero"   # raises AssertionError if False
    return a / b

# assert  →  sanity check during development / testing
# Disabled in production when Python runs with -O flag — don't rely on for security


# ======================================================================
# Quick Reference — Gotchas

"""
  Keyword       Common Mistake                  Correct Usage
  ----------    ----------------------------    -------------------------
  is            x is 5   (for values)           x == 5
  is            x is None                       ✓ correct for None
  not in        not x in lst  (works but ugly)  x not in lst
  pass          forgetting it in empty block    def f(): pass
  global        overusing it (code smell)       prefer returning values
  break         breaking outer loop             use a flag or function
  return        forgetting → returns None       explicit return when needed
"""
