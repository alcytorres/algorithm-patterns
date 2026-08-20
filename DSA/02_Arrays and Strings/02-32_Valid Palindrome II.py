# 680. Valid Palindrome II
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'b' or 'c'.

Example 3:
    Input: s = "abc"
    Output: false
    
Constraints:
    1 <= s.length <= 10⁵
    s consists of lowercase English letters.

Solution: https://leetcode.com/problems/valid-palindrome-ii/

Neetcode: https://neetcode.io/solutions/valid-palindrome-ii

"""


# Solution 1: Two Pointers + Slice Remaining  ← memorize this one
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1 : r + 1]   # drop s[l]
                skipR = s[l : r]           # drop s[r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1

        return True


solution = Solution()
s = "aaaaza"
print(solution.validPalindrome(s))
# Output: True → skipL "aaz" fails; skipR drops 'z' → "aaa"

s = "aba"
print(solution.validPalindrome(s))
# Output: True → never mismatches; already a palindrome

s = "abc"
print(solution.validPalindrome(s))
# Output: False → skipL "bc" no; skipR "ab" no

s = "abca"
print(solution.validPalindrome(s))
# Output: True → mismatch 'b' vs 'c'; skipL works first ("aca"); skipR ("aba") also works


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0                             # Left pointer at the start
        r = len(s) - 1                    # Right pointer at the end

        while l < r:                      # Walk inward from both ends
            if s[l] != s[r]:              # First mismatch — one free delete
                skipL = s[l + 1 : r + 1]  # Drop s[l]. r+1 keeps s[r] (stop is exclusive)
                skipR = s[l : r]          # Drop s[r]. stop is r, so s[r] is not included
                return skipL == skipL[::-1] or skipR == skipR[::-1]  # If skipping the left letter gives a palindrome, return True; otherwise check skipping the right letter

            l += 1                        # Characters match — move left pointer inward
            r -= 1                        # Characters match — move right pointer inward

        return True                       # Already a palindrome — nothing to delete

"""
Time: O(N)
  - Let N = length of the string s.
  - Main loop: two pointers walk inward from both ends → at most N/2 comparisons → O(N).
  - On the first mismatch, we build at most two leftover strings and compare each to its reverse.
  - Each slice-and-reverse checks the leftover once → O(N) each.
  - Combined: O(N) + O(N) + O(N) = O(N).
  - We only get one free delete, so we never restart from the beginning → not O(N²).
  - Overall: O(N).

Space: O(N)
  - skipL and skipR are new string copies of the leftover.
  - Each [::-1] builds another copy.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - One inward pass, then at most two slice-and-reverse palindrome checks.

Space: O(N)
  - Each skip builds a new string copy (and its reverse).


---
Most IMPORTANT thing to Understand:

    • A palindrome reads the same forwards and backwards.

    • We may delete at most one character — zero deletes is also fine.

    • Walk inward from both ends. Matching pairs are fine.

    • On the first mismatch, try deleting the left character OR the right character.

    • skipL and skipR are the two leftovers. If either one is a palindrome, return True.

    • Both leftovers are always built. `or` only skips the second CHECK.

---
Why this code Works:

    • Two pointers:
        • l starts at the beginning, r starts at the end.
        • Matching ends → move both inward.
        • First mismatch → we have used our one free delete.

    • The two leftovers:
        • skipL = s[l + 1 : r + 1] drops s[l]. r + 1 keeps s[r], because stop is exclusive.
        • skipR = s[l : r] drops s[r]. stop is r, so s[r] is left out.
        • [::-1] reverses a string, so `x == x[::-1]` is the palindrome check.

    • Why try both:
        • We do not know which character is the extra one.
        • Example "abca": drop 'b' → "aca", or drop 'c' → "aba". Either works.

    • Why only the letters between l and r:
        • Everything outside l..r already matched on the way in.
        • Those pairs are settled, so the leftover only needs to cover the middle.

    • Efficiency:
        • One inward pass, then at most two slice-and-reverse checks.
        • Time: O(N). Space: O(N) because of the copies.

    • Intuition:
        • Fold the string in half like a palindrome check.
        • One pair does not line up → you get one mulligan: throw out the left letter or the right letter, then read what is left.

---
TLDR:

    • Walk inward from both ends. On the first mismatch, delete left or delete right — if either leftover string is a palindrome, the answer is True.


---
Full Example Walkthrough:

    s = "aaaaza"
        0: a
        1: a
        2: a
        3: a
        4: z
        5: a

    Starting State:
        l = 0  →  s[0] = "a"
        r = 5  →  s[5] = "a"

    Loop Iteration 1:
        Compare:
            "a" == "a" → MATCH

        Since they match:
            l += 1
            r -= 1

        Now:
            l = 1  →  "a"
            r = 4  →  "z"

        The outer "a"s already matched. We do not check them again.

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            "a" vs "z" → NO MATCH

        First mismatch — one free delete.

        We build BOTH leftovers:
            skipL = s[l + 1 : r + 1] = s[2:5] → "aaz"    drop 'a' at l
            skipR = s[l : r]         = s[1:4] → "aaa"    drop 'z'

        Then the check:
            return skipL == skipL[::-1] or skipR == skipR[::-1]
                 = "aaz" == "zaa"       or "aaa" == "aaa"
                 = False                or True

        skipL failed, so `or` does check skipR.
        skipR was still built. Building and checking are two different steps.

        Whole-string picture: delete 'z' → "aaaaa"

    --------------------------------------------------

    Final Check:
        return True

        This means:
            Deleting the left letter failed. Deleting 'z' worked. One delete is enough.


    ---
    Overview for Each Iteration
    Input: s = "aaaaza"

    Walk inward. On first mismatch, build both leftovers and check them.

    Phase 1: Walk inward
    l | r | s[l] | s[r] | match? | Action
    --|---|------|------|--------|------------------
    0 | 5 | a    | a    | Yes    | l++, r--
    1 | 4 | a    | z    | No     | one free delete

    Phase 2: Build both leftovers (l = 1, r = 4)
    name  | slice   | leftover | palindrome? | result
    ------|---------|----------|-------------|--------
    skipL | s[2:5]  | "aaz"    | "zaa" → no  | False
    skipR | s[1:4]  | "aaa"    | "aaa" → yes | True

    Final: True (skipL fails; skipR drops 'z')


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
        • We never build skipL or skipR

    Final Answer: True


---
Quick Example Walkthrough:

    s = "abc"
        0: a
        1: b
        2: c

    Step 1: Start
        l = 0 ('a'), r = 2 ('c')

    Step 2: Walk inward
        • 'a' != 'c' → first mismatch (no matching pair first)

    Step 3: Try both skips
        • skipL = s[1:3] = "bc" → "bc" != "cb" → no
        • skipR = s[0:2] = "ab" → "ab" != "ba" → no

        skipL failed, so `or` does check skipR. skipR also failed.

    Final Answer: False


---
Quick Example Walkthrough:

    s = "abca"

    Step 1: Start
        l = 0 ('a'), r = 3 ('a')

    Step 2: Walk inward
        • 'a' == 'a' → match, move in
        • 'b' != 'c' → first mismatch, one free delete

    Step 3: Try both skips
        • skipL = s[2:3] = "c" → palindrome → True
        • skipR is not needed (`or` skips the skipR CHECK), but "b" / "aba" would also work

        Whole-string picture: drop 'b' → "aca". Drop 'c' → "aba" (also works).

    Final Answer: True


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

    • Delete left, or delete right. If either leftover is a palindrome, you are done. No second delete.

Why two pointers?
    • A palindrome is symmetric, so the ends must match as you fold inward.

    • The first mismatch is the only place worth spending your one delete.

    • Greedy "pick the side that looks better" is wrong — you have to try both.

Thought → line of code
    • `l = 0` / `r = len(s) - 1`
        → Same start as Valid Palindrome.

    • `while l < r`
        → Fold until the pointers meet.

    • `if s[l] != s[r]`
        → First mismatch. This is the one free delete.

    • `skipL = s[l + 1 : r + 1]`
        → The leftover if we delete the left letter. r + 1 keeps s[r], because stop is exclusive.

    • `skipR = s[l : r]`
        → The leftover if we delete the right letter. stop is r, so s[r] is left out.

    • `return skipL == skipL[::-1] or skipR == skipR[::-1]`
        → NOT instinct. Delete left OR delete right. Don't guess which character is extra.
        → `or` means "either leftover is enough."

    • `l += 1` / `r -= 1`
        → Ends matched. Keep folding. Bookkeeping.

    • `return True`
        → Never mismatched. Already a palindrome.

Memory hook (one sentence)
    • Palindrome check with one life: on the first mismatch, delete left or delete right and read what is left.

Would you arrive at this cold?
    • Immediately: try deleting each character. That is the natural first answer.

    • After "n is 10⁵, I already know Valid Palindrome": two pointers from both ends.

    • What you would NOT invent on instinct: the `or` line that tries both leftovers. Greedy pick-one fails. That is the line you study.
"""








# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution 2: Two Pointers + Skip-One Helper
# Same idea, but a helper checks the leftover by index instead of copying it. O(1) space.
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

s = "aaaaza"
print(solution.validPalindrome(s))
# Output: True → skip left "aaz" fails; skip right drops 'z' → "aaa"

s = "abc"
print(solution.validPalindrome(s))
# Output: False → skip 'a' → "bc" no; skip 'c' → "ab" no

s = "abca"
print(solution.validPalindrome(s))
# Output: True → mismatch at 'b' vs 'c'; skip 'b' → "aca" (skip 'c' → "aba" also works)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):          # Helper: is s from index l to index r a palindrome?
            while l < r:                  # Keep going until the pointers meet
                if s[l] != s[r]:          # Two letters don't match
                    return False          # This range is not a palindrome
                l += 1                    # They matched — move left pointer inward
                r -= 1                    # They matched — move right pointer inward
            return True                   # Every pair matched

        l = 0                             # Left pointer at the start
        r = len(s) - 1                    # Right pointer at the end

        while l < r:                      # Walk inward from both ends
            if s[l] != s[r]:              # First mismatch — one free delete
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)  # If skipping the left letter gives a palindrome, return True; otherwise check skipping the right letter
            l += 1                        # Characters match — move left pointer inward
            r -= 1                        # Characters match — move right pointer inward

        return True                       # Already a palindrome — nothing to delete

"""
Intuition
    • Same walk as Solution 1: matching letters keep going, first mismatch is the problem spot.
    • Only two choices — remove the left letter or remove the right letter.
    • The difference: instead of copying the leftover into a new string, pass the start and end
      indexes to a helper. Same answer, no copy, so space is O(1).

Why this solution works
    • A palindrome has matching ends as you walk inward.
    • You may delete at most one letter.

    • Walk in from both ends.
    • Matching letters are fine — leave them.
    • First mismatch: one of those two letters is the extra one. You don't know which.
    • is_palindrome(l + 1, r) asks "is the leftover a palindrome if I drop the left letter?"
    • is_palindrome(l, r - 1) asks the same for the right letter.
    • The helper has no extra delete of its own — it is the plain palindrome check.

Interview Answer: Worst Case

Time: O(N)
  - One inward pass, then at most two extra palindrome checks on the leftover.

Space: O(1)
  - Only pointer variables are used.


---
Full Example Walkthrough:

    s = "aaaaza"
        0: a
        1: a
        2: a
        3: a
        4: z
        5: a

    Starting State:
        l = 0  →  s[0] = "a"
        r = 5  →  s[5] = "a"

    Loop Iteration 1:
        Compare:
            s[l] == s[r]
            "a" == "a" → MATCH

        Since they match:
            l += 1
            r -= 1

        Now:
            l = 1
            r = 4

        Current state:
            l points at s[1] = "a"
            r points at s[4] = "z"

        The outer "a"s already matched. We do not check them again.

    --------------------------------------------------

    Loop Iteration 2:
        Compare:
            "a" == "z" → NO MATCH

        First mismatch — one free delete.

        return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
             = is_palindrome(2, 4) or is_palindrome(1, 3)

        Helper A — skip left (drop s[1] = "a"):
            is_palindrome(2, 4)
            leftover of this range: "aaz"

            l = 2 ("a"), r = 4 ("z")
            "a" == "z" → NO MATCH
            Helper has no extra delete.
            → False

        Helper A failed, so `or` checks Helper B.

        Helper B — skip right (drop s[4] = "z"):
            is_palindrome(1, 3)
            leftover of this range: "aaa"

            l = 1 ("a"), r = 3 ("a")
            "a" == "a" → MATCH
            l += 1, r -= 1
            Now l = 2, r = 2 (pointers meet at "a")
            l < r is False
            → True

        Whole-string picture: delete "z" → "aaaaa"

    --------------------------------------------------

    Final Check:
        return True

        This means:
            Skip left failed. Skip right worked. One delete is enough.


    ---
    Overview for Each Iteration
    Input: s = "aaaaza"

    Walk inward. On first mismatch, skip left or skip right.

    Phase 1: Walk inward
    l | r | s[l] | s[r] | match? | Action
    --|---|------|------|--------|------------------
    0 | 5 | a    | a    | Yes    | l++, r--
    1 | 4 | a    | z    | No     | one free delete

    Phase 2a: Skip left — is_palindrome(2, 4) leftover "aaz"
    l | r | s[l] | s[r] | match? | result
    --|---|------|------|--------|--------
    2 | 4 | a    | z    | No     | False

    Phase 2b: Skip right — is_palindrome(1, 3) leftover "aaa"
    l | r | s[l] | s[r] | match? | result
    --|---|------|------|--------|---------------------------
    1 | 3 | a    | a    | Yes    | l++, r--
    2 | 2 | a    | a    | meet   | l < r is False → True

    Final: True (skip left fails; skip right drops 'z')


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
Q: Why does a helper function help here?

    • We need the same palindrome check twice: leftover after dropping the left letter, leftover after dropping the right letter.

    • The helper's only job is: "does s from index l to index r read the same both ways?" No extra delete.

    • The main function owns the special rule (one free delete). The helper is the normal palindrome check.

    • Passing l and r (indexes) means we do not copy the string. That is why this solution is O(1) space and Solution 1 is O(N).

---
Q: How would I arrive at a helper next time?

    • This is not a palindrome trick. A helper is just: "I have a small job I need to run more than once."

    • Write the obvious solution first. Then look for a chunk you are about to paste twice — same steps, only the inputs change (a different index, a different leftover, a different node).

    • Name that chunk in one sentence. If you can say it ("is this range a palindrome?", "is this path valid?"), it is a helper. The sentence becomes the function name. What changes becomes the arguments.

    • Split the jobs:
        • Main function = the special / one-time rule for this problem.
        • Helper = the boring, reusable check with no special rule.

    • If the repeated job is "look at part of the same list/string," pass indexes (l, r) instead of copying a slice. Same answer, less memory.

    • Signal to remember: same job, different inputs → helper. If you only need it once, keep it in the main function.
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
s = "abca"
print(solution.validPalindrome(s))
# Output: True → left to right hits 'b' first ("aca"); 'c' would also work ("aba")

s = "aba"
print(solution.validPalindrome(s))
# Output: True → original is already a palindrome (0 deletes)

s = "abc"
print(solution.validPalindrome(s))
# Output: False → "bc", "ac", "ab" are all not palindromes


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:                  # Already a palindrome? 0 deletes. Still allowed.
            return True

        for i in range(len(s)):           # Drop one letter per pass, left to right
            newS = s[:i] + s[i + 1:]      # Drop s[i]. Glue before + after. If i is 0, s[:0] is ""
            if newS == newS[::-1]:        # If the leftover is a palindrome, return True
                return True

        return False                      # Original failed and every one-letter drop failed

"""
Intuition
    • Try every delete. If any leftover is a palindrome, return True.
    • This works, but the input can be n = 10⁵ means 100,000 letters.
      That is 100,000 deletions, and each deletion scans ~100,000 letters.
      100,000 × 100,000 = 10 billion steps → Time Limit Exceeded (TLE).
    • The two-pointer solutions only try a deletion when two letters first fail to match.

Why this answers the question
    • "At most one" means 0 deletes or 1 delete.
    • 0 deletes: the first line, s == s[::-1]. Nothing removed. Still allowed.
    • 1 delete: the loop. Each pass drops only s[i]. newS never drops a second letter.
    • Direction: i goes 0, 1, 2, ... so we try dropping the leftmost letter first, then the next, then the next. One letter per pass, left to right. First leftover that is a palindrome → stop.
    • If the original fails and every one-letter drop fails → False.

What leftover means
    • Leftover = the WHOLE string minus that one letter. Not a palindrome hiding inside s.
    • Example "abaX": first three "aba" is a palindrome, but that alone does not win.
      It only wins when we drop "X" and the leftover is the entire rest: "aba".
      Left to right still catches that. i is which letter we drop:
          drop index 0 → "baX"
          drop index 1 → "aaX"
          drop index 2 → "abX"
          drop index 3 → "aba" → True

Interview Answer: Worst Case

Time: O(N²)
  - For each of N characters, rebuild the string and check if it is a palindrome.

Space: O(N)
  - Each deletion makes a new copy of the leftover string (newS).


---
Full Example Walkthrough:

    s = "abca"          ← this is a STRING, not a list
        0: a
        1: b
        2: c
        3: a

    How we drop one letter (every loop):
        newS = s[:i] + s[i + 1:]
        s[:i]     = letters BEFORE index i   (always a string)
                    if i is 0, there is nothing before → ""
        s[i]      = the letter we drop       (not in newS)
        s[i + 1:] = letters AFTER index i    (always a string)
        +         = glue two strings together
                    "" + "bca" is still the string "bca"
                    not an array

    Starting State:
        Check the original first.
        s == s[::-1]
        "abca" == "acba" → No
        So we start the loop and try deleting one letter at a time.

    --------------------------------------------------

    Loop i = 0: drop s[0] = "a"

        s[:0]     = ""          nothing before index 0
        s[1:]     = "bca"       everything after "a"
        newS      = "" + "bca" = "bca"

        newS == newS[::-1]
        "bca" == "acb" → No

        Keep going.

    --------------------------------------------------

    Loop i = 1: drop s[1] = "b"

        s[:1]     = "a"         everything before "b"
        s[2:]     = "ca"        everything after "b"
        newS      = "a" + "ca" = "aca"

        newS == newS[::-1]
        "aca" == "aca" → Yes

        return True
        Stop. We do not try i = 2 or i = 3.
        (Dropping "c" at i = 2 would also leave "aba", but we already returned True on "b".)

    --------------------------------------------------

    Final Check:
        return True

        This means:
            After deleting one letter ("b"), the leftover string "aca"
            reads the same forwards and backwards.

            Deleting "c" would also work — brute force just hits "b" first (left to right).


---
Quick Example Walkthrough:

    s = "aba"
        0: a
        1: b
        2: a

    Step 1: Original first
        "aba" == "aba" → Yes

    Step 2: Loop never runs
        Zero deletes is allowed. We already have a palindrome.

    Final Answer: True


---
Quick Example Walkthrough:

    s = "abc"
        0: a
        1: b
        2: c

    Step 1: Original first
        "abc" == "cba" → No
        Try deleting one letter, left to right.

    Step 2: Loop
        • i = 0 drop 'a' → newS = "" + "bc" = "bc" → "bc" != "cb" → no
        • i = 1 drop 'b' → newS = "a" + "c"  = "ac" → "ac" != "ca" → no
        • i = 2 drop 'c' → newS = "ab" + ""  = "ab" → "ab" != "ba" → no

    Step 3: Every one-letter drop failed

    Final Answer: False
"""
