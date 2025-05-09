# #  1. Compute Prefix Sum Array
# """
# Task: Given an array, create a new array of its prefix sums. Return an empty array if input is empty
# Example 1: [1, 2, 3, 4] → [1, 3, 6, 10]
# Example 2: [3, 7, 5] → [3, 10, 15]
# """
# def prefix_sum(arr):
#     # 1️⃣ Handle empty array case
#     if not arr: # if any falsy value --> return []
#         return []
    
#     # 2️⃣ Initialize result with the first element
#     result = [arr[0]] 

#     # 3️⃣ Compute prefix sums for remaining elements
#     for i in range(1, len(arr)):
#         result.append(result[-1] + arr[i])  

#     # 4️⃣ Return the prefix sum array
#     return result

# # print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  → [1, 1+2, 1+2+3 + 1+2+3+4]


