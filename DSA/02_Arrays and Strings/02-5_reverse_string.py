# 344. Reverse String
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output:    ["o","l","l","e","h"]
 
Solution: https://leetcode.com/problems/reverse-string/editorial/
"""

# Solution: Two Pointers In-Place Reverse

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s

s = ["h", "e", "l", "l", "o"]
print(reverseString(s))  
# Output: ["o", "l", "l", "e", "h"]

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def reverseString(s):
    left = 0                 # Initialize left pointer at start of list
    right = len(s) - 1       # Initialize right pointer at end of list
    
    while left < right:               # Continue until pointers meet
        s[left], s[right] = s[right], s[left]  # Swap elements at left and right pointers
        left += 1            # Move left pointer inward
        right -= 1           # Move right pointer inward
    
    return s                 # Return the reversed list

# Complexity
# Time: O(n) - Performs n/2 swaps to reverse n elements.
# Space: O(1) - Uses two pointers, modifying list in-place.

# Output: ["o","l","l","e","h"] - Returns the list with characters reversed in-place.


"""
Time: O(N)
  - Let N = length of the input list s.
  - Two pointers (left, right) move toward each other from both ends.
  - Each pair of characters is swapped once → O(1) per swap.
  - Total of N/2 swaps → O(N) overall.

Space: O(1)
  - The reversal is done in-place using only two pointer variables.
  - No additional data structures are created.
  - Overall: O(1)

  
Interview Answer: Worst Case

Time: O(N)
  - Each character is swapped once in a single pass.

Space: O(1)
  - In-place reversal, constant extra space.


---
Overview for Each Iteration
Input: s = ["h", "e", "l", "l", "o"]

Step: Reverse string in-place using two pointers
l   | r   | s[l] | s[r] | l < r | Action          | s
----|-----|------|------|-------|-----------------|---------------
0   | 4   | h    | o    | True  | Swap s[0], s[4] | [o, e, l, l, h]
1   | 3   | e    | l    | True  | Swap s[1], s[3] | [o, l, l, e, h]
2   | 2   | l    | l    | False | Exit loop       | [o, l, l, e, h]

Final: ["o", "l", "l", "e", "h"]



---
Most IMPORTANT thing to Understand:
    • We need to reverse the list in-place — swap characters inside the same array, no extra list.

    • Two pointers start at opposite ends: left at the start, right at the end.

    • Each swap puts one character in its final reversed position.

    • When left >= right, every pair has been swapped and the string is reversed.

---
Why this code Works:
    • Two pointers:
        • left = index from the front (starts at 0).
        • right = index from the back (starts at len(s) - 1).

    • Each iteration:
        • Swap s[left] and s[right].
        • Move left forward and right backward.

    • Why swapping works:
        • First swap puts the last character where the first was, and the first where the last was.
        • Each inward step fixes the next outer pair.
        • The middle character (if odd length) stays put — left == right, loop stops.

    • Efficiency:
        • One pass, N/2 swaps.
        • Time: O(N).
        • Space: O(1) — only two pointer variables.

    • Intuition:
        • Like two people at opposite ends of a line swapping name tags and stepping inward until they meet in the middle.

---
TLDR:
    • Swap the outermost pair, then the next pair inward, until the pointers meet. After N/2 swaps, the list is reversed in-place.

---
Quick Example Walkthrough:
    s = ["h", "e", "l", "l", "o"]

    Step 1: Initialize
        left = 0, right = 4

    Step 2: Swap and move inward
        • Swap s[0]='h' and s[4]='o' → ["o", "e", "l", "l", "h"], left=1, right=3
        • Swap s[1]='e' and s[3]='l' → ["o", "l", "l", "e", "h"], left=2, right=2
        • left < right? 2 < 2 → False → exit loop

    Final Answer: ["o", "l", "l", "e", "h"]

---
Full Example Walkthrough:
    s = ["h", "e", "l", "l", "o"]

    Starting State:
        left = 0
        right = 4

        left points at s[0] = "h"
        right points at s[4] = "o"

        s = ["h", "e", "l", "l", "o"]

    Loop Iteration 1:
        Check:
            left < right → 0 < 4 → True

        Swap:
            s[0], s[4] = s[4], s[0]
            "h" ↔ "o"

        Move pointers:
            left = 1
            right = 3

        Current state:
            s = ["o", "e", "l", "l", "h"]
            left points at s[1] = "e"
            right points at s[3] = "l"

    --------------------------------------------------

    Loop Iteration 2:
        Check:
            left < right → 1 < 3 → True

        Swap:
            s[1], s[3] = s[3], s[1]
            "e" ↔ "l"

        Move pointers:
            left = 2
            right = 2

        Current state:
            s = ["o", "l", "l", "e", "h"]
            left points at s[2] = "l"
            right points at s[2] = "l"

    --------------------------------------------------

    Loop Iteration 3:
        Check:
            left < right → 2 < 2 → False

        Loop exits — no swap this round.

    --------------------------------------------------

    Final Check:
        Return s → ["o", "l", "l", "e", "h"]

        Every character is in reversed order, done in-place with O(1) extra space.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Shortcut solution

def reverseString(s):
    s.reverse    
    return s

s = ["h","e","l","l","o"]
print(reverseString(s))  # Output: ["o","l","l","e","h"]

# Time: O(n) - Python's list.reverse() method processes n elements, performing n/2 swaps internally, each O(1).
# Space: O(1) - Modifies the input array in-place, using only a constant amount of auxiliary space for internal operations.



