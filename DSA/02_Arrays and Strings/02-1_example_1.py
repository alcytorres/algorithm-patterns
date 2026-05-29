# Simple Palindrome Checker
"""
Check if a clean String is a Palindrome

Given a string s, return true if it is a palindrome, false otherwise.

Checks if string s is a palindrome by comparing characters from both ends.
"""

# Solution: Two Pointers: Opposite-End Character Check

def is_palindrome(s):
    left = 0                    
    right = len(s) - 1          

    while left < right:         
        if s[left] != s[right]: 
            return False
        left += 1               
        right -= 1             

    return True                

s = "racecar"
print(is_palindrome(s))  
# Output: True

# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def is_palindrome(s):
    left = 0                    # Start left pointer at index 0
    right = len(s) - 1          # Start right pointer at last index

    while left < right:         # Continue until pointers meet
        if s[left] != s[right]: # If characters don't match, not a palindrome
            return False
        left += 1               # Move left pointer inward
        right -= 1              # Move right pointer inward

    return True                 # String is a palindrome


"""
Time: O(N)
  - Let N = length of the string s.

  - Step 1: Set left = 0 and right = N - 1 → O(1).

  - Step 2: Two pointers scan from both ends → O(N).
      • Loop runs while left < right — at most N/2 comparisons.
      • Each iteration: compare s[left] and s[r] → O(1).
      • Move left and right inward → O(1).

  - Overall: O(N).


Space: O(1)
  - Only a few integer variables (left, right).
  - No extra data structures.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Two pointers scan the string once from both ends.

Space: O(1)
  - Only pointer variables are used.


---
Overview for Each Iteration
Input: s = "racecar"

Step: Check if string is a palindrome using two pointers
l | r | s[l] | s[r] | l < r | Action      | Result
--|---|------|------|-------|-------------|--------
0 | 6 | r    | r    | True  | l+=1, r-=1  | -
1 | 5 | a    | a    | True  | l+=1, r-=1  | -
2 | 4 | c    | c    | True  | l+=1, r-=1  | -
3 | 3 | e    | e    | False | Exit loop   | True

Final: True


---
Most IMPORTANT thing to Understand:
    • A palindrome reads the same forward and backward.

    • Compare characters from both ends moving inward.

    • left starts at the front, right starts at the back.

    • If any pair doesn't match → not a palindrome → return False immediately.

    • If pointers meet or cross without a mismatch → palindrome → return True.


---
Why this code Works:
    • Two pointers:
        • left = front character to check.
        • right = back character to check.

    • Each loop compares s[left] and s[right]:
        • Match → move both pointers inward.
        • No match → return False early.

    • Loop stops when left >= right — every necessary pair was checked.

    • Efficiency:
        • Brute force reverses the whole string → O(N²) time, O(N) space.
        • Two pointers compare in place → O(N) time, O(1) space.

    • Intuition:
        • Like folding the string in half — outer letters must match, then the next pair in, and so on.


---
TLDR:
    • Walk two pointers from opposite ends; if all pairs match until they meet, the string is a palindrome.


---
Quick Example Walkthrough:
    s = "racecar"

    Step 1: left = 0, right = 6

    Step 2: Compare pairs moving inward
        • s[0]='r' vs s[6]='r' → match → left=1, right=5
        • s[1]='a' vs s[5]='a' → match → left=2, right=4
        • s[2]='c' vs s[4]='c' → match → left=3, right=3

    Step 3: left < right? 3 < 3 → False → exit loop

    Final Answer: True


---
Full Example Walkthrough:
    s = "racecar"

    Starting State:
        left = 0
        right = 6

        left points at s[0] = "r"
        right points at s[6] = "r"

    Loop Iteration 1:
        Compare:
            s[left] == s[right]
            "r" == "r" → MATCH

        Move both inward:
            left = 1, right = 5

        Current state:
            left points at s[1] = "a"
            right points at s[5] = "a"

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            "a" == "a" → MATCH

        Move both inward:
            left = 2, right = 4

        Current state:
            left points at s[2] = "c"
            right points at s[4] = "c"

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            "c" == "c" → MATCH

        Move both inward:
            left = 3, right = 3

        Current state:
            left and right both point at s[3] = "e"

    --------------------------------------------------

    Final Check:
        left < right → 3 < 3 → False → loop ends
        return True

        Meaning: every mirrored pair matched — "racecar" is a palindrome.



---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Does the string read the same forward and backward?

    • You only need to compare mirrored positions — not rebuild the whole string.


Start naive (totally fine)
    • Reverse the string and check if it equals the original.
    • Say out loud: "If backward == forward, it's a palindrome."
    • Time: O(N²) if you build the reverse with string concatenation.


The one insight that unlocks the optimal code
    • You don't need a reversed copy — compare from both ends at once.
    • First vs last, then second vs second-to-last, move inward.
    • Stop early the moment a pair doesn't match.


Why two pointers?
    • Palindrome = mirrored pairs. That's naturally a front pointer and a back pointer.
    • No extra string, no reversal — just index math.


Thought → line of code
    right = len(s) - 1
        → "Start at the last index, not len(s)."

    while left < right:
        → "Keep going while there are still pairs to compare — stop when they meet."

    if s[left] != s[right]: return False
        → "One mismatch kills it — no need to check the rest."

    left += 1 / right -= 1
        → "Pair matched — shrink the window from both sides."


Memory hook (one sentence)
    • Two pointers walk inward; any mismatch = False, they meet = True.


Would you arrive at this cold?
    • Immediately: reverse and compare, or loop with index i and index len-1-i.
    • After feeling the O(N²) pain of string building: compare in place instead.
    • Bookkeeping: left=0, right=len-1 — standard two-pointer setup.
    • Real insight: palindrome is a mirror problem → opposite-end pointers.



---
Q: Why is the time complexity O(N) instead of O(N/2)?

  • The loop runs at most N/2 times because two pointers move toward the center.

  • Each iteration checks two characters and moves both pointers inward.

  • Big-O measures how runtime grows as N increases, not the exact number of operations.

  • Since N/2 still grows linearly with N, O(N/2) simplifies to O(N).

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def is_palindrome_bruteforce(s):
    # Reverse the string and compare
    reversed_s = ""
    
    for c in s:
        reversed_s = c + reversed_s
    
    if reversed_s == s:
        return True
    return False


s = "racecar"
print(is_palindrome_bruteforce(s))
# Output: True

"""
Time: O(N²)
  - Let N = length of the string s.

  - Step 1: Build reversed string → O(N²).
      • Loop runs N times (once per character).
      • Each step: reversed_s = c + reversed_s creates a new string → O(N).

  - Step 2: Compare reversed_s == s → O(N).

  - Combined: O(N² + N).
  - Overall: O(N²).


Space: O(N)
  - reversed_s stores up to N characters.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N²)
  - Each prepend builds a new string; N prepends → quadratic time.

Space: O(N)
  - Reversed copy of the string.


---
Overview for Each Iteration
s = "racecar"

    reversed_s starts = ""

    read 'r' → reversed_s = "r"
    read 'a' → reversed_s = "ar"
    read 'c' → reversed_s = "car"
    read 'e' → reversed_s = "ecar"
    read 'c' → reversed_s = "cecar"
    read 'a' → reversed_s = "acecar"
    read 'r' → reversed_s = "racecar"

    compare reversed_s == s
    "racecar" == "racecar" → True

"""