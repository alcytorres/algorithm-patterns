# 560. Subarray Sum Equals K

# Example 4: Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

# Example 1:
    # Input: nums = [1, 1, 1], k = 2
    # Output: 2

# Example 2:
    # Input: nums = [1, 2, 3], k = 3
    # Output: 2

# Solution: https://leetcode.com/problems/subarray-sum-equals-k/solutions/127728/subarray-sum-equals-k/



# ––––––––––––––––––––––––––––––––––––––––––––––––
from collections import defaultdict

def numberOfSubarrays(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    odd = ans = 0

    for num in nums:
        odd += num % 2
        ans += counts[odd - k]
        counts[odd] += 1
    
    return ans

    
nums = [1, 1, 2, 1, 1, 1]
k = 3
print(numberOfSubarrays(nums, k))
