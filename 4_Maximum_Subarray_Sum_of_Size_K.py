# 4. Maximum Subarray Sum of Size K   → Reference problem 1. Compute Prefix Sum Array 
"""
Task: Find the largest sum of consecutive numbers (for any subarray) in the array of size k.
      i.e. Find the maximum sum of any subarray of size k.
Example 1: [1, 2, 3, 4], k=2 → 7 (3 + 4)
Example 2: [5, 2, 8, 1], k=3 → 15 (5 + 2 + 8)
Why: Bridges to more complex subarray problems.
"""
# ----------------------------------------------------------------------------------
# 1. Compute Prefix Sum Array  → Reference this solution [1, 3, 6, 10)] for Maximum Subarray Sum of Size K
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3, 4] → [1, 3, 6, 10]
"""

def prefix_sum(arr):   # Define the function that takes an array 'arr' as input
    if not arr:         # Check if the array is empty
        return []       # Return an empty array if input is empty
    result = [arr[0]]   # Start the result with the first element of 'arr'
    for i in range(1, len(arr)):  # Loop from the second element to the end
        result.append(result[-1] + arr[i])  # Add the previous sum to the current element
    return result       # Return the prefix sum array

print(prefix_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]  →  [1, 1+2, 1+2+3, 1+2+3+4]
# ----------------------------------------------------------------------------------

# 4. Maximum Subarray Sum of Size K
def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None
    prefix = prefix_sum(arr)
    max_sum = prefix[k - 1]  # First window sum
    for i in range(k, len(arr)):
        current_sum = prefix[i] - prefix[i - k]  # Sum of current window
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test the function
print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


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
    prefix = prefix_sum(arr)      # Compute prefix sum array    prefix = [1, 2, 3, 4] → [1, 3, 6, 10)] 
    max_sum = prefix[k - 1]       # Sum of the first k elements    
    for i in range(k, len(arr)):  # Slide the window from k to the end    
        current_sum = prefix[i] - prefix[i - k]  # Calculate sum of current window    
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger   
    return max_sum      # Return the maximum sum found

# Test the function
print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)


# ----------------------------------------------------------------------------------
# Solution with output
def max_subarray_sum(arr, k): 
    if len(arr) < k:              # 4 < 2 → False
        return None              
    prefix = prefix_sum(arr)      # prefix = [1, 3, 6, 10]
    max_sum = prefix[k - 1]       # prefix[2-1] = prefix[1] = 3 (1+2)
    for i in range(k, len(arr)):  # range(2, 4): i = 2 | i = 3
        current_sum = prefix[i] - prefix[i - k]  # prefix[2]-prefix[0] = 6-1 = 5 | prefix[3]-prefix[1] = 10-3 = 7
        max_sum = max(max_sum, current_sum)      # max(3, 5) = 5 | max(5, 7) = 7
    return max_sum                               # 7


print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)

