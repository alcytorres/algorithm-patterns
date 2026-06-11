# 202. Happy Number
"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 
Example 1:
    Input: n = 19
    Output: true
    Explanation:
    1² + 9² = 82
    8² + 2² = 68
    6² + 8² = 100
    1² + 0² + 0² = 1

Example 2:
    Input: n = 2
    Output: false
    Explanation:
    2² = 4
    4² = 16
    1² + 6² = 37
    3² + 7² = 58
    5² + 8² = 89
    8² + 9² = 145
    1² + 4² + 5² = 42
    4² + 2² = 20
    2² + 0² = 4

    We are back at 4, so the process repeats:
    4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4

    Since we never reach 1, the number is not happy.
 
Constraints:
    1 <= n <= 231 - 1

Solution: https://leetcode.com/problems/happy-number/
"""


#1 — Hash set cycle detection (recommended)

def get_next(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

n = 19
print(isHappy(n))  
# Output: True


# LeetCode submission — one function, no helper (same algorithm)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            n = total

        return n == 1


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def get_next(n):
    total = 0                 # Running sum of squared digits
    while n > 0:              # Keep going while digits are left
        digit = n % 10        # Grab the rightmost digit
        total += digit * digit  # Add its square to the total
        n //= 10              # Drop the digit we just used
    return total              # Return the new number for this step

def isHappy(n):
    seen = set()              # Notebook of numbers we've already seen
    while n != 1 and n not in seen:  # Keep going until 1 or a repeat
        seen.add(n)           # Remember this number before moving on
        n = get_next(n)       # Replace n with sum of squared digits
    return n == 1             # True if we landed on 1, False if we looped


"""
Time: O(log n)
  - Let n = the input number, D = number of digits in n.

  Step 1: get_next(n)
      • Loops through every digit once → O(D).
      • D is about log n (more digits as n gets bigger).

  Step 2: Main loop (isHappy)
      • Runs until n is 1 or n is already in seen.
      • Each loop step calls get_next once and adds n to seen.
      • We cannot loop forever because seen catches repeats.
      • After each step, n usually gets smaller (fewer digits to process).

  Combined: O(steps × digits per step) → O(log n).
  Overall: O(log n).


Space: O(log n)
  - seen set stores each number we visit before stopping.
  - One new entry is added per loop step.
  - Set size grows with how many steps we take (same order as time).

  - A few extra variables (total, digit) use O(1).
  Overall: O(log n).


Interview Answer: Worst Case

Time: O(log n)
  - Each get_next scans the digits of n, and we repeat until 1 or a cycle.

Space: O(log n)
  - Hash set stores visited numbers, one per step before we stop.




---
Most IMPORTANT thing to Understand:
    • A happy number keeps transforming until it hits 1.

    • An unhappy number never hits 1 — it loops through the same numbers forever.

    • get_next(n) is one transformation step: sum of each digit squared.

    • seen is a notebook of every number we've already visited.

    • If n shows up in seen again, we're in a loop → not happy.

    • If n reaches 1, we're done → happy.

---
Why this code Works:
    • get_next(n):
        • Peels off digits from the right with n % 10.
        • Squares each digit and adds to total.
        • Returns the new number for this step.

    • seen set:
        • Stores numbers we've already seen.
        • Before transforming n, we add the current n to seen.
        • If the next n is already in seen, the loop stops.

    • Main loop condition (n != 1 and n not in seen):
        • Keep going while we haven't won (n == 1) and haven't looped (n in seen).

    • Return n == 1:
        • True if we landed on 1.
        • False if we stopped because of a repeat.

    • Efficiency:
        • Without seen, an unhappy number would loop forever.
        • seen catches the repeat in one lookup → O(1) per check.

    • Intuition:
        • Like walking a trail and dropping breadcrumbs.
        • If you step on a breadcrumb you've already dropped, you're going in circles.

---
TLDR:
    • Keep replacing n with the sum of squared digits until n is 1 (happy) or n repeats (not happy). The set tracks visited numbers so we can detect the loop.


---
Quick Example Walkthrough:
    n = 19

    Step 1: Start with seen = {}, n = 19
        • Add 19 to seen → seen = {19}
        • get_next(19) = 1² + 9² = 82 → n = 82

    Step 2: n = 82, not in seen yet
        • Add 82 → seen = {19, 82}
        • get_next(82) = 8² + 2² = 68 → n = 68

    Step 3: n = 68
        • Add 68 → seen = {19, 82, 68}
        • get_next(68) = 6² + 8² = 100 → n = 100

    Step 4: n = 100
        • Add 100 → seen = {19, 82, 68, 100}
        • get_next(100) = 1² + 0² + 0² = 1 → n = 1

    Step 5: Loop stops because n == 1
        • return n == 1 → True

    Final Answer: True


---
Full Example Walkthrough:
    n = 19

    Starting State:
        n = 19
        seen = {}

    get_next reminder (matches the code):
        digit = n % 10   → grab last digit
        total += digit²  → add its square
        n //= 10         → drop that digit, repeat until n is 0
        return total     → send the sum back (only when inner while is done)


    Loop Iteration 1:
        Check:
            n != 1 → 19 != 1 → True
            n not in seen → 19 not in {} → True
            → Enter loop

        Add to seen:
            seen.add(19)
            seen = {19}

        Transform — get_next(19), peel from the RIGHT:
            total = 0
            n=19 → last digit 9 → total=81 → n becomes 1
            n=1  → last digit 1 → total=82 → n becomes 0 → stop
            return total → 82 goes back
            n = get_next(n) → n is now 82 (main loop continues)

        Current state:
            n = 82
            seen = {19}

    --------------------------------------------------

    Loop Iteration 2:
        Check:
            n != 1 → 82 != 1 → True
            n not in seen → 82 not in {19} → True
            → Enter loop

        Add to seen:
            seen = {19, 82}

        Transform — get_next(82), peel from the RIGHT:
            total = 0
            n=82 → last digit 2 → total=4  → n becomes 8
            n=8  → last digit 8 → total=68 → n becomes 0 → stop
            return total → 68  |  n = get_next(n) → n is now 68

        Current state:
            n = 68
            seen = {19, 82}

    --------------------------------------------------

    Loop Iteration 3:
        Check:
            n != 1 → True
            n not in seen → True
            → Enter loop

        Add to seen:
            seen = {19, 82, 68}

        Transform — get_next(68), peel from the RIGHT:
            n=68 → last digit 8 → total=64  → n=6
            n=6  → last digit 6 → total=100 → n=0 → stop
            return total → 100  |  n = get_next(n) → n is now 100

        Current state:
            n = 100
            seen = {19, 82, 68}

    --------------------------------------------------

    Loop Iteration 4:
        Check:
            n != 1 → True
            n not in seen → True
            → Enter loop

        Add to seen:
            seen = {19, 82, 68, 100}

        Transform — get_next(100), peel from the RIGHT:
            n=100 → digit 0 → total=0 → n=10
            n=10  → digit 0 → total=0 → n=1
            n=1   → digit 1 → total=1 → n=0 → stop
            return total → 1  |  n = get_next(n) → n is now 1

        Current state:
            n = 1
            seen = {19, 82, 68, 100}

    --------------------------------------------------

    Loop ends:
        n == 1 → while condition is False → exit loop
        (main loop is done — get_next is NOT called again)

    Final Check:
        return n == 1
        1 == 1 → True

        This means:
            19 reached 1 through the transformation process → happy number.




---
Overview for Each Iteration
Input: n = 19

Transform n with get_next until n == 1 or n repeats

i | n  | in seen? | get_next(n) | Action          | seen
--|----|----------|-------------|-----------------|------------------
- | -  | -        | -           | start           | {}
0 | 19 | No       | 82          | add 19, n → 82  | {19}
1 | 82 | No       | 68          | add 82, n → 68  | {19, 82}
2 | 68 | No       | 100         | add 68, n → 100 | {19, 82, 68}
3 | 100| No       | 1           | add 100, n → 1  | {19, 82, 68, 100}

Loop exits: n == 1 → return n == 1 → True

Final: True


---
Q: Why use a helper function (get_next) here?

    • get_next does ONE job: transform n into the sum of squared digits.

    • isHappy does a DIFFERENT job: loop, track seen, decide happy or not.

    • Splitting them makes each part easier to read while learning.

    • Not required — you can inline get_next inside isHappy for LeetCode submission.

    • Same algorithm either way; helper is for clarity, not correctness.






---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Keep replacing n with "sum of squared digits" until you hit 1 (happy) or loop forever (not happy).

    • The problem literally says "loops endlessly in a cycle" — that's a huge hint you need cycle detection.

    • Return True/False — no array, just simulate a process step by step.


Start naive (totally fine)
    • Write a while loop: while n != 1, transform n with digit squares.
    • Problem: unhappy numbers like n=2 never reach 1 — you'd loop forever.
    • Time: infinite on unhappy inputs without a stop condition.


The one insight that unlocks the optimal code
    • Track every n you've already seen — if n repeats, you're in a cycle → return False.
    • If n reaches 1 before any repeat → return True.
    • A set gives O(1) "have I seen this before?" checks.


Why a hash set?
    • The problem is NOT about the digits — it's about detecting when the sequence repeats.
    • You only need membership ("is this number new?"), not counts.
    • Without seen, simulation has no exit for unhappy numbers.


Thought → line of code
    def get_next(n):
        → "Pull out the repeated step into a helper — one transformation per call."

    digit = n % 10  /  n //= 10
        → "Peel digits from the right — last digit first."
        → "% 10 and //= 10 is the standard digit-stripping pattern (not obvious first time)."

    seen = set()
        → "Notebook of every n we've visited."

    while n != 1 and n not in seen:
        → "Keep going until we win (hit 1) OR loop (n already seen)."

    seen.add(n)  then  n = get_next(n)
        → "Mark current n BEFORE transforming — so we catch the repeat on the next check."

    return n == 1
        → "If we stopped because n==1 → True. If we stopped because n in seen → False."


Memory hook (one sentence)
    • Transform n until 1 or repeat — use a set to catch the repeat.


Would you arrive at this cold?
    • Immediately: simulate the digit-square process in a while loop.
    • Stuck on: unhappy numbers loop forever — you need something to detect cycles.
    • After "loops in a cycle" clicks: seen set is the obvious tool (hashing chapter helps).
    • Bookkeeping: get_next helper, % 10 / //= 10 digit peeling — pattern to memorize separately.
    • Real insight: the set is the whole trick; get_next is just the transformation rule from the problem.

"""






# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — List to track seen numbers (linear scan each step)

def get_next(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def isHappy_bruteforce(n):
    seen = []
    while n != 1 and n not in seen:
        seen.append(n)
        n = get_next(n)
    return n == 1


n = 19
print(isHappy_bruteforce(n))
# Output: True


"""
Time: O(K²)
  - Let K = number of transformation steps before stopping.
  - Let D = digits in n during get_next (about log n).

  - Step 1: get_next(n) peels each digit → O(D) per step.

  - Step 2: n not in seen scans the whole list → O(len(seen)), up to O(K).

  - Main loop runs K times.
  - Combined: O(K × (D + K)) = O(K² + K log n).
  - Overall: O(K²) when list scans dominate.


Space: O(K)
  - seen list stores up to K numbers before stopping.
  - Same memory as the set version.
  - Overall: O(K).


Interview Answer: Worst Case

Time: O(K²)
  - Each step scans the growing list to check for repeats.

Space: O(K)
  - List stores every number visited before stopping.


---
Overview for Each Iteration
Input: n = 19

    seen starts = []

    n = 19 → not in [] → append → seen = [19] → get_next → n = 82
    n = 82 → not in [19] → append → seen = [19, 82] → get_next → n = 68
    n = 68 → not in [19, 82] → append → seen = [19, 82, 68] → get_next → n = 100
    n = 100 → not in [19, 82, 68] → append → seen = [19, 82, 68, 100] → get_next → n = 1

    n == 1 → exit loop → return True

Final: True

"""







# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative get_next — string version (same hash set algorithm)

def get_next_str(n):
    return sum(int(d) ** 2 for d in str(n))

def isHappy_str(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next_str(n)

    return n == 1


"""
Same algorithm as the main solution — only get_next changes.

When to use:
    • Still learning % 10 and //= 10 — this avoids digit math entirely.
    • str(n) turns 19 into "19", then you square each character as a digit.

Tradeoff:
    • Easier to read and write.
    • Slightly slower (creates a string each step) — fine for LeetCode, not for interviews if you should know digit peeling.

Time: O(log n)   — same as main (hash set + transform each step)
Space: O(log n)  — seen set stores visited numbers

"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 2 — Floyd's cycle detection (O(1) space, learn after hash set)

def get_next(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def isHappy_floyd(n):
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1 or slow == 1


"""
Learn this AFTER the hash set version makes sense.

Same get_next — different way to detect a cycle:
    • slow moves 1 step per loop
    • fast moves 2 steps per loop
    • if they meet inside a cycle → not happy
    • if fast hits 1 → happy

Why learn it:
    • O(1) space — no seen set needed
    • Same trick on Linked List Cycle, Find the Duplicate Number

When to use:
    • Interview asks for O(1) space
    • Not your first choice while learning Happy Number — hash set is clearer

Time: O(log n)  — same digit work per step, slow/fast meet in bounded steps
Space: O(1)     — only slow and fast pointers, no seen set

"""