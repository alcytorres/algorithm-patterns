# 412. Fizz Buzz
"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]

Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
    1 <= n <= 104

Solution: https://leetcode.com/problems/fizz-buzz/description/
"""

# Solution 1: Straightforward If/Elif/Else Chain

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    ans = []

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))

    return ans

n = 15
print(fizzBuzz(n))

# Output: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

# → Loop each i; check 3&5 first, then 3, then 5, else str(i)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def fizzBuzz(n):
    ans = []                              # Empty list to collect results

    for i in range(1, n+1):               # Go through each number 1 to n
        if i % 3 == 0 and i % 5 == 0:     # Divisible by both? Check this FIRST
            ans.append("FizzBuzz")
        elif i % 3 == 0:                  # Divisible by 3 only?
            ans.append("Fizz")
        elif i % 5 == 0:                  # Divisible by 5 only?
            ans.append("Buzz")
        else:                             # Not divisible by 3 or 5
            ans.append(str(i))            # Just add the number as a string

    return ans                            # Return the full list of labels



"""
Time: O(N)
  - Let N = input integer n (we generate results for numbers 1 → n).
  - The loop runs from 1 to n → N iterations.
  - Each iteration performs constant work:
      * Modulo checks (i % 3, i % 5) → O(1)
      * Append to list → O(1)
  - Combined time across all iterations: O(N).
  - Overall: O(N).


Space: O(N)
  - Output list 'ans' stores one string for each number from 1 → n → N elements.
  - Only a few extra variables besides the list.
  - Overall space complexity: O(N).


Interview Answer: Worst Case

Time: O(N)
  - Single loop from 1 to n with constant work per iteration.

Space: O(N)
  - Output list stores n strings.



Note: LeetCode lists space as O(1) bc they exclude the required output list

We say O(N) because we count everything, and in interviews counting the output is best practice.



---
Most IMPORTANT thing to Understand:
    • We build one answer string for every number from 1 to n.

    • The order of checks matters: check divisible by BOTH 3 and 5 first.

    • If we checked "divisible by 3" before "both", numbers like 15 would wrongly become "Fizz".

    • `%` asks: "does this number divide evenly?" → remainder 0 means yes.

---
Why this code Works:
    • Loop:
        • Go through every i from 1 to n.
        • Decide the correct label for that i, then append it.

    • If / elif chain:
        • First: i divisible by 3 AND 5 → "FizzBuzz"
        • Else if divisible by 3 → "Fizz"
        • Else if divisible by 5 → "Buzz"
        • Else → the number itself as a string

    • Efficiency:
        • One pass from 1 to n.
        • Time: O(n)
        • Space: O(n) for the output list

    • Intuition:
        • Like sorting mail into 4 boxes.
        • "Both 3 and 5" is the special box — check it first so those numbers don't land in the wrong pile.

---
TLDR:
    • Loop 1 to n and label each number by divisibility rules, checking 3-and-5 first so FizzBuzz is never mislabeled as only Fizz or only Buzz.


---
Quick Example Walkthrough:

n = 15

Step 1: Start with empty list
    ans = []

Step 2: Check each i from 1 to 15
    • i=1 → not 3 or 5 → "1"
    • i=2 → not 3 or 5 → "2"
    • i=3 → divisible by 3 → "Fizz"
    • i=4 → not 3 or 5 → "4"
    • i=5 → divisible by 5 → "Buzz"
    • i=6 → divisible by 3 → "Fizz"
    • i=7 → "7"
    • i=8 → "8"
    • i=9 → "Fizz"
    • i=10 → "Buzz"
    • i=11 → "11"
    • i=12 → "Fizz"
    • i=13 → "13"
    • i=14 → "14"
    • i=15 → divisible by 3 AND 5 → "FizzBuzz"

Final Answer: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


---
Full Example Walkthrough:
    n = 5

    Starting State:
        ans = []
        Loop will run i = 1, 2, 3, 4, 5

    Loop Iteration 1 (i = 1):
        Compare:
            1 % 3 == 0 and 1 % 5 == 0? → NO
            1 % 3 == 0? → NO
            1 % 5 == 0? → NO

        Else branch:
            ans.append("1")

        Now:
            ans = ["1"]

    --------------------------------------------------

    Loop Iteration 2 (i = 2):
        Compare:
            2 % 3 == 0 and 2 % 5 == 0? → NO
            2 % 3 == 0? → NO
            2 % 5 == 0? → NO

        Else branch:
            ans.append("2")

        Now:
            ans = ["1", "2"]

    --------------------------------------------------

    Loop Iteration 3 (i = 3):
        Compare:
            3 % 3 == 0 and 3 % 5 == 0? → NO (3 is not divisible by 5)
            3 % 3 == 0? → YES

        Elif branch:
            ans.append("Fizz")

        Now:
            ans = ["1", "2", "Fizz"]

    --------------------------------------------------

    Loop Iteration 4 (i = 4):
        Compare:
            4 % 3 == 0 and 4 % 5 == 0? → NO
            4 % 3 == 0? → NO
            4 % 5 == 0? → NO

        Else branch:
            ans.append("4")

        Now:
            ans = ["1", "2", "Fizz", "4"]

    --------------------------------------------------

    Loop Iteration 5 (i = 5):
        Compare:
            5 % 3 == 0 and 5 % 5 == 0? → NO (5 is not divisible by 3)
            5 % 3 == 0? → NO
            5 % 5 == 0? → YES

        Elif branch:
            ans.append("Buzz")

        Now:
            ans = ["1", "2", "Fizz", "4", "Buzz"]

    --------------------------------------------------

    Final Check:
        Loop finished (i went through 1 → 5).

        return ans
        → ["1", "2", "Fizz", "4", "Buzz"]

        This means:
            Every number from 1 to n got the correct label by checking both, then 3, then 5, then the number itself.





---
Overview for Each Iteration
Input: n = 15

Loop from 1 to n: check divisibility, append the matching label.

i  | i%3==0 | i%5==0 | Action         | ans (appended)
---|--------|--------|----------------|---------------
1  | False  | False  | append str(i)  | "1"
2  | False  | False  | append str(i)  | "2"
3  | True   | False  | append Fizz    | "Fizz"
4  | False  | False  | append str(i)  | "4"
5  | False  | True   | append Buzz    | "Buzz"
6  | True   | False  | append Fizz    | "Fizz"
7  | False  | False  | append str(i)  | "7"
8  | False  | False  | append str(i)  | "8"
9  | True   | False  | append Fizz    | "Fizz"
10 | False  | True   | append Buzz    | "Buzz"
11 | False  | False  | append str(i)  | "11"
12 | True   | False  | append Fizz    | "Fizz"
13 | False  | False  | append str(i)  | "13"
14 | False  | False  | append str(i)  | "14"
15 | True   | True   | append FizzBuzz| "FizzBuzz"

Final: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]




---
Q: Why do we write  for i in range(1, n+1):   
   instead of range(1, n) or range(0, n+1)?

A: We need to process every number **from 1 to n inclusive** (exactly what Fizz Buzz asks for).

- range(1, n+1) → gives 1, 2, 3, ..., n  
  (starts at 1 and includes n)

- range(1, n) → gives 1, 2, 3, ..., n-1  
  (misses the last number n)

- range(0, n+1) → gives 0, 1, 2, ..., n  
  (starts at 0 — which we don't want)
  

Fizz Buzz never includes 0 and always includes n, so `range(1, n+1)` is the correct way to loop over exactly the numbers 1 through n.




---
Q: What does "1-indexed" mean here?

A: It means the counting starts at 1, not 0.

  • answer[1] = label for the number 1.
  • answer[2] = label for the number 2.
  • answer[n] = label for the number n.

  • In Python lists are 0-indexed, so answer[0] holds the label for number 1.
  • That's why we loop with `range(1, n+1)` — we process numbers 1 through n, then append each label in order.
"""







# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 2: String Concatenation Build
def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if not s:
            s = str(i)
        result.append(s)
    return result


n = 15
print(fizzBuzz(n))
# Output: 15 labels for 1..15 → Append Fizz/Buzz when divisible; if still empty, use str(i) (15 → FizzBuzz)

