# 2. Count Subarrays with Sum K  
# Note this solution has limitations for negative numbers. Review the limitations below.
"""
Task: Count the number of contiguous subarrays that sum up to a given value k. Assume non-negative numbers.
Example 1: [1, 2, 3], k=3 → 2 ([1, 2], [3])
Example 2: [1, 2, 3], k=8 → 0 (no subarray sums to 8)
Example 3: [2, 2, 2, 2], k=4 → 3 ([2, 2], [2, 2], [2, 2])
Example 4: [0, 0, 0], k=0 → 3 ([0], [0], [0])
Example 5: [1, 3, 2, 1], k=3 → 2 ([3], [2, 1])
Why: Practices maintaining a window with a condition.
"""

def count_subarrays_with_sum(arr, k):
    # 1️⃣ Initialize variables
    count = 0
    window_sum = 0
    left = 0

    # 2️⃣ Iterate over array with right pointer
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
            left += 1            # Move the left pointer one step right
        
        # 5️⃣ Check if window sum equals k
        if window_sum == k:     # If the current window sum equals k
            count += 1          # Increment the count of valid subarrays

    # 6️⃣ Return total count
    return count               # Return the total number of subarrays found


print(count_subarrays_with_sum([1, 1], 1))  # Output: 2 ([1], [1])
# print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])


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

def count_subarrays_with_sum(arr, k):  # Example: arr = [1, 2, 3], k = 3
    # 1️⃣ Initialize variables
    # Set up counters and pointers for sliding window
    # Why? We need to track subarray count, current window sum, and window boundaries
    count = 0              # count = 0 (number of subarrays with sum k)
    window_sum = 0         # window_sum = 0 (current sum of window)
    left = 0               # left = 0 (left boundary of window)
    # After initialization: Ready to process array with sliding window

    # 2️⃣ Iterate over array with right pointer
    # Expand window by moving right pointer
    # Why? We check all possible subarrays by extending the window
    for right in range(len(arr)):  # len(arr) = 3, range(0, 3) → right = 0, 1, 2
        
        # 3️⃣ Add current element to window sum
        # Include arr[right] in the window
        # Why? We need to update the sum as the window grows
        window_sum += arr[right]  # --- right = 0 ---
                                  # arr[0] = 1, window_sum = 0 + 1 = 1
                                  # --- right = 1 ---
                                  # arr[1] = 2, window_sum = 1 + 2 = 3
                                  # --- right = 2 ---
                                  # arr[2] = 3, window_sum = 3 + 3 = 6

        # 4️⃣ Shrink window if sum exceeds k
        # Reduce window size from left if sum > k
        # Why? We want subarrays with sum exactly k, so remove elements until sum <= k
        while window_sum > k and left <= right:
            window_sum -= arr[left]  # --- right = 0, window_sum = 1 ---
                                     # 1 < 3, skip
                                     # --- right = 1, window_sum = 3 ---
                                     # 3 = 3, skip
                                     # --- right = 2, window_sum = 6 ---
                                     # 6 > 3, left = 0
                                     # arr[0] = 1, window_sum = 6 - 1 = 5
                                     # left = 1
                                     # 5 > 3, left = 1
                                     # arr[1] = 2, window_sum = 5 - 2 = 3
                                     # left = 2
            left += 1                # Update left pointer after shrinking

        # 5️⃣ Check if window sum equals k
        # If sum is exactly k, increment count
        # Why? A valid subarray is found when window_sum = k
        if window_sum == k:       # --- right = 0, window_sum = 1 ---
                                  # 1 ≠ 3, skip
                                  # --- right = 1, window_sum = 3 ---
                                  # 3 = 3, count = 0 + 1 = 1 ([1, 2])
                                  # --- right = 2, window_sum = 3 ---
                                  # 3 = 3, count = 1 + 1 = 2 ([3])
            count += 1
        # After right = 0: window_sum = 1, count = 0, left = 0, window: [1]
        # After right = 1: window_sum = 3, count = 1, left = 0, window: [1, 2]
        # After right = 2: window_sum = 3, count = 2, left = 2, window: [3]

    # 6️⃣ Return total count
    # Why? count holds the number of subarrays with sum k
    return count              # Return count = 2
    # Final state: count = 2 (subarrays [1, 2] and [3])
    # Conclusion: Successfully counted subarrays with sum k=3

print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])



# ----------------------------------------------------------------------------------
# Solution with output 
