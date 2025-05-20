# 2. Count Subarrays with Sum K  
# ***Note this solution has limitations for negative numbers. Review the limitations below.*** Search if there is a better solution 
"""
Task: Count the number of contiguous subarrays that sum up to a given value k. Assume non-negative numbers.

Example 1: [1, 2, 3]    k=3 → 2 ([1, 2], [3])
Example 2: [1, 2, 3]    k=8 → 0 (no subarray sums to 8)
Example 3: [2, 2, 2, 2] k=4 → 3 ([2, 2], [2, 2], [2, 2])
Example 4: [0, 0, 0]    k=0 → 3 ([0], [0], [0])
Example 5: [1, 3, 2, 1] k=3 → 2 ([3], [2, 1])

Why: Practices maintaining a window with a condition.
"""

def count_subarrays_with_sum(arr, k):
    # 1️⃣ Initialize variables
    count = 0
    window_sum = 0
    left = 0

    # 2️⃣ Expand window by moving the right pointer & check conditions
    for right in range(len(arr)):

        # 3️⃣ Add current element to window sum
        window_sum += arr[right]

        # 4️⃣ Shrink window if sum exceeds k
        while window_sum > k and left <= right:
            window_sum -= arr[left]  # Shrink window
            left += 1

        # 5️⃣ Check if window sum equals k
        if window_sum == k:
            count += 1

    # 6️⃣ Return total count
    return count


print(count_subarrays_with_sum([1, 2, 3], 3))     # Output: 2 ([1, 2], [3])
print(count_subarrays_with_sum([1, 2, 3], 8))     # Output: 0 (no subarray sums to 8)
print(count_subarrays_with_sum([2, 2, 2, 2], 4))  # Output: 3 ([2, 2], [2, 2], [2, 2])
print(count_subarrays_with_sum([0, 0, 0], 0))     # Output: 3 ([0], [0], [0])
print(count_subarrays_with_sum([1, 3, 2, 1], 3))  # Output: 2 ([3], [2, 1])

# print(count_subarrays_with_sum([1, 1, 1], 1))  # Output: 3
# print(count_subarrays_with_sum([1, 1, 1], 2))  # Output: 2
# print(count_subarrays_with_sum([1, 1, 1], 3))  # Output: 1


# Simple Breakdown
def count_subarrays_with_sum(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Counts subarrays with sum equal to k (assuming non-negative numbers).
    
    - Uses a variable-size sliding window to find matching sums.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Simple sliding window approach is beginner-friendly for this case.
    """
    # 1️⃣ Initialize variables
    count = 0              # Initialize the count of subarrays with sum equal to k
    window_sum = 0         # Initialize the sum of the current window
    left = 0               # Set the left pointer of the window to the start
    
    # 2️⃣ Iterate over array with right pointer
    for right in range(len(arr)):  # Loop through the array with the right pointer

        # 3️⃣ Add current element to window sum
        window_sum += arr[right]  # Add the current element to the window sum

        # 4️⃣ Shrink window if sum exceeds k
        while window_sum > k and left <= right:  # If the sum exceeds k, shrink the window from the left
            window_sum -= arr[left]  # Subtract the leftmost element from the sum
            left += 1                # Move the left pointer one step right
        
        # 5️⃣ Check if window sum equals k
        if window_sum == k:     # If the current window sum equals k
            count += 1          # Increment the count of valid subarrays

    # 6️⃣ Return total count
    return count               # Return the total number of subarrays found


print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])
# print(count_subarrays_with_sum([1, 1], 1))  # Output: 2 ([1], [1])


"""
Concise Walkthrough of Why count_subarrays_with_sum Works

The count_subarrays_with_sum function counts how many contiguous subarrays in an array sum to a target value k. Here’s why it works, explained simply:

    1. Track Window Sum: It uses two pointers (left and right) to form a sliding window. window_sum tracks the sum of elements from left to right. For [1, 1], k=1, it starts with window_sum = 0.
    2.Expand Window: For each right, it adds arr[right] to window_sum. For example, at right=0, window_sum = 1 (adds 1).
    3. Shrink if Too Big: If window_sum > k, it shrinks the window by subtracting arr[left] and moving left forward until window_sum <= k or left > right. For right=1, window_sum = 2 > 1, so it subtracts arr[0]=1, making window_sum = 1.
    4. Count Matches: If window_sum == k, it increments count. For [1, 1], it finds window_sum = 1 at right=0 (subarray [1]) and after shrinking at right=1 (subarray [1]), so count = 2.
    5. Repeat Until End: It continues moving right through the array, checking each window. The while loop ensures only valid windows are counted.

    Why It Works: The sliding window efficiently checks all possible contiguous subarrays by expanding (right moves) and shrinking (left moves) as needed. It counts a subarray whenever its sum equals k, ensuring no valid subarray is missed. For [1, 1], k=1, it correctly finds both [1] subarrays, returning 2.


    
Limitations:
    - If the problem allowed negative numbers, the solution would need modification (e.g., using a prefix sum with a hash map for O(n) time).

    - Misses subarrays if k is negative (not relevant here due to non-negative input). 
"""


# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown

# Task: Count the number of contiguous subarrays that sum up to a given value k.
# Example: arr = [1, 2, 3], k = 3 → Output = 2 (subarrays [1, 2] and [3])
# Why? Practices maintaining a sliding window to find subarrays with a specific sum.

def count_subarrays_with_sum(arr, k):  # Example: arr = [1, 2, 3], k = 3

    # 1️⃣ Initialize variables
    # Count of subarrays that sum to k
    # Why? We need to track how many valid subarrays we find
    count = 0                  # count = 0 (no subarrays found yet)

    # Sum of the current window
    # Why? We track the sum to compare with k
    window_sum = 0             # window_sum = 0 (window is empty)

    # Left pointer for the start of the sliding window
    # Why? We'll move this to shrink the window when the sum exceeds k
    left = 0                   # left = 0 (start at beginning)

    # 2️⃣ Expand window by moving the right pointer & check conditions
    # Loop through each element as the right end of the window
    # Why? We process each element to build subarrays
    for right in range(len(arr)):  # right goes from 0 to 2 (len(arr) = 3)

        # --- Iteration 0: right = 0, arr[0] = 1 ---
        # 3️⃣ Add the current element to window sum
        # Why? We expand the window by including the new element
        window_sum += arr[right]   # window_sum = 0 + 1 = 1

        # 4️⃣ Shrink window if sum exceeds k and left <= right
        # Why? We need to keep the sum <= k and ensure a valid window
        while window_sum > k and left <= right:  # window_sum = 1, k = 3, skip (1 <= 3)
            # Subtract the leftmost element from the sum
            # Why? This shrinks the window to reduce the sum
            window_sum -= arr[left]  # skip
            # Move the left pointer forward
            # Why? Adjust the window start after removing an element
            left += 1                # skip
        # After while: window_sum = 1, left = 0

        # 5️⃣ Check if window sum equals k
        # Why? If it equals k, we've found a valid subarray
        if window_sum == k:         # window_sum = 1, k = 3, skip (1 != 3)
            count += 1              # skip
        # After Iteration 0: count = 0, window_sum = 1, left = 0
        # Current window: [1] (sum = 1, not equal to k)

        # --- Iteration 1: right = 1, arr[1] = 2 ---
        if right == 1:
            window_sum += arr[right]  # window_sum = 1 + 2 = 3

            while window_sum > k and left <= right:  # window_sum = 3, k = 3, skip (3 <= 3)
                window_sum -= arr[left]
                left += 1
            # After while: window_sum = 3, left = 0

            if window_sum == k:       # window_sum = 3, k = 3, true (3 == 3)
                count += 1            # count = 0 + 1 = 1
            # After Iteration 1: count = 1, window_sum = 3, left = 0
            # Current window: [1, 2] (sum = 3, equals k, subarray [1, 2] found)

        # --- Iteration 2: right = 2, arr[2] = 3 ---
        if right == 2:
            window_sum += arr[right]  # window_sum = 3 + 3 = 6

            while window_sum > k and left <= right:  # window_sum = 6, k = 3, true (6 > 3)
                # Remove arr[left] = arr[0] = 1
                window_sum -= arr[left]  # window_sum = 6 - 1 = 5
                left += 1                # left = 1
                # Check again: window_sum = 5, k = 3, true (5 > 3)
                # Remove arr[left] = arr[1] = 2
                window_sum -= arr[left]  # window_sum = 5 - 2 = 3
                left += 1                # left = 2
                # Check again: window_sum = 3, k = 3, false (3 <= 3), exit while
            # After while: window_sum = 3, left = 2

            if window_sum == k:       # window_sum = 3, k = 3, true (3 == 3)
                count += 1            # count = 1 + 1 = 2
            # After Iteration 2: count = 2, window_sum = 3, left = 2
            # Current window: [3] (sum = 3, equals k, subarray [3] found)

    # 6️⃣ Return total count of subarrays that sum to k
    # Why? count contains all the subarrays the sum to k
    return count                  # count = 2


print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 (subarrays [1, 2] and [3] sum to 3)



# ----------------------------------------------------------------------------------
# Solution with output 
