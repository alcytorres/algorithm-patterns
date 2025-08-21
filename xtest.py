# 560. Subarray Sum Equals K

# Example 4: 

# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2

# Solution: https://leetcode.com/problems/subarray-sum-equals-k/solutions/127728/subarray-sum-equals-k/


from collections import defaultdict

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


numbers = [1, 2, 3]
print(subarraySum(numbers, 3))
# Output: 









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
