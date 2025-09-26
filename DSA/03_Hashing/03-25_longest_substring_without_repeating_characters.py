# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Solution: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Example 1:
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.

# Example 2:
#     Input: s = "bbbbb"
#     Output: 1
#     Explanation: The answer is "b", with the length of 1.

# Constraints:
    # 0 <= s.length <= 5 * 104
    # s consists of English letters, digits, symbols and spaces.

# Approach: Sliding Window with Set

def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If duplicate, shrink window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        # Expand window
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

s = "abbabcb"
print(lengthOfLongestSubstring(s))  
# Output: 3


"""
Time: O(N)
  - Let N = length of string s.
  - Both pointers (left and right) move across the string at most once.
  - Each character is added to and removed from the set at most once → O(1) per operation.
  - Overall: O(N).

Space: O(K)
  - The set 'seen' stores up to K unique characters in the current window.
  - In worst case (all characters unique), K = N → O(N).
  - A few integer variables (left, right, max_len) use O(1).
  - Overall: O(K), worst case O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Sliding window ensures each character is processed at most twice.

Space: O(N)
  - Set can hold up to all unique characters in s.


Overview for Each Iteration
Input: s = "ababcb"
Step: Find longest substring without repeating characters using sliding window
r  | s[r] | seen       | s[r] in seen | l  | Action            | max_len
---|------|------------|--------------|----|-------------------|--------
0  | a    | {}         | False        | 0  | Add 'a'           | 1 (0-0+1)
1  | b    | {a}        | False        | 0  | Add 'b'           | 2 (1-0+1)
2  | a    | {a, b}     | True         | 0  | Remove 'a', l+=1  | 2
   |      | {b}        | False        | 1  | Add 'a'           | 2 (2-1+1)
3  | b    | {b, a}     | True         | 1  | Remove 'b', l+=1  | 2
   |      | {a}        | False        | 2  | Add 'b'           | 2 (3-2+1)
4  | c    | {a, b}     | False        | 2  | Add 'c'           | 3 (4-2+1)
5  | b    | {a, b, c}  | True         | 2  | Remove 'a', l+=1  | 3
   |      | {b, c}     | True         | 3  | Remove 'b', l+=1  | 3
   |      | {c}        | False        | 4  | Add 'b'           | 3 (5-4+1)
Final: 3 ("abc")



Most IMPORTANT thing to Understand:
    • We need the longest substring (continuous part of s) with no repeated characters.

    • A sliding window [left, right] keeps track of the current substring without duplicates.

    • The set 'seen' ensures we only keep unique characters inside the window.

---
Why this code Works:
    • Data structure: set(seen) tracks which characters are currently in the window.

    • Technique: Sliding window expands with right; if a duplicate is found, shrink from left until it's removed.

    • Efficiency: Each char is added/removed at most once → O(N) time, faster than checking all substrings O(N²).

    • Intuition: Like moving a window over the string and adjusting it so the window always has unique chars.

---
TLDR:
    • Expand the window with right, shrink with left when duplicates appear, and track the max length.

---
Quick Example Walkthrough:

    s = "abcabcbb"

    Step 1: right=0 → 'a' not in seen → add → window="a" → max_len=1  
    Step 2: right=1 → 'b' not in seen → add → window="ab" → max_len=2  
    Step 3: right=2 → 'c' not in seen → add → window="abc" → max_len=3  
   
    Step 4: right=3 → 'a' in seen → remove left 'a' → window="bc" → add 'a' → window="bca" → max_len=3  
    
    Step 5: right=4 → 'b' in seen → remove left until 'b' gone → window="ca" → add 'b' → window="cab" → max_len=3  
  
    Step 6: right=5 → 'c' in seen → shrink left until 'c' gone → window="ab" → add 'c' → window="abc" → max_len=3  
   
    Step 7: right=6 → 'b' in seen → shrink left until 'b' gone → window="c" → add 'b' → window="cb" → max_len=3  
   
    Step 8: right=7 → 'b' in seen → shrink left until 'b' gone → window="b" → max_len=3  

    Final Answer: 3 ("abc")

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach: Sliding Window with Set

def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If duplicate, shrink window from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        # Expand window
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))  
# Output: 3


"""
Overview for Each Iteration
Input: s = "abcabcbb"
Step: Find longest substring without repeating characters
r   | s[r] | seen before | s[r] in seen | l   | seen after remove | seen after add | max_len
----|------|-------------|--------------|-----|-------------------|----------------|--------
0   | a    | {}          | False        | 0   | -                 | {a}            | 1
1   | b    | {a}         | False        | 0   | -                 | {a, b}         | 2
2   | c    | {a, b}      | False        | 0   | -                 | {a, b, c}      | 3
3   | a    | {a, b, c}   | True         | 0   | {b, c}            | {b, c, a}      | 3
4   | b    | {b, c, a}   | True         | 1   | {c, a}            | {c, a, b}      | 3
5   | c    | {c, a, b}   | True         | 2   | {a, b}            | {a, b, c}      | 3
6   | b    | {a, b, c}   | True         | 3   | {b, c}            | {b, c}         | 3
    |      | {b, c}      | True         | 4   | {c}               | {c, b}         | 3
7   | b    | {c, b}      | True         | 5   | {b}               | {b}            | 3
    |      | {b}         | True         | 6   | {}                | {b}            | 3
Final: 3 ("abc")

"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def lengthOfLongestSubstring(s):
    seen = set()              # Track characters in current window
    left = max_len = 0        # Left bound, max substring length

    for right in range(len(s)):  # Iterate right pointer over string
        while s[right] in seen:  # If current char already in window
            seen.remove(s[left]) # Remove leftmost char
            left += 1            # Shrink window from left
        seen.add(s[right])       # Add current char to window
        max_len = max(max_len, right - left + 1)  # Update max length
    return max_len            # Return longest substring without repeating chars



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 

def lengthOfLongestSubstring(s):
    def check(start, end):
        chars = set()
        for i in range(start, end + 1):
            c = s[i]
            if c in chars:
                return False
            chars.add(c)
        return True

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground

"""
📘 Tutorial: set.add() and set.remove()
    • Sets in Python are collections of unique elements.
    • .add(x) inserts an element into the set.
    • .remove(x) deletes an element from the set (raises an error if x not present).
    • Very useful for sliding window problems where we track what's inside the window.
"""

# Basic Example
fruits = set()
fruits.add("apple")
fruits.add("banana")
print(fruits)   # Output: {'apple', 'banana'}

fruits.remove("apple")
print(fruits)   # Output: {'banana'}


# Example with .add(): count unique numbers
def unique_count(nums):
    seen = set()
    for n in nums:
        seen.add(n)   # add each number
    return len(seen)  # number of unique items

nums = [1, 2, 2, 3]
print(unique_count(nums))  
# Output: 3 (unique numbers are 1, 2, 3)


# Example with .remove(): filter duplicates out
def remove_duplicates(nums):
    seen = set(nums)   # keep only unique items
    seen.remove(min(seen))  # remove the smallest one
    return seen

nums = [4, 2, 2, 5]
print(remove_duplicates(nums))  
# Output: {4, 5} (unique set {2, 4, 5} minus the smallest element 2)



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solutions

# Approach 2: Sliding Window w Counter

from collections import Counter

def lengthOfLongestSubstring(s):
    chars = Counter()

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[r] += 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1

    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 3: Sliding Window Optimized

def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    # charToNextIndex stores the index after current character
    charToNextIndex = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in charToNextIndex:
            i = max(charToNextIndex[s[j]], i)

        ans = max(ans, j - i + 1)
        charToNextIndex[s[j]] = j + 1

    return ans

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3

