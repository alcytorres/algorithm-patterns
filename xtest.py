# 2090. K Radius Subarray Averages

# Solution: https://leetcode.com/problems/k-radius-subarray-averages/description/

# Video https://www.youtube.com/watch?v=L33kbF6Cr_I

# Eaxmple
# nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

# Sliding Window Video Solution 1
# Video https://www.youtube.com/watch?v=L33kbF6Cr_I
    # I think I like this more than the LeetCode official solution

def getAverages(nums, k):
    n = len(nums)  # 9
    result = [-1] * n  # [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    window_size = 2*k + 1  # 7
    curr_sum = 0

    if (n < window_size):
        return result
    
    curr_sum = sum(nums[0:window_size])
    result[k] = curr_sum//window_size

    for i in range(k+1, n-k):
        curr_sum += nums[i+k] - nums[i-k-1]
        result[i] = curr_sum // window_size
    return result


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
print(getAverages(nums, 3))
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]















# # DSA Example 1 (Key-Value Iteration):
# ages = {"Alice": 25, "Bob": 30}
# print(list(ages.items()))  # Output: [("Alice", 25), ("Bob", 30)]




# how to identidy time and space
# how to know if  aquestion is commonly asked


# What is point of this from typing import List


# prefix[j] - prefix[i - 1]
# prefix[j] - prefix[i] + nums[i]


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
