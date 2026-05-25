# 125. Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---
A simpler way to say it:
    • Given a string, strip out everything that isn't a letter or number, make it all lowercase, then check if it reads the same forwards and backwards. Return true if it does, false if it doesn't.

    So the steps are:
      1. Remove all spaces, punctuation, and special characters (keep only letters and digits).
      2. Lowercase everything.
      3. Compare the cleaned string to its reverse — if they match, it's a palindrome.
 
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

Solution: https://leetcode.com/problems/valid-palindrome/description/
"""


# Solution 1: Build String → Two Pointers (with list + join)

def is_palindrome(s):
    chars = []
    for c in s:
        if c.isalnum():
            chars.append(c.lower())
    new_string = "".join(chars)

    l = 0
    r = len(new_string) - 1

    while l < r:
        if new_string[l] != new_string[r]:
            return False
        l += 1
        r -= 1

    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))  # Output: True


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def is_palindrome(s):

    # Step 1: Create a new string with only letters and numbers, all lowercase
    chars = []                        # Empty list to collect valid characters

    for c in s:                       # Go through each character in the string
        if c.isalnum():               # Keep only letters and numbers
            chars.append(c.lower())   # Lowercase it and add to the list
    new_string = "".join(chars)       # Turn the list into one clean string


    # Step 2: Check if the new string reads the same forwards and backwards
    l = 0                             # Left pointer starts at the beginning
    r = len(new_string) - 1           # Right pointer starts at the end

    while l < r:                      # Keep going until pointers meet in the middle
        if new_string[l] != new_string[r]:  # If the two ends don't match
            return False              # Not a palindrome — stop early
        l += 1                        # Move left pointer inward
        r -= 1                        # Move right pointer inward

    return True                       # Every pair matched — it's a palindrome


"""
Time: O(N)
  - Let N = length of the input string s.

  - Step 1: Build cleaned string with list + join → O(N).
      • Scan s once → O(N).
      • Filter: c.isalnum() → O(1) per character.
      • Lowercase: c.lower() → O(1) per character.
      • chars.append() → O(1) per character.
      • "".join(chars) → one O(N) pass to build the final string.

  - Step 2: Two pointers scan new_string from both ends → at most N/2 comparisons → O(N).
  - Overall: O(N).

Space: O(N)
  - chars stores up to N characters (worst case: every char is alphanumeric).
  - new_string stores up to N characters.
  - Pointer variables (l, r) → O(1).
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to build cleaned string, one pass to compare from both ends.

Space: O(N)
  - List and cleaned string can be as long as the original input.


---
Overview for Each Iteration
Input: s = "A man, a plan, a canal: Panama"

Step 1: Build cleaned string (list + join)
c            | isalnum? | append      | chars (after)
-------------|----------|-------------|--------------------
A            | Yes      | a           | ['a']
(space)      | No       | —           | ['a']
m            | Yes      | m           | ['a', 'm']
a            | Yes      | a           | ['a', 'm', 'a']
n            | Yes      | n           | ['a', 'm', 'a', 'n']
,            | No       | —           | ['a', 'm', 'a', 'n']
...          | ...      | ...         | → continues
a            | Yes      | a           | [..., 'a']

join → new_string = "amanaplanacanalpanama"

Step 2: Two-pointer validation
l  | r  | char l | char r | match? | Action
---|----|--------|--------|--------|------------------
0  | 20 | a      | a      | Yes    | l++, r--
1  | 19 | m      | m      | Yes    | l++, r--
2  | 18 | a      | a      | Yes    | l++, r--
...| ...| ...    | ...    | Yes    | continue
10 | 10 | n      | n      | —      | l ≥ r → exit

Final: True




---
Most IMPORTANT thing to Understand:
    • A palindrome reads the same forwards and backwards (after cleaning).

    • Cleaning means: keep only letters and digits, and lowercase everything.

    • Once cleaned, we only need to check that each pair (left end, right end) matches as we move inward.

    • If even ONE pair fails to match → not a palindrome.

---
Why this code Works:
    • Step 1 — Build a clean version:
        • We collect valid characters into a list, lowercased.
        • Then "".join(chars) glues them into one final string.
        • Using a list + join avoids the slow string += pattern.

    • Step 2 — Two pointers:
        • l starts at the beginning, r starts at the end.
        • Each loop compares the two ends.
        • If they match, both pointers move inward.
        • If they don't match, return False immediately.

    • Why two pointers work:
        • A palindrome is symmetric, so position i from the start
          must equal position i from the end.

    • Efficiency:
        • Each character is touched a constant number of times.
        • No nested loops, no sorting, no extra scans.

    • Intuition:
        • Think of folding the cleaned string in half.
        • Every character on the left must line up with its mirror on the right.

---
TLDR:
    • Clean the string (letters + digits, lowercased), then walk two pointers inward from both ends — first mismatch means False.


---
Quick Example Walkthrough:

    s = "A man, a plan, a canal: Panama"

    Step 1: Build the cleaned string
        • Skip spaces, commas, and the colon.
        • Lowercase each kept character.
        • Result: new_string = "amanaplanacanalpanama"

    Step 2: Walk two pointers from both ends
        • l = 0, r = 20
        • Compare new_string[l] vs new_string[r] at each step.
        • Every pair matches as they move inward.
        • Pointers meet in the middle → return True.

    Comparison:
        a == a
        m == m
        a == a
        n == n
        a == a
        p == p
        ...
        ... pointers meet in the middle with all matches

    Final Answer: True


---
Full Example Walkthrough:
    s = "A man, a plan, a canal: Panama"

    Starting State:
        chars = []
        l, r = (set after Step 1)

    --------------------------------------------------
    Step 1: Build cleaned string

    Go through each character in s:

        'A' → isalnum? Yes → append 'a' → chars = ['a']
        ' ' → isalnum? No  → skip
        'm' → Yes → append 'm' → chars = ['a', 'm']
        'a' → Yes → append 'a' → chars = ['a', 'm', 'a']
        'n' → Yes → append 'n' → chars = ['a', 'm', 'a', 'n']
        ',' → No  → skip
        ... (continues for the rest of the string) ...

    After the loop:
        new_string = "".join(chars) = "amanaplanacanalpanama"

    --------------------------------------------------
    Step 2: Two-pointer validation

    Set up:
        l = 0
        r = len(new_string) - 1 = 20

    Loop Iteration 1:
        Compare:
            new_string[0] == new_string[20]
            'a' == 'a' → MATCH

        Move:
            l += 1 → l = 1
            r -= 1 → r = 19

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            new_string[1] == new_string[19]
            'm' == 'm' → MATCH

        Move:
            l = 2, r = 18

    --------------------------------------------------

    Loop Iteration 3:
        Compare:
            new_string[2] == new_string[18]
            'a' == 'a' → MATCH

        Move:
            l = 3, r = 17

    --------------------------------------------------

    ... (continues — every pair matches as the pointers move inward) ...

    --------------------------------------------------

    Final Iteration:
        l = 10, r = 10
        Loop condition l < r is False → exit loop.

    Final Check:
        return True

        This means:
            Every pair of characters matched from both ends inward,
            so the cleaned string is a palindrome.






---
Q: Why is the space complexity O(N)?

A: Because we store the cleaned version of the input in extra memory.

  • `chars` holds up to N valid characters (worst case: every char is kept).
  • `new_string` from `"".join(chars)` stores up to N characters too.
  • Pointer variables (`l`, `r`) are just O(1).

  • Extra memory grows with input size → O(N) space.



---
Q: Why can't a string be changed in place?

A: Because strings in Python are immutable — once created, they cannot be modified.

  • `new_string += c` does NOT edit the old string — it creates a brand-new one.
  • That's why building a string in a loop with `+=` can get slow.
  • Use a list + `"".join()` when you need to build a string piece by piece.
"""




# ––––––––––––––––––––––––––––––––––––––––––––––––
# 🧠 First Time? Thoughts → Code

"""
Read the problem (10 sec)
    • Check if a string is a palindrome after removing non-alphanumeric chars and lowercasing.
    • Key hint: "removing" and "lowercase" → you need a clean version of the string first.

Start naive (totally fine)
    • Clean the string, reverse it, compare: cleaned == cleaned[::-1]
    • Works. O(N). Perfectly valid.

The one insight that unlocks the two-pointer version
    • A palindrome is symmetric — first char = last char, second = second-to-last, etc.
    • Instead of building a reversed copy, walk inward from both ends.
    • If every pair matches, it's a palindrome. If any pair fails, return False immediately.
    • Early exit = skip checking the rest once you find a mismatch.

Thought → line of code
    chars = []
        → I need a place to collect valid characters. Start with an empty list.

    if c.isalnum()
        → The problem says "only letters and numbers." This is the filter.

    chars.append(c.lower())
        → "A" and "a" should be treated the same. Lowercase and add to the list.

    new_string = "".join(chars)
        → Turn the list into one clean string in one pass.
        → List + join avoids the O(N²) trap of string += in a loop.

    l, r = 0, len(new_string) - 1
        → Two pointers at opposite ends of the cleaned string.

    while l < r
        → Stop when they meet or cross. If l == r, the middle char doesn't need a partner.

    if new_string[l] != new_string[r]: return False
        → First mismatch = not a palindrome. Done.

Memory hook (one sentence)
    • Collect valid chars → join into a string → squeeze inward from both ends.

Would you arrive at this cold?
    • Yes — this is one of the more intuitive problems.
    • "Build a clean string" is the obvious first step anyone would think of.
    • Two pointers from both ends is natural once you picture what a palindrome looks like.
    • The only non-obvious details: remembering .isalnum() exists, and list + join instead of +=.
    • list + join is bookkeeping for performance — the real insight is still filter + compare.
"""





# Solution 2: Build String → Reverse Compare (with list + join)
def is_palindrome(s):
    chars = []
    for c in s:
        if c.isalnum():
            chars.append(c.lower())
    cleaned = "".join(chars)

    return cleaned == cleaned[::-1]

"""
Time: O(N)
  - Let N = length of the input string s.

  - Step 1: Build cleaned string with list + join → O(N).
      • Scan s once → O(N).
      • Filter: c.isalnum() → O(1) per character.
      • Lowercase: c.lower() → O(1) per character.
      • chars.append() → O(1) per character.
      • "".join(chars) → one O(N) pass to build the final string.

  - Step 2: Reverse and compare → O(N).
      • cleaned[::-1] creates a reversed copy → O(N).
      • == compares character by character → O(N).

  - Overall: O(N).

Space: O(N)
  - chars stores up to N characters (worst case: every char is alphanumeric).
  - cleaned stores up to N characters.
  - cleaned[::-1] creates another N-character copy during comparison.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One pass to build cleaned string, then reverse and compare in linear time.

Space: O(N)
  - Cleaned string plus a temporary reversed copy (uses more memory than two pointers).
"""



"""
---
Biggest Takeaway

This is one of the most important Python performance lessons:

    string += char

    inside a loop is usually bad.

Instead use:

    chars.append(char)
    "".join(chars)

    because lists append in O(1) amortized time.

"""












# ––––––––––––––––––––––––––––––––––––––––––––––––––
# MY OLD SOLUTION
# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Simple Palindrome Check (Build String → Two Pointers)

def is_palindrome(s):
    new_string = ""
    
    for c in s:
        if c.isalpha() or c.isdigit():   
            new_string += c.lower()  
    
    # Check if the new string reads the same forwards and backwards
    l = 0
    r = len(new_string) - 1
    
    while l < r:
        if new_string[l] != new_string[r]:
            return False
        l += 1
        r -= 1
        
    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))  # Output: True


"""
---
Note: new_string += c
    • On paper: each += copies the whole string → O(N²).
    • In CPython (normal Python): usually optimized to O(N) in practice.
    • Interview-safe: say O(N). list + join is the cleaner fix.


---
Time: O(N)
  - Let N = length of the input string s.
  
  - Step 1: Build a cleaned string by scanning s once → O(N).
      • Filter: c.isalpha() / c.isdigit() → O(1) per character.
      • Lowercase: c.lower() → O(1) per character.

      • Note: new_string += c copies the entire string each 
      time (strings are immutable).
        Technically O(N) per append → O(N²) total.
        Python often optimizes this away, and list + join 
        avoids it entirely.
        For interviews: safe to say O(N).

      • See note above on += (naive O(N²), CPython usually O(N)).

  - Step 2: Two pointers scan new_string from both ends → at most N/2 comparisons → O(N).
  - Overall: O(N).

Space: O(N)
  - new_string stores up to N characters (worst case: every char is alphanumeric).
  - Pointer variables (l, r) → O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - One pass to build cleaned string, one pass to compare from both ends.

Space: O(N)
  - Cleaned string can be as long as the original input.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Why += on Strings is O(N²) and How List + Join Fixes It

# String += (copies entire string each time)
new_string = ""
new_string += "a"   # creates "a"          (copies 1 char)
new_string += "b"   # creates "ab"         (copies 2 chars)
new_string += "c"   # creates "abc"        (copies 3 chars)
# Each += rebuilds from scratch → 1 + 2 + 3 + ... + N = O(N²)


# List + join (appends in place, joins once)
chars = []
chars.append("a")   # ["a"]               (O(1))
chars.append("b")   # ["a", "b"]          (O(1))
chars.append("c")   # ["a", "b", "c"]     (O(1))
result = "".join(chars)  # "abc"           (one O(N) pass)
# Total: N appends at O(1) + one join at O(N) = O(N)


"""
---
Q: Why += on Strings is O(N²)

The code above shows why:
    • Each += rebuilds the entire string from scratch (strings are immutable).
    • List + join appends in O(1), then builds the final string once.

Think of it like writing on paper.

You have 5 letters to add: a, b, c, d, e

But the rule is: every time you add a letter, you throw away
the old paper and rewrite everything from scratch on a new sheet.

    Round 1: Write "a"         → wrote 1 letter
    Round 2: Write "ab"        → wrote 2 letters
    Round 3: Write "abc"       → wrote 3 letters
    Round 4: Write "abcd"      → wrote 4 letters
    Round 5: Write "abcde"     → wrote 5 letters

How many total letters did your hand write?

    1 + 2 + 3 + 4 + 5 = 15


For N letters, the total is:

    1 + 2 + 3 + ... + N

    This is a famous math formula:

        N × (N + 1)
        ───────────
             2

    Example with N = 5:

        5 × 6       30
        ─────   =   ──   =   15  ✓  (matches our count above)
          2           2

    Example with N = 100:

        100 × 101     10100
        ─────────  =  ─────  =  5050 total letters written
            2            2

    In Big-O we drop constants and lower terms:

        N × (N + 1)       N² + N       N²
        ───────────   =   ──────   ≈   ──   =   O(N²)
             2               2          2

    The /2 is just part of the formula — Big-O ignores it.


Why NOT N³?
    • N³ would mean: each round you rewrite the page N times.
    • But you don't — you rewrite it ONCE per round.
    • Each rewrite just gets a little longer (1, 2, 3, ... N).
    • Add them up → N²


TLDR:
    • N rounds of rewriting
    • Each rewrite costs 1, 2, 3, ... up to N
    • Sum = N(N+1)/2 = O(N²)
"""
