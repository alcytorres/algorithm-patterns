# Example 2: Longest Substring with At Most One "0"
"""
Finds the longest substring with at most one "0" by flipping at most one "0" to "1". 

In other words "what is the longest substring that contains at most one "0"?

Example:
    Input: s = "10101"
    Output: 3
    Explanation: "101" is the longest substring containing at most one "0".
"""

# Solution: Sliding Window: Shrink Window When Zero Count Exceeds Limit

def longest_substring_one_zero(s):
    l = zero_count = ans = 0        
        
    for r in range(len(s)): 
        if s[r] == "0":     
            zero_count += 1            
        
        while zero_count > 1:          
            if s[l] == "0":   
                zero_count -= 1        
            l += 1            
            
        ans = max(ans, r - l + 1)  
    
    return ans

s = "10101"
print(longest_substring_one_zero(s))
# Output: 3  →  Substring "101" (length 3) is the longest with at most one "0".


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 

def longest_substring_one_zero(s):
    l = 0            # Left edge of window
    zero_count = 0   # Count of zeros
    ans = 0          # Best length so far

    for r in range(len(s)):      # Expand window by moving right edge through the string
        if s[r] == "0":          # New character on the right is a zero
            zero_count += 1      # One more zero inside the window
            
        while zero_count > 1:     # Too many zeros — shrink from the left until at most one
            if s[l] == "0":       # Character leaving the window on the left is a zero
                zero_count -= 1   # Remove that zero from the count
            l += 1                # Move left edge right to shrink the window
            
        ans = max(ans, r - l + 1)  # Window is valid — maybe this is the longest so far
    
    return ans                    # Longest substring length with at most one "0"


"""
Time: O(N)
  - Let N = length of the string s.
  - Right pointer r moves through the string once (for loop) → O(N).
  - Left pointer l only moves forward; each character enters and leaves the window at most once.
  - Inner while loop shrinks the window when there are too many zeros — total work across all steps is O(N).
  - Overall: O(N).


Space: O(1)
  - Only a few integer variables: l, zero_count, ans, and loop index r.
  - No extra arrays or hash maps.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Sliding window: r scans the string once, and l moves forward at most N times total.
  - Each character is visited a constant number of times.

Space: O(1)
  - Only pointer and counter variables — no extra structures.
"""


"""
---
Most IMPORTANT thing to Understand:
    • We want the longest continuous substring that has at most one "0".

    • Think of a window from index l to index r — every substring we consider is inside this window.

    • zero_count tracks how many "0"s are currently inside the window.

    • r always moves right to grow the window (add the next character).

    • When zero_count becomes 2, the window is invalid — we move l right (shrink) until zero_count is 1 or less again.

    • Once the window is valid again, r - l + 1 is its length — ans keeps the best length we've seen.

---
Why this code Works:
    • Sliding window:
        • l = left edge of the current substring.
        • r = right edge (the for loop index).
        • The window is always s[l] through s[r].

    • When s[r] is "0":
        • Add it to the window and increase zero_count.

    • When zero_count > 1:
        • Too many zeros — remove s[l] from the window by moving l forward.
        • If s[l] was a "0", decrease zero_count.
        • Repeat until the window has at most one "0".

    • After the window is valid:
        • Update ans with the current window length (r - l + 1).

    • Efficiency:
        • r visits each index once.
        • l only moves forward, never backward — each character is added and removed at most once.
        • Time: O(N). Space: O(1).

    • Intuition:
        • Like stretching a rubber band from l to r across the string.
        • If you stretch too far and get two zeros, pull the left side in until you're allowed only one zero again.
        • Every valid window you see is a candidate for the answer.

---
TLDR:
    • r expands a window one character at a time; when there are more than one "0", l shrinks the window from the left until it's valid again, and ans stores the longest valid window length.


---
Quick Example Walkthrough:
    s = "10101"

    Step 1: Start with l = 0, zero_count = 0, ans = 0

    Step 2: Move r through the string and grow/shrink the window
        • r=0, add "1" → zero_count=0, window "1", ans=1
        • r=1, add "0" → zero_count=1, window "10", ans=2
        • r=2, add "1" → zero_count=1, window "101", ans=3
        • r=3, add "0" → zero_count=2 → shrink: drop "1" at l=0, then drop "0" at l=1 → window "10", ans stays 3
        • r=4, add "1" → zero_count=1, window "101", ans stays 3

    Step 3: Return ans

    Final Answer: 3 (substring "101" at indices 0–2, or again at indices 2–4)


---
Full Example Walkthrough:
    s = "10101"

    Starting State:
        l = 0
        zero_count = 0
        ans = 0

        Window is empty; r will start at 0.

    Loop Iteration 1 (r = 0):
        Add character:
            s[0] = "1" → not a zero, zero_count stays 0

        Shrink check:
            zero_count (0) > 1? No → skip while loop

        Update ans:
            r - l + 1 = 0 - 0 + 1 = 1
            ans = max(0, 1) = 1

        Current state:
            Window: s[0] = "1" (length 1)
            l = 0, zero_count = 0, ans = 1

    --------------------------------------------------

    Loop Iteration 2 (r = 1):
        Add character:
            s[1] = "0" → zero_count = 1

        Shrink check:
            zero_count (1) > 1? No → skip while loop

        Update ans:
            r - l + 1 = 1 - 0 + 1 = 2
            ans = max(1, 2) = 2

        Current state:
            Window: s[0:2] = "10" (length 2)
            l = 0, zero_count = 1, ans = 2

    --------------------------------------------------

    Loop Iteration 3 (r = 2):
        Add character:
            s[2] = "1" → not a zero, zero_count stays 1

        Shrink check:
            zero_count (1) > 1? No → skip while loop

        Update ans:
            r - l + 1 = 2 - 0 + 1 = 3
            ans = max(2, 3) = 3

        Current state:
            Window: s[0:3] = "101" (length 3) ← best so far
            l = 0, zero_count = 1, ans = 3

    --------------------------------------------------

    Loop Iteration 4 (r = 3):
        Add character:
            s[3] = "0" → zero_count = 2

        Shrink check:
            zero_count (2) > 1? Yes → enter while loop

            Shrink step 1:
                s[l] = s[0] = "1" → not a zero, only l += 1
                l = 1, zero_count still 2

            Shrink step 2:
                s[l] = s[1] = "0" → zero_count -= 1 → zero_count = 1
                l += 1 → l = 2
                zero_count (1) > 1? No → exit while loop

        Update ans:
            r - l + 1 = 3 - 2 + 1 = 2
            ans = max(3, 2) = 3  (keep 3)

        Current state:
            Window: s[2:4] = "10" (length 2)
            l = 2, zero_count = 1, ans = 3

    --------------------------------------------------

    Loop Iteration 5 (r = 4):
        Add character:
            s[4] = "1" → not a zero, zero_count stays 1

        Shrink check:
            zero_count (1) > 1? No → skip while loop

        Update ans:
            r - l + 1 = 4 - 2 + 1 = 3
            ans = max(3, 3) = 3

        Current state:
            Window: s[2:5] = "101" (length 3)
            l = 2, zero_count = 1, ans = 3

    --------------------------------------------------

    Final Check:
        return ans → 3

        This means:
            The longest substring with at most one "0" has length 3.
            Examples: "101" (indices 0–2) or "101" (indices 2–4).
"""


"""
Overview for Each Iteration
Input: s = "10101"

Sliding window: expand with r, shrink from l when zero_count > 1, update ans with valid window length.

r| s[r] |l|zeros| Action / Decision                | Window (s[l:r+1]) | ans
-|------|-|-----|----------------------------------|-------------------|----
0| 1    |0| 0   | add "1", valid                   | "1"               | 1
1| 0    |0| 1   | add "0", valid                   | "10"              | 2
2| 1    |0| 1   | add "1", valid                   | "101"             | 3
3| 0    |2| 1   | add "0" → shrink (drop s[0], s[1]) | "10"            | 3
4| 1    |2| 1   | add "1", valid                   | "101"             | 3

Final: 3
"""


"""
---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Find the longest **continuous** substring that has **at most one** `"0"`.

    • "Flip at most one zero" = same rule: the substring can contain 0 or 1 zero, not 2+.

    • You're maximizing **length**, not returning the substring itself.


Start naive (totally fine)
    • Try every start `i` and every end `j`, count zeros in `s[i:j+1]`, keep the max length when count ≤ 1.

    • Say out loud: "Check every substring."

    • Time: O(N²) — nested loops, maybe break inner loop once zeros > 1.


The one insight that unlocks the optimal code
    • You don't need a fresh scan for every new `i` — keep one window `[l … r]` and slide it.

    • Always grow `r` by one (add the next character).

    • Only when zeros > 1, move `l` right to kick characters out until the window is legal again.

    • `l` never moves backward → each index is added and removed at most once → O(N) total.


Why sliding window?
    • The answer is about a **substring** with a **count constraint** (zeros ≤ 1).

    • Expand right to try longer windows; shrink left only when the rule breaks — same pattern as "longest with at most K of something."

    • Brute force re-counts from scratch each time; the window **reuses** work from the previous step.


Thought → line of code
    • `l = zero_count = ans = 0`
        → Left edge of window, how many zeros inside, best length seen.

    • `for r in range(len(s))`
        → Right edge always steps forward — "try including this character."

    • `if s[r] == "0": zero_count += 1`
        → New character might be the one that breaks the rule.

    • `while zero_count > 1:`
        → Window illegal — keep shrinking from the left until at most one zero. (Not obvious: might need **multiple** `l` steps if you drop a `"1"` first.)

    • `if s[l] == "0": zero_count -= 1`
        → Only subtract when a zero actually leaves the window.

    • `l += 1`
        → Drop `s[l]` from the window (shrink).

    • `ans = max(ans, r - l + 1)`
        → Window is valid now; `r - l + 1` is its length — maybe update the record.


Memory hook (one sentence)
    • Grow `r` every step; if more than one zero, peel from `l` until legal, then save the longest valid length.


Would you arrive at this cold?
    • Immediately: nested loops O(N²) — totally fine first answer.

    • After "longest substring + limit on what's inside": sliding window is a known family, but you still have to invent `l`, `zero_count`, and the shrink loop.

    • Easy to miss: `while` not `if` on shrink — dropping one `"1"` doesn't fix two zeros.

    • Bookkeeping: `zero_count`, `r - l + 1`, `ans = max(...)` — pattern vocabulary once you've seen one window problem.

    • Real insight: one window, expand right, shrink left only when broken — that's what beats checking every substring again.
"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — Try every substring (nested loops)

def longest_substring_one_zero_bruteforce(s):
    ans = 0
    n = len(s)

    for i in range(n):              # start index of substring
        zero_count = 0
        for j in range(i, n):       # end index of substring
            if s[j] == "0":
                zero_count += 1

            if zero_count <= 1:
                ans = max(ans, j - i + 1)
            else:
                break               # too many zeros — stop extending from this start

    return ans


s = "10101"
print(longest_substring_one_zero_bruteforce(s))
# Output: 3


"""
Time: O(N²)
  - Let N = length of the string s.

  - Step 1: Outer loop tries every start index i → O(N).

  - Step 2: Inner loop extends end index j from i → O(N) per i.
      • Count zeros as we extend → O(1) per step.
      • Break early once zero_count > 1.

  - Combined: O(N × N).
  - Overall: O(N²).


Space: O(1)
  - Only ans, zero_count, and loop indices i, j.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N²)
  - Every start index i can extend j up to N times in the worst case.

Space: O(1)
  - Only a few counter and index variables.


---
Overview for Each Iteration
s = "10101"

    i = 0 (start at index 0)
        j = 0 → substring "1", zeros = 0 → ans = 1
        j = 1 → substring "10", zeros = 1 → ans = 2
        j = 2 → substring "101", zeros = 1 → ans = 3
        j = 3 → substring "1010", zeros = 2 → break (too many zeros)

    i = 1 (start at index 1)
        j = 1 → "0", zeros = 1 → length 1, ans stays 3
        j = 2 → "01", zeros = 1 → length 2, ans stays 3
        j = 3 → "010", zeros = 2 → break

    i = 2 (start at index 2)
        j = 2 → "1", zeros = 0 → length 1
        j = 3 → "10", zeros = 1 → length 2
        j = 4 → "101", zeros = 1 → length 3, ans stays 3

    i = 3, i = 4 → shorter windows only; none beat length 3

    return ans → 3

Final: 3
"""
