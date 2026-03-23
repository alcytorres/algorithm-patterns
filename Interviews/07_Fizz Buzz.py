# 412. Fizz Buzz
"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Solution: https://leetcode.com/problems/fizz-buzz/solutions/173828/fizz-buzz-by-leetcode-v2ox/

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
    • For each number from 1 to n, check divisibility by 3 and 5 to decide what string to add.

    • Order matters: check "both 3 and 5" FIRST, then 3 alone, then 5 alone, then default to the number as a string.

    • If you check 3 or 5 individually first, you'll never reach the "both" case — it'll get caught early.

---
Why this code Works:
    • Loop from 1 to n: each number gets exactly one label — FizzBuzz, Fizz, Buzz, or the number itself.

    • if/elif/else chain: guarantees only ONE branch runs per number. The first true condition wins.

    • Why check "both" first: 15 is divisible by 3 AND 5. If we checked `i % 3` first, it would match "Fizz" and skip "FizzBuzz." Checking both first prevents this.

    • Efficiency: one pass, constant work per number → O(N) time. No nested loops, no sorting.

    • Intuition: it's just a labeling machine — feed it numbers 1 through n, and it stamps each one with the right label.

---
TLDR
    • Loop 1 to n, check divisibility in order (both → 3 → 5 → number), append the matching string.

---
Quick Example Walkthrough:
    n = 5

    i=1: not divisible by 3 or 5 → append "1"
    i=2: not divisible by 3 or 5 → append "2"
    i=3: divisible by 3          → append "Fizz"
    i=4: not divisible by 3 or 5 → append "4"
    i=5: divisible by 5          → append "Buzz"

    Final Answer: ["1", "2", "Fizz", "4", "Buzz"]



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

