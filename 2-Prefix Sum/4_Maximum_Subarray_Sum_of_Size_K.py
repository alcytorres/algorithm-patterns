# 4. Maximum Subarray Sum of Size K   → Reference problem 1. Compute Prefix Sum Array 

# ----------------------------------------------------------------------------------
# *** Reference: 1. Compute Prefix Sum Array ***
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
"""
def prefix_sum(arr):
    if not arr:
        return []
    result = [arr[0]]  # First element is the same
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum
    return result

print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
# ----------------------------------------------------------------------------------

# 4. Maximum Subarray Sum of Size K
"""
Task: Find the largest sum of consecutive numbers (any subarray) in the array of size k. If array is shorter than 'k' return none
      i.e. Find the maximum sum of any subarray of size k.
Example 1: [1, 2, 3], k=2 → 5 (2 + 3)
Example 2: [7, 1, 8, 3], k=3 → 16 (7 + 1 + 8)
Why: Bridges to more complex subarray problems.
"""

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None
    prefix = prefix_sum(arr)
    max_sum = prefix[k - 1]  # First window sum
    for i in range(k, len(arr)):
        current_sum = prefix[i] - prefix[i - k]  # Sum of current window
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray_sum([1, 2, 3], 2))  # Output: 5 (2 + 3, largest sum of 2 consecutive numbers)
print(max_subarray_sum([4, 6, 1], 2))  # Output: 10 (4 + 6, largest sum of 2 consecutive numbers)
# print(max_subarray_sum([7, 1, 8, 3], 3))  # Output: 16  (7 + 1 + 8)


# Solution
def max_subarray_sum(arr, k):  # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any subarray of size k.
    
    - Uses prefix sums to compute subarray sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(n) for prefix array.
    - Prefix sum approach is simpler than sliding window for beginners here.
    """
    if len(arr) < k:      # If array is shorter than 'k'
        return None       # Cannot form a subarray of size 'k'
    prefix = prefix_sum(arr)      # Compute prefix sum array    prefix = [1, 2, 3] → [1, 3, 6)] 
    max_sum = prefix[k - 1]       # Sum of the first k elements    
    for i in range(k, len(arr)):  # Slide the window from k to the end    
        current_sum = prefix[i] - prefix[i - k]  # Calculate sum of current window    
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger   
    return max_sum      # Return the maximum sum found

# Test the function
print(max_subarray_sum([1, 2, 3], 2))  # Output: 5 (2 + 3, largest sum of 2 consecutive numbers)

"""
How to Remember It
    - Story to recall: Imagine a candy row. You want 2 candies together that are worth the most. Instead of adding each pair, you keep a running total (scoreboard: [1, 3, 6]). To find a pairs value, subtract an earlier total from a later one (like 6 - 1 = 5). Check all pairs, keep the best.
    - Steps to memorize:
        - Check if there is enough candies (if len(arr) < k).
        - Get the scoreboard (prefix_sum).
        - Start with the first pairs sum (prefix[k-1]).
        - Check other pairs by subtracting totals (prefix[i] - prefix[i-k]).
        - Pick the biggest sum (max).
"""

# ----------------------------------------------------------------------------------
# Solution with output

def max_subarray_sum(arr, k):            # arr = [1, 2, 3], k = 2
    if len(arr) < k:                     # len(arr) = 3, k = 2, is 3 < 2? False
        return None                      # skip
    prefix = prefix_sum(arr)             # prefix = [1, 3, 6] (totals: 1, 1+2, 1+2+3)
    max_sum = prefix[k - 1]              # k = 2, k-1 = 1, max_sum = prefix[1] = 3 (sum of [1, 2])
    for i in range(k, len(arr)):         # k = 2, len(arr) = 3, i = 2 to 2
                                         # Iteration 1: i = 2
        current_sum = prefix[i] - prefix[i - k]  # i = 2, i-k = 2-2 = 0, prefix[2] = 6, prefix[0] = 1, current_sum = 6-1=5 (sum of [2, 3])
        max_sum = max(max_sum, current_sum)  # max(3, 5) = 5, max_sum = 5
    return max_sum                       # Return 5 (biggest sum found)

print(max_subarray_sum([1, 2, 3], 2))  # Output: 5 (2 + 3, largest sum of 2 consecutive numbers)

# ----------------------------------------------------------------------------------
# Solution with output

def max_subarray_sum(arr, k):            # arr = [1, 2, 3, 4], k = 2
    if len(arr) < k:                     # len(arr) = 4, k = 2, is 4 < 2? False
        return None                      # skip
    prefix = prefix_sum(arr)             # prefix = [1, 3, 6, 10] (totals: 1, 1+2, 1+2+3, 1+2+3+4)
    max_sum = prefix[k - 1]              # k = 2, k-1 = 1, max_sum = prefix[1] = 3 (sum of [1, 2])
    for i in range(k, len(arr)):         # k = 2, len(arr) = 4, i = 2 to 3
                                         # Iteration 1: i = 2
        current_sum = prefix[i] - prefix[i - k]  # i = 2, i-k = 2-2 = 0, prefix[2] = 6, prefix[0] = 1, current_sum = 6-1=5 (sum of [2, 3])
        max_sum = max(max_sum, current_sum)  # max(3, 5) = 5, max_sum = 5
                                         # Iteration 2: i = 3
                                         # i = 3, i-k = 3-2 = 1, prefix[3] = 10, prefix[1] = 3, current_sum = 10-3=7 (sum of [3, 4])
                                         # max(5, 7) = 7, max_sum = 7
    return max_sum                       # Return 7 (biggest sum found)

print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4, largest sum of 2 consecutive numbers)

# ----------------------------------------------------------------------------------
# Solution with output

def max_subarray_sum(arr, k):            # arr = [4, 6, 1], k = 2
    if len(arr) < k:                     # len(arr) = 3, k = 2, is 3 < 2? False
        return None                      # skip
    prefix = prefix_sum(arr)             # prefix = [4, 10, 11] (totals: 4, 4+6, 4+6+1)
    max_sum = prefix[k - 1]              # k = 2, k-1 = 1, max_sum = prefix[1] = 10 (sum of [4, 6])
    for i in range(k, len(arr)):         # k = 2, len(arr) = 3, i = 2 to 2
                                         # Iteration 1: i = 2
        current_sum = prefix[i] - prefix[i - k]  # i = 2, i-k = 2-2 = 0, prefix[2] = 11, prefix[0] = 4, current_sum = 11-4=7 (sum of [6, 1])
        max_sum = max(max_sum, current_sum)  # max(10, 7) = 10, max_sum = 10
    return max_sum                       # Return 10 (biggest sum found)

print(max_subarray_sum([4, 6, 1], 2))  # Output: 10 (4 + 6, largest sum of 2 consecutive numbers)

