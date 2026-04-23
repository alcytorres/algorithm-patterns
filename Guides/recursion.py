# Recursion — A First-Principles Guide for Beginners
# Style: heavy comments, plain English, trace-through clarity over theory.
# Goal: by the end, you can read a tiny recursive function and follow it in your head.

# Read this guide top to bottom. Each section builds on the one before it.


# ======================================================================
# 1. What Is Recursion?
# ======================================================================
#
# Real-world analogy: Russian nesting dolls.
#   • You open a doll. Inside is a smaller doll.
#   • You open that one. Inside is an even smaller doll.
#   • You keep going until you reach the tiniest doll that has nothing inside.
#   • Then you close them back up, one by one, in reverse order.
#
# Recursion is the same idea in code:
#   A function that calls ITSELF on a smaller version of the problem,
#   until the problem is so small there's nothing left to do.
#
# One-sentence definition:
#   "Recursion = a function that solves a problem by calling itself
#    on a slightly smaller piece of that same problem."
#
# That's it. The rest of this guide just teaches you how to do it
# without getting lost in your own head.


# ======================================================================
# 2. The Two Parts Every Recursive Function Needs
# ======================================================================
#
# Every recursive function has exactly TWO parts. Memorize these names —
# they will appear over and over.
#
#   1) BASE CASE
#      The "stop" condition. The smallest, simplest version of the
#      problem that you can answer immediately, with no more recursion.
#      Without a base case, the function calls itself FOREVER. That's bad.
#
#   2) RECURSIVE CASE
#      The "shrink and call again" part. You make the problem a little
#      smaller, then call the same function on that smaller piece.
#
# 🔑 NAMED RULE — "The Base Case Rule":
#    Every recursive function MUST have a base case.
#    No base case = infinite recursion = your program crashes.
#
# 🔑 NAMED RULE — "The Shrink Rule":
#    Every recursive call MUST move you closer to the base case.
#    If the problem doesn't get smaller, you'll never stop.


# ======================================================================
# 3. The Call Stack — What Actually Happens (Visual Trace)
# ======================================================================
#
# When a function calls another function (even itself), Python "pauses"
# the current function and starts the new one. The paused function waits
# on a pile called the CALL STACK.
#
# Think of a stack of plates:
#   • Each function call adds a plate on top.
#   • When a function finishes (returns), its plate is removed.
#   • The function below it picks up where it left off.
#
# Tiny visual for a function f() that calls itself 3 times:
#
#     Call f(3)
#       │
#       ├── pauses, calls f(2)
#       │       │
#       │       ├── pauses, calls f(1)
#       │       │       │
#       │       │       └── base case! returns a value
#       │       │
#       │       └── resumes with f(1)'s return value, then returns
#       │
#       └── resumes with f(2)'s return value, then returns
#
# Two phases happen:
#   • GOING DOWN: each call adds a "plate" to the stack.
#   • COMING BACK UP: each call returns and is removed from the stack.
#
# This "going down then coming back up" is THE thing to picture in your
# head every time you read a recursive function.


# ======================================================================
# 4. The 3-Step Recipe for Writing Any Recursive Function
# ======================================================================
#
# When writing a recursive function, ALWAYS ask yourself these 3 things,
# in this exact order. We'll use this recipe in every example below.
#
#   STEP 1 — Base case:    "When do I stop?"
#   STEP 2 — Recursive case:"How do I shrink the problem by one step?"
#   STEP 3 — Combine:       "What do I return / combine from the smaller answer?"
#
# 🔑 NAMED RULE — "The 3-Step Recipe":
#    1) Stop.   2) Shrink.   3) Combine.
#
# If you can answer all three for a problem, you can write the recursion.


# ======================================================================
# 5. Tiny Example #1 — countdown(n)
# ======================================================================
#
# Goal: print numbers from n down to 0.
#
# Apply the 3-Step Recipe:
#   1) Stop:    when n < 0, do nothing.
#   2) Shrink:  print n, then call countdown(n - 1).
#   3) Combine: nothing to return — we're just printing.

def countdown(n):
    if n < 0:               # STEP 1 — base case (the "stop")
        return
    print(n)                # STEP 2a — do the work for THIS step
    countdown(n - 1)        # STEP 2b — shrink and call again

countdown(3)
# → 3
# → 2
# → 1
# → 0

# Step-by-step trace (read top to bottom):
#
#   countdown(3)
#     prints 3
#     → countdown(2)
#         prints 2
#         → countdown(1)
#             prints 1
#             → countdown(0)
#                 prints 0
#                 → countdown(-1)   ← base case hit, returns nothing
#                 ← returns
#             ← returns
#         ← returns
#     ← returns
#
# Notice the two phases:
#   • Going down: each call prints, then calls a smaller one.
#   • Coming back up: each call simply finishes (nothing to combine here).


# ======================================================================
# 6. Tiny Example #2 — sum_to_n(n)
# ======================================================================
#
# Goal: return the sum 1 + 2 + 3 + ... + n.
#
# Apply the 3-Step Recipe:
#   1) Stop:    if n == 0, the sum is 0. Return 0.
#   2) Shrink:  ask for the sum up to (n - 1).
#   3) Combine: add n to whatever the smaller call returned.

def sum_to_n(n):
    if n == 0:                      # STEP 1 — base case
        return 0
    return n + sum_to_n(n - 1)      # STEP 2 + STEP 3 — shrink + combine

print(sum_to_n(4))   # → 10   (because 4 + 3 + 2 + 1 + 0 = 10)

# Step-by-step trace:
#
#   sum_to_n(4)
#     returns 4 + sum_to_n(3)
#       sum_to_n(3)
#         returns 3 + sum_to_n(2)
#           sum_to_n(2)
#             returns 2 + sum_to_n(1)
#               sum_to_n(1)
#                 returns 1 + sum_to_n(0)
#                   sum_to_n(0)
#                     returns 0      ← base case
#                 returns 1 + 0 = 1
#               returns 2 + 1 = 3
#           returns 3 + 3 = 6
#         returns 4 + 6 = 10
#     final answer: 10
#
# Key insight:
#   On the way DOWN, nothing is computed yet — each call is "waiting"
#   for its smaller call to return a number.
#   On the way UP, the actual addition happens.


# ======================================================================
# 7. Tiny Example #3 — factorial(n)
# ======================================================================
#
# Factorial of n means: n * (n-1) * (n-2) * ... * 1.
# Example: factorial(4) = 4 * 3 * 2 * 1 = 24.
#
# Apply the 3-Step Recipe:
#   1) Stop:    factorial(0) = 1.   (math says so — just memorize it)
#   2) Shrink:  ask for factorial(n - 1).
#   3) Combine: multiply n by whatever the smaller call returned.

def factorial(n):
    if n == 0:                       # STEP 1 — base case
        return 1
    return n * factorial(n - 1)      # STEP 2 + STEP 3 — shrink + combine

print(factorial(4))   # → 24

# Step-by-step trace:
#
#   factorial(4)
#     returns 4 * factorial(3)
#       factorial(3)
#         returns 3 * factorial(2)
#           factorial(2)
#             returns 2 * factorial(1)
#               factorial(1)
#                 returns 1 * factorial(0)
#                   factorial(0)
#                     returns 1      ← base case
#                 returns 1 * 1 = 1
#               returns 2 * 1 = 2
#           returns 3 * 2 = 6
#         returns 4 * 6 = 24
#     final answer: 24
#
# Same shape as sum_to_n! Only difference: we MULTIPLY instead of ADD.
# Most simple recursion looks the same — only the "combine" step changes.


# ======================================================================
# 8. Tiny Example #4 — reverse_string(s)
# ======================================================================
#
# Goal: take a string like "cat" and return "tac".
#
# Apply the 3-Step Recipe:
#   1) Stop:    if the string is empty (""), return "".
#               An empty string reversed is still an empty string.
#   2) Shrink:  reverse the string MINUS its first character (s[1:]).
#   3) Combine: stick the first character (s[0]) on the END of that result.

def reverse_string(s):
    if s == "":                              # STEP 1 — base case
        return ""
    return reverse_string(s[1:]) + s[0]      # STEP 2 + STEP 3

print(reverse_string("cat"))   # → tac

# Step-by-step trace:
#
#   reverse_string("cat")
#     returns reverse_string("at") + "c"
#       reverse_string("at")
#         returns reverse_string("t") + "a"
#           reverse_string("t")
#             returns reverse_string("") + "t"
#               reverse_string("")
#                 returns ""              ← base case
#             returns "" + "t" = "t"
#           returns "t" + "a" = "ta"
#       returns "ta" + "c" = "tac"
#     final answer: "tac"
#
# Important pattern to notice:
#   The "first character" is glued onto the END after the smaller piece
#   has been fully reversed. That's why the order flips.


# ======================================================================
# 9. Slightly Bigger — fibonacci(n)
# ======================================================================
#
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each number = the sum of the two before it.
# So: fib(n) = fib(n - 1) + fib(n - 2).
#
# Apply the 3-Step Recipe:
#   1) Stop:    fib(0) = 0, fib(1) = 1. Two base cases this time.
#   2) Shrink:  call fib(n - 1) AND fib(n - 2).
#   3) Combine: add their results.

def fibonacci(n):
    if n == 0:                           # STEP 1 — base case A
        return 0
    if n == 1:                           # STEP 1 — base case B
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   # STEP 2 + STEP 3

print(fibonacci(6))   # → 8
# Sequence check: 0, 1, 1, 2, 3, 5, 8  → index 6 is 8. ✓

# Why is this slow?
#   Each call splits into TWO more calls. So fib(6) calls fib(5) AND fib(4),
#   and fib(5) calls fib(4) AND fib(3) — and we end up recomputing the
#   same little answers over and over.
#
#   For small n it's fine. For n = 40+, it gets noticeably slow.
#   (There's a fix called "memoization" — saving past answers — but
#    that's a topic for later. Just be aware this naive version is slow.)


# ======================================================================
# 10. Common Beginner Mistakes
# ======================================================================
#
# ❌ MISTAKE 1 — Forgetting the base case.
#    Without it, the function calls itself forever and Python crashes
#    with: "RecursionError: maximum recursion depth exceeded".
#
#    Bad:
#       def bad_countdown(n):
#           print(n)
#           bad_countdown(n - 1)   # never stops!
#
#    Fix: add an `if` at the top that returns when n is small enough.
#
# ❌ MISTAKE 2 — Forgetting to RETURN the recursive call.
#    If a function should hand back a value, you must `return` the
#    smaller call's result. Otherwise the function returns None.
#
#    Bad:
#       def bad_factorial(n):
#           if n == 0:
#               return 1
#           n * bad_factorial(n - 1)   # missing `return` → returns None
#
#    Fix:
#       return n * factorial(n - 1)
#
# ❌ MISTAKE 3 — Confusing "what the function returns" vs "what it prints".
#    `print(x)` shows x on the screen. `return x` hands x back to the caller.
#    Recursion that needs to combine values MUST `return`, not just print.
#
# ❌ MISTAKE 4 — Not making the problem smaller.
#    If you call f(n) inside f(n), the problem never shrinks. You must
#    pass something smaller, like f(n - 1), f(s[1:]), f(arr[1:]), etc.
#
# ❌ MISTAKE 5 — Reaching for recursion when a simple loop would do.
#    "Sum a list" or "find max" — a `for` loop is shorter, faster, and
#    won't blow up the call stack on huge inputs. Recursion shines for
#    naturally nested or branching problems (see next section).


# ======================================================================
# 11. When to Reach for Recursion (Checklist)
# ======================================================================
#
# Use recursion when the problem has any of these shapes. (You don't need
# to know HOW to solve all of these yet — just recognize the smell.)
#
#   ✅ TREES
#      Binary trees, file folders, the DOM, JSON. Each node has children
#      that look just like the parent — perfect for recursion.
#
#   ✅ NESTED STRUCTURES
#      A list of lists of lists, or any data that contains smaller
#      versions of itself.
#
#   ✅ DIVIDE & CONQUER
#      You can split the input in half, solve each half, then combine.
#      Examples: merge sort, quicksort, binary search.
#
#   ✅ BACKTRACKING
#      Try a choice, recurse, undo if it didn't work. Used in mazes,
#      sudoku solvers, "all permutations of a string", etc.
#
# When NOT to reach for recursion:
#   ❌ Simple loops over a flat array (use `for` / `while`).
#   ❌ Problems where the input can be HUGE (Python's default recursion
#      depth is around 1,000 — a loop has no such limit).


# ======================================================================
# 12. One-Page Summary / Cheatsheet
# ======================================================================
#
# 🔑 What recursion is:
#    A function that calls itself on a smaller version of the problem,
#    until the problem is small enough to solve directly.
#
# 🔑 Every recursive function has TWO parts:
#    1) Base case      — the "stop" condition.
#    2) Recursive case — shrink the problem and call yourself.
#
# 🔑 The Named Rules:
#    • Base Case Rule — Always have a base case, or you crash.
#    • Shrink Rule    — Every recursive call must move toward the base case.
#    • 3-Step Recipe  — Stop. Shrink. Combine.
#
# 🔑 Mental picture (the call stack):
#    Going DOWN  → each call is paused, waiting for the smaller call.
#    Coming UP   → smaller calls return, and the paused calls combine results.
#
# 🔑 Skeleton of (almost) every simple recursive function:
#
#       def f(input):
#           if input is at the base case:
#               return the trivial answer
#           smaller_answer = f(smaller_input)
#           return combine(input, smaller_answer)
#
# 🔑 Common beginner traps:
#    • Forgetting the base case.
#    • Forgetting to `return` the recursive call.
#    • Mixing up `print` with `return`.
#    • Not making the input smaller each call.
#
# 🔑 Use recursion for: trees, nested data, divide & conquer, backtracking.
#    Use a loop for:   simple iteration over a flat list.
#
# That's the whole foundation. Re-read sections 5–8 (the tiny traces)
# until you can predict each step in your head — that's when recursion
# truly clicks.
