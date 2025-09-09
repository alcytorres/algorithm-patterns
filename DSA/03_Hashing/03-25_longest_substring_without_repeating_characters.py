# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.

# Example 2:
#     Input: s = "bbbbb"
#     Output: 1
#     Explanation: The answer is "b", with the length of 1.


# Solution: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/








# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown





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
# Alternate Solutions

# Approach 2: Sliding Window

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


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––

def lengthOfLongestSubstring(s):
    chars = [None] * 128

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]

        index = chars[ord(r)]
        if index is not None and left <= index < right:
            left = index + 1

        res = max(res, right - left + 1)

        chars[ord(r)] = right
        right += 1

    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
# Output: 3