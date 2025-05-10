# 4. Maximum Subarray Sum of Size K   → Reference problem 1. Compute Prefix Sum Array 

# ----------------------------------------------------------------------------------
# *** Reference: 1. Compute Prefix Sum Array ***
"""
Task: Given an array, create a new array of its prefix sums.
Example: [1, 2, 3] → [1, 3, 6]
"""
def prefix_sum(arr):
    # 1️⃣ Handle empty array case
    if not arr:
        return []
    
    # 2️⃣ Initialize result with the first element
    result = [arr[0]]  

    # 3️⃣ Compute prefix sums for remaining elements
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])  # Add current element to previous sum

    # 4️⃣ Return the prefix sum array
    return result

print(prefix_sum([1, 2, 3]))  # Output: [1, 3, 6]  →  [1, 1+2, 1+2+3]
# ----------------------------------------------------------------------------------

# 4. Maximum Subarray Sum of Size K
"""
Task: Find the largest sum of consecutive numbers (any subarray) in the array of size k. If array is shorter than 'k' return none
      i.e. "Find the maximum sum of any subarray of size k."
Example 1: [1, 2, 3],     k=2 → 5 (2 + 3)
Example 2: [1, 2, 3, 4],  k=2 → 7 (3 + 4)
Example 3: [1, 4, 6, 1],  k=2 → 10 (4 + 6)
Example 4: [7, 1, 8, 3],  k=3 → 16 (7 + 1 + 8)
Why: Bridges to more complex subarray problems.
"""

def max_subarray_sum(arr, k):

    # 1️⃣ Check if array length is sufficient
    if len(arr) < k:
        return None
    
    # 2️⃣ Compute prefix sums
    prefix = prefix_sum(arr)

    # 3️⃣ Initialize maximum sum with first window
    max_sum = prefix[k - 1]  # First window sum
    for i in range(k, len(arr)):
        current_sum = prefix[i] - prefix[i - k]  
        max_sum = max(max_sum, current_sum)

    # 5️⃣ Return the maximum sum
    return max_sum

print(max_subarray_sum([1, 4, 6, 1], 2))  # Output: 10 (largest sum of 2 consecutive numbers)
print(max_subarray_sum([1, 2, 3], 2))     # Output: 5 (2 + 3)
print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)
print(max_subarray_sum([4, 6, 1], 2))     # Output: 10 (4 + 6)
print(max_subarray_sum([1, 6, 7, 3], 3))  # Output: 16 (6 + 7 + 3)


# Simple Breakdown
def max_subarray_sum(arr, k):  # Define the function that takes an array 'arr' and integer 'k'
    """
    Finds the maximum sum of any subarray of size k.
    
    - Uses prefix sums to compute subarray sums efficiently.
    - Time Complexity: O(n), Space Complexity: O(n) for prefix array.
    - Prefix sum approach is simpler than sliding window for beginners here.
    """
    # 1️⃣ Check if array length is sufficient
    if len(arr) < k:      # If array is shorter than 'k'
        return None       # Cannot form a subarray of size 'k'
    
    # 2️⃣ Compute prefix sums
    prefix = prefix_sum(arr)      # Compute prefix sum array    prefix = [1, 2, 3] → [1, 3, 6)] 
    
    # 3️⃣ Initialize maximum sum with first window
    max_sum = prefix[k - 1]       # Sum of the first k elements    

    # 4️⃣ Iterate through remaining windows
    for i in range(k, len(arr)):  # Slide the window from k to the end    
        current_sum = prefix[i] - prefix[i - k]  # Calculate sum of current window    
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger   

    # 5️⃣ Return the maximum sum
    return max_sum      # Return the maximum sum found


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
# Solution with output Full Breakdown 

def max_subarray_sum(arr, k):  # Example: arr = [1, 4, 6, 1], k = 2

    # 1️⃣ Check if array length is sufficient
    # Verify if the array has at least k elements
    # Why? If len(arr) < k, no subarray of size k is possible
    if len(arr) < k:           # len(arr) = 4, k = 2, 4 < 2 → False
        return None            # Skip (array length is sufficient)
    # After check: Proceed since len(arr) >= k

    # 2️⃣ Compute prefix sums
    # Generate prefix sum array using prefix_sum function
    # Why? Prefix sums allow efficient calculation of subarray sums
    prefix = prefix_sum(arr)   # arr = [1, 4, 6, 1] → prefix = [1, 5, 11, 12]
    # After computation: prefix = [1, 5, 11, 12] (1, 1+4, 1+4+6, 1+4+6+1)

    # 3️⃣ Initialize maximum sum with first window
    # Set max_sum to the sum of the first k elements
    # Why? The first subarray of size k is our initial candidate
    max_sum = prefix[k - 1]    # k = 2, k - 1 = 1, prefix[1] = 5
                               # max_sum = 5 (sum of arr[0:2] = 1 + 4)
    # After initialization: max_sum = 5, representing sum of first window [1, 4]

    # 4️⃣ Iterate through remaining windows
    # Loop through array to compute sums of subsequent k-sized windows
    # Why? We compare each window's sum to find the maximum
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, range(2, 4) → i = 2, 3
        
        # --- Iteration 1: i = 2 ---
        # Calculate sum of current window using prefix sums
        # Why? prefix[i] - prefix[i - k] gives sum of arr[i-k:i]
        current_sum = prefix[i] - prefix[i - k]  # i = 2, prefix[2] = 11
                                                 # i - k = 2 - 2 = 0, prefix[0] = 1
                                                 # current_sum = 11 - 1 = 10
                                                 # (sum of arr[1:3] = 4 + 6)
        
        # Update max_sum if current_sum is larger
        # Why? We want the largest sum among all k-sized subarrays
        max_sum = max(max_sum, current_sum)  # max(5, 10) = 10
                                             # max_sum = 10
        # After Iteration 1: i = 2, max_sum = 10
        # Current window: [4, 6], sum = 10

        # --- Iteration 2: i = 3 ---
        if i == 3:                           # Check for clarity
            current_sum = prefix[i] - prefix[i - k]  # i = 3, prefix[3] = 12
                                                     # i - k = 3 - 2 = 1, prefix[1] = 5
                                                     # current_sum = 12 - 5 = 7
                                                     # (sum of arr[2:4] = 6 + 1)
            max_sum = max(max_sum, current_sum)  # max(10, 7) = 10
                                                 # max_sum = 10
        # After Iteration 2: i = 3, max_sum = 10
        # Current window: [6, 1], sum = 7

    # 5️⃣ Return the maximum sum
    # Why? max_sum is the largest sum of any k-sized subarray
    return max_sum               # Return max_sum = 10
    # Final state: max_sum = 10 (from subarray [4, 6])
    # Conclusion: Successfully found maximum sum of subarray of size k=2

print(max_subarray_sum([1, 4, 6, 1], 2))  # Output: 10 (4 + 6)



# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown 

def max_subarray_sum(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

    # 1️⃣ Check if array length is sufficient
    # Verify if the array has at least k elements
    # Why? If len(arr) < k, no subarray of size k is possible
    if len(arr) < k:           # len(arr) = 4, k = 2, 4 < 2 → False
        return None            # Skip (array length is sufficient)
    # After check: Proceed since len(arr) >= k

    # 2️⃣ Compute prefix sums
    # Generate prefix sum array using prefix_sum function
    # Why? Prefix sums allow efficient calculation of subarray sums
    prefix = prefix_sum(arr)   # arr = [1, 2, 3, 4] → prefix = [1, 3, 6, 10]
    # After computation: prefix = [1, 3, 6, 10] (1, 1+2, 1+2+3, 1+2+3+4)

    # 3️⃣ Initialize maximum sum with first window
    # Set max_sum to the sum of the first k elements
    # Why? The first subarray of size k is our initial candidate
    max_sum = prefix[k - 1]    # k = 2, k - 1 = 1, prefix[1] = 3
                               # max_sum = 3 (sum of arr[0:2] = 1 + 2)
    # After initialization: max_sum = 3, representing sum of first window [1, 2]

    # 4️⃣ Iterate through remaining windows
    # Loop through array to compute sums of subsequent k-sized windows
    # Why? We compare each window's sum to find the maximum
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, range(2, 4) → i = 2, 3
        
        # --- Iteration 1: i = 2 ---
        # Calculate sum of current window using prefix sums
        # Why? prefix[i] - prefix[i - k] gives sum of arr[i-k:i]
        current_sum = prefix[i] - prefix[i - k]  # i = 2, prefix[2] = 6
                                                 # i - k = 2 - 2 = 0, prefix[0] = 1
                                                 # current_sum = 6 - 1 = 5
                                                 # (sum of arr[1:3] = 2 + 3)
        
        # Update max_sum if current_sum is larger
        # Why? We want the largest sum among all k-sized subarrays
        max_sum = max(max_sum, current_sum)  # max(3, 5) = 5
                                             # max_sum = 5
        # After Iteration 1: i = 2, max_sum = 5
        # Current window: [2, 3], sum = 5

        # --- Iteration 2: i = 3 ---
        if i == 3:                           # Check for clarity
            current_sum = prefix[i] - prefix[i - k]  # i = 3, prefix[3] = 10
                                                     # i - k = 3 - 2 = 1, prefix[1] = 3
                                                     # current_sum = 10 - 3 = 7
                                                     # (sum of arr[2:4] = 3 + 4)
            max_sum = max(max_sum, current_sum)  # max(5, 7) = 7
                                                 # max_sum = 7
        # After Iteration 2: i = 3, max_sum = 7
        # Current window: [3, 4], sum = 7

    # 5️⃣ Return the maximum sum
    # Why? max_sum is the largest sum of any k-sized subarray
    return max_sum               # Return max_sum = 7
    # Final state: max_sum = 7 (from subarray [3, 4])
    # Conclusion: Successfully found maximum sum of subarray of size k=2

print(max_subarray_sum([1, 2, 3, 4], 2))  # Output: 7 (3 + 4)



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

def max_subarray_sum(arr, k):          # arr = [1, 2, 3, 4], k = 2
    if len(arr) < k:                   # len(arr) = 4, k = 2, is 4 < 2? False
        return None                    # skip
    prefix = prefix_sum(arr)           # prefix = [1, 3, 6, 10] (totals: 1, 1+2, 1+2+3, 1+2+3+4)
    max_sum = prefix[k - 1]            # k = 2, k-1 = 1, max_sum = prefix[1] = 3 (sum of [1, 2])
    for i in range(k, len(arr)):       # k = 2, len(arr) = 4, i = 2 to 3
                                       # Iteration 1: i = 2
        current_sum = prefix[i] - prefix[i - k]  # i = 2, i-k = 2-2 = 0, prefix[2] = 6, prefix[0] = 1, current_sum = 6 - 1 = 5 (sum of [2, 3])
        max_sum = max(max_sum, current_sum)  # max(3, 5) = 5, max_sum = 5
                                       # Iteration 2: i = 3
        current_sum = prefix[i] - prefix[i - k]  # i = 3, i-k = 3-2 = 1, prefix[3] = 10, prefix[1] = 3, current_sum = 10 - 3 = 7 (sum of [3, 4])
        max_sum = max(max_sum, current_sum)  # max(5, 7) = 7, max_sum = 7

    return max_sum                     # Return 7 (biggest sum found)


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

