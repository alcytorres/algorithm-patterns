# 1248. Count Number of Nice Subarrays

# Example 5
# Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

# A continuous subarray is called nice if there are k odd numbers on it.


# Example 1:
# Input: nums = [1, 1, 2, 1, 1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1, 1, 2, 1] and [1, 2, 1, 1].

# Solution: https://leetcode.com/problems/count-number-of-nice-subarrays/solutions/5349373/count-number-of-nice-subarrays/


from collections import defaultdict

def numberOfSubarrays(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0
    
    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

nums = [1, 1, 2, 1, 1]
print(numberOfSubarrays(nums, 3))
# Output: 2
