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



# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero. Return false otherwise.
Example: [4, -4, 1] → True  (4 + -4 = 0)
Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num  # Update running sum
        if prefix_sum == 0 or prefix_sum in seen:
            return True  
        seen.add(prefix_sum)
    return False

# Test the function
print(has_zero_sum_subarray([1, 3, -4, 5,]))  # Output: True ()
print(has_zero_sum_subarray([1, 3, 5, -4]))  # Output: False ()
print(has_zero_sum_subarray([1, 2, -2, 3]))  # Output: True ()

print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)
print(has_zero_sum_subarray([1, 2, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)






