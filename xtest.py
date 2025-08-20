# 1941. Check if All Characters Have Equal Number of Occurrences

# Example 3: 
# Given a string s, determine if all characters have the same frequency.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# For example, given s = "abacbc", return true, because all characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

# Example:
# Input: s = "abacbc"
# Output: True
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Solution: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/solutions/


from collections import defaultdict

def areOccurrencesEqual(s):
    


s = "abacbc"
print(areOccurrencesEqual(s))
# Output: True









# # how to identidy time and space
# # how to know if  aquestion is commonly asked


# # What is point of this from typing import List


# # prefix[j] - prefix[i - 1]
# # prefix[j] - prefix[i] + nums[i]


# # Template 1
# def fn(arr):
#     prefix = [arr[0]]
#     for i in range(1, len(arr)):
#         prefix.append(prefix[-1] + arr[i])
    
#     return prefix

# print(fn([1, 6, 3, 2, 7, 2]))


# # Template 2
# def prefix_sum(arr):
#     prefix = [arr[0]]  # Array to store prefix sums, starts with first element
#     curr = arr[0]      # Tracks running sum for building prefix array
    
#     for i in range(1, len(arr)):  # Iterate from index 1
#         # Add current element to running sum
#         curr += arr[i]
#         # Append running sum to prefix array
#         prefix.append(curr)
    
#     return prefix  # Return prefix sum array for subarray sum queries

# print(prefix_sum([1, 6, 3, 2, 7, 2]))
