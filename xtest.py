
















# Why ans += counts[curr - k]?

# curr is the sum from start to current index.
# If curr - k is in counts, it means a previous sum exists where curr - prev = k, forming a subarray with sum k.
# counts[curr - k] tells how many such subarrays end at the current index.





# Trace Overview



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
