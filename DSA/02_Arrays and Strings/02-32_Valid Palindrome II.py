# 680. Valid Palindrome II
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

Example 3:
    Input: s = "abc"
    Output: false
    
Constraints:
    1 <= s.length <= 10⁵
    s consists of lowercase English letters.

Solution: https://leetcode.com/problems/valid-palindrome-ii/

Neetcode: https://neetcode.io/solutions/valid-palindrome-ii

"""


# Solution 1: Two Pointers + Skip-One Helper  ← memorize this one
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1

        return True


solution = Solution()
s = "aba"
print(solution.validPalindrome(s))
# Output: True

s = "abca"
print(solution.validPalindrome(s))
# Output: True → mismatch at 'b' vs 'c'; skip 'c' and "aba" is a palindrome

s = "abc"
print(solution.validPalindrome(s))
# Output: False → skip 'a' → "bc" no; skip 'c' → "ab" no


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):          # Helper: is this range a palindrome?
            while l < r:                  # Keep going until pointers meet
                if s[l] != s[r]:          # Ends don't match
                    return False          # Not a palindrome
                l += 1                    # Move left inward
                r -= 1                    # Move right inward
            return True                   # Every pair matched

        l = 0                             # Left pointer at the start
        r = len(s) - 1                    # Right pointer at the end

        while l < r:                      # Walk inward from both ends
            if s[l] != s[r]:              # First mismatch — one free delete
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)  # Skip left or skip right
            l += 1                        # Ends match — move left in
            r -= 1                        # Ends match — move right in

        return True                       # Already a palindrome — nothing to delete

"""
Time: O(N)
  - Let N = length of the string s.
  - Main loop: two pointers walk inward from both ends → at most N/2 comparisons → O(N).
  - On the first mismatch, we call is_palindrome at most twice (skip left, then skip right if needed).
  - Each helper scan checks the leftover range once → O(N) each.
  - Combined: O(N) + O(N) + O(N) = O(N).
  - We only get one free delete, so we never restart from the beginning → not O(N²).
  - Overall: O(N).

Space: O(1)
  - Only integer pointers (l, r) and the helper's own l, r.
  - No extra list, string copy, or recursion.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - One inward pass, then at most two extra palindrome checks on the leftover.

Space: O(1)
  - Only pointer variables are used.


---
Most IMPORTANT thing to Understand:

    • A palindrome reads the same forwards and backwards.

    • We may delete at most one character — zero deletes is also fine.

    • Walk inward from both ends. Matching pairs are fine.

    • On the first mismatch, try skipping the left character OR the right character.

    • If either leftover range is a palindrome, return True.

    • is_palindrome(l, r) is the normal palindrome check on a range — no extra deletes.

---
Why this code Works:

    • Two pointers:
        • l starts at the beginning, r starts at the end.
        • Matching ends → move both inward.
        • First mismatch → we have used our one free delete.

    • The helper:
        • is_palindrome(l + 1, r) skips s[l].
        • is_palindrome(l, r - 1) skips s[r].
        • Each helper is a normal palindrome check — if it finds another mismatch, that range fails.

    • Why try both:
        • We do not know which character is the extra one.
        • Example "abca": skip 'b' → "aca", or skip 'c' → "aba". Either works.

    • Efficiency:
        • One inward pass, then at most two extra scans of the leftover.
        • Time: O(N). Space: O(1).

    • Intuition:
        • Fold the string in half like a palindrome check.
        • One pair does not line up → you get one mulligan: throw out the left letter or the right letter, then keep folding.

---
TLDR:

    • Walk inward from both ends. On the first mismatch, skip left or skip right — if either leftover is a palindrome, the answer is True.


---
Quick Example Walkthrough:

    s = "abca"

    Step 1: Start
        l = 0 ('a'), r = 3 ('a')

    Step 2: Walk inward
        • 'a' == 'a' → match, move in
        • 'b' != 'c' → first mismatch, one free delete

    Step 3: Try both skips
        • Skip left ('b'): leftover "aca" → palindrome → True
        • Skip right ('c') is not needed (or short-circuits), but "aba" would also work

    Final Answer: True


---
Quick Example Walkthrough:

    s = "aba"

    Step 1: Start
        l = 0 ('a'), r = 2 ('a')

    Step 2: Walk inward
        • 'a' == 'a' → match, move in
        • l = 1, r = 1 → pointers meet at 'b'

    Step 3: No mismatch
        • Already a palindrome — nothing to delete

    Final Answer: True


---
Quick Example Walkthrough:

    s = "abc"

    Step 1: Start
        l = 0 ('a'), r = 2 ('c')

    Step 2: Walk inward
        • 'a' != 'c' → first mismatch, one free delete

    Step 3: Try both skips
        • Skip left ('a'): leftover "bc" → not a palindrome
        • Skip right ('c'): leftover "ab" → not a palindrome

    Final Answer: False


---
Full Example Walkthrough:

    s = "abca"
        0: a
        1: b
        2: c
        3: a

    Starting State:
        l = 0  →  s[0] = "a"
        r = 3  →  s[3] = "a"

    Loop Iteration 1:
        Compare:
            s[l] == s[r]
            "a" == "a" → MATCH

        Since they match:
            l += 1
            r -= 1

        Now:
            l = 1
            r = 2

        Current state:
            l points at s[1] = "b"
            r points at s[2] = "c"

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            "b" == "c" → NO MATCH

        First mismatch — one free delete.

        return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
             = is_palindrome(2, 2) or is_palindrome(1, 1)

        Helper A — skip left (drop "b"):
            is_palindrome(2, 2)
            l = 2, r = 2
            l < r is False (same index — one character "c")
            → True

        Because Helper A is True, `or` stops here.
        (Helper B would skip "c" and check "b" — also True, but we do not need it.)

    --------------------------------------------------

    Final Check:
        return True

        This means:
            After deleting at most one character, the string can read the same forwards and backwards.


---
Overview for Each Iteration
Input: s = "abca"

Walk inward. On first mismatch, skip left or skip right.

Phase 1: Walk inward
l | r | s[l] | s[r] | match? | Action
--|---|------|------|--------|------------------
0 | 3 | a    | a    | Yes    | l++, r--
1 | 2 | b    | c    | No     | one free delete

Phase 2: Skip left — is_palindrome(2, 2)
l | r | s[l] | s[r] | result
--|---|------|------|---------------------------
2 | 2 | c    | c    | l < r is False → True

Final: True (skip 'b' works; `or` stops)


---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Can s become a palindrome after deleting at most one character? (Zero deletes is also fine.)

    • n ≤ 10⁵ → must be O(N). Trying every deletion will time out.

Start naive (totally fine)
    • For each index i, delete s[i] and check if the leftover is a palindrome. Also check the original.

    • O(N²). Say that out loud first if you're stuck.

The one insight that unlocks the optimal code
    • You do not need to try every index.

    • Walk inward like a normal palindrome. Matching pairs are already fine.

    • The extra character shows up at the first mismatch — it is either the left one or the right one.

    • Skip left, or skip right. If either leftover is a palindrome, you are done. No second delete.

Why two pointers?
    • A palindrome is symmetric, so the ends must match as you fold inward.

    • The first mismatch is the only place worth spending your one delete.

    • Greedy "pick the side that looks better" is wrong — you have to try both.

Thought → line of code
    • `def is_palindrome(l, r)`
        → Normal palindrome check on a range. No extra delete inside the helper.

    • `l = 0` / `r = len(s) - 1`
        → Same start as Valid Palindrome.

    • `while l < r`
        → Fold until the pointers meet.

    • `if s[l] != s[r]`
        → First mismatch. This is the one free delete.

    • `return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)`
        → NOT instinct. Skip left OR skip right. Don't guess which character is extra.
        → `or` means "either skip is enough."

    • `l += 1` / `r -= 1`
        → Ends matched. Keep folding. Bookkeeping.

    • `return True`
        → Never mismatched. Already a palindrome.

Memory hook (one sentence)
    • Palindrome check with one life: on the first mismatch, skip left or skip right.

Would you arrive at this cold?
    • Immediately: try deleting each character. That is the natural first answer.

    • After "n is 10⁵, I already know Valid Palindrome": two pointers from both ends.

    • What you would NOT invent on instinct: the `or` line that tries both skips. Greedy pick-one fails. That is the line you study.
"""







# Solution 2: Two Pointers + Slice Remaining
# Walk inward. On mismatch, delete left or right and check the leftover string against its reverse.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_left = s[l + 1 : r + 1]   # drop s[l]
                skip_right = s[l : r]          # drop s[r]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            l += 1
            r -= 1

        return True


solution = Solution()
s = "abca"
print(solution.validPalindrome(s))
# Output: True

"""
Intuition
    • Walk inward. On the first mismatch, try deleting the left letter or the right letter.
    • Check each leftover by comparing it to its reverse.
      Example: "abca" → drop 'b' → "aca", or drop 'c' → "aba".
    • Same idea as Solution 1, but here you build a new string instead of moving pointers.
      That copy is why space is O(N). Memorize Solution 1.

How it works
    • Walk inward from both ends.
    • Mismatch → skip_left = s[l+1:r+1] (drop s[l]) or skip_right = s[l:r] (drop s[r]).
    • [::-1] is the palindrome check.
    • Either skip works → True. Loop finishes with no mismatch → already a palindrome.

Interview Answer: Worst Case

Time: O(N)
  - One inward pass, then at most two slice-and-reverse palindrome checks.

Space: O(N)
  - Each skip builds a new string copy (and its reverse).


---
Quick Example Walkthrough:

    s = "abca"

    Step 1: Start
        l = 0 ('a'), r = 3 ('a')

    Step 2: Walk inward
        • 'a' == 'a' → match, move in
        • 'b' != 'c' → first mismatch

    Step 3: Try both leftovers
        • skip_left  (drop 'b') = "aca"  → "aca" == "aca" → True
        • skip_right (drop 'c') is not needed (`or` stops), but "aba" would also work

    Final Answer: True
"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — try deleting each character
# Try deleting every character. Too slow at 100,000 letters. The two-pointer solutions only delete at the first mismatch.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            newS = s[:i] + s[i + 1:]
            if newS == newS[::-1]:
                return True

        return False


solution = Solution()
s = "aba"
print(solution.validPalindrome(s))
# Output: True

s = "abca"
print(solution.validPalindrome(s))
# Output: True → delete 'b' → "aca", or delete 'c' → "aba"

s = "abc"
print(solution.validPalindrome(s))
# Output: False → "bc", "ac", "ab" are all not palindromes

"""
Intuition
    • Try every delete. If any leftover is a palindrome, return True.
    • This works, but the input can be n = 10⁵ means 100,000 letters.
      That is 100,000 deletions, and each deletion scans ~100,000 letters.
      100,000 × 100,000 = 10 billion steps → Time Limit Exceeded (TLE).
    • The two-pointer solutions only try a deletion when two letters first fail to match.

How it works
    • Already a palindrome? return True.
    • For each i, newS = s without s[i].
    • newS == newS[::-1]? return True.
    • Else False.

Interview Answer: Worst Case

Time: O(N²)
  - For each of N characters, rebuild the string and check if it is a palindrome.

Space: O(N)
  - Each deletion makes a new copy of the leftover string (newS).


---
Quick Example Walkthrough:

    s = "abca"

    Step 1: Already a palindrome?
        "abca" == "acba" → No

    Step 2: Try deleting each character
        • i = 0  delete 'a'  newS = "bca"  "bca" == "acb" → No
        • i = 1  delete 'b'  newS = "aca"  "aca" == "aca" → Yes

    Final Answer: True
"""
