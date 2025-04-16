# # ----------------------------------------------------------------------------------
# # 1. Compute Prefix Sum Array
# """
# Task: Given an array, create a new array of its prefix sums. Return an empty array if input is empty
# Example: [1, 2, 3] → [1, 3, 6]
# Why: Direct practice for Running Sum of 1d Array.
# """

# def prefix_sum(arr):
#     if not arr:
#         return []
#     result = [arr[0]]
#     for i in range(1, len(arr)):
#         result.append(result[-1] + arr[i])
#     return result

# # Test the function
# print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
# # print(prefix_sum([]))  # Output: []  

# ----------------------------------------------------------------------------------

# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero.
Example: [4, -4, 1] → True
Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):   
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)
        print(seen)
        return False

# Test the function
print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)



def has_zero_sum_subarray(arr):    # Define the function that takes an array 'arr' as input
    prefix_sum = 0      # Initialize prefix sum to zero
    seen = set()        # Create an empty set to store seen prefix sums
    for num in arr:     # Iterate through each element in 'arr'
        prefix_sum += num  # Add the current number to the prefix sum
        if prefix_sum == 0 or prefix_sum in seen:  # If prefix sum is zero or seen before
            return True   # A subarray with sum zero exists
        seen.add(prefix_sum)  # Add the current prefix sum to the set
    return False        # No subarray with sum zero found

# Test the function
# print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)



