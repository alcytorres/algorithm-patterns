# 2. Count Subarrays with Sum K
"""
Count the number of contiguous subarrays that sum to a given value k.
Task: Count subarrays with a given sum.
Example: [1, 2, 3], k=3 → 2 ([1, 2], [3])
Why: Practices maintaining a window with a condition.
"""

def count_subarrays_with_sum(arr, k):
    count = 0
    window_sum = 0
    left = 0
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum > k and left <= right:
            window_sum -= arr[left]  # Shrink window
            left += 1
        if window_sum == k:
            count += 1
    return count


print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])


# Solution
def count_subarrays_with_sum(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Counts subarrays with sum equal to k (assuming non-negative numbers).
    
    - Uses a variable-size sliding window to find matching sums.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Simple sliding window approach is beginner-friendly for this case.
    """
    count = 0              # Initialize the count of subarrays with sum equal to k
    window_sum = 0         # Initialize the sum of the current window
    left = 0               # Set the left pointer of the window to the start
    for right in range(len(arr)):  # Loop through the array with the right pointer
        window_sum += arr[right]  # Add the current element to the window sum
        while window_sum > k and left <= right:  # If the sum exceeds k, shrink the window from the left
            window_sum -= arr[left]  # Subtract the leftmost element from the sum
            left += 1            # Move the left pointer one step right
        if window_sum == k:     # If the current window sum equals k
            count += 1          # Increment the count of valid subarrays
    return count               # Return the total number of subarrays found

# Test the function
print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])


# ----------------------------------------------------------------------------------
# Solution with output 

def count_subarrays_with_sum(arr, k):           # arr = [1, 2, 3], k = 3
    count = 0                                   # count = 0
    window_sum = 0                              # window_sum = 0
    left = 0                                    # left = 0
    for right in range(len(arr)):                # range(3) → right = 0, 1, 2
        window_sum += arr[right]                 # right = 0: window_sum = 0 + 1 = 1
                                                 # right = 1: window_sum = 1 + 2 = 3
                                                 # right = 2: window_sum = 3 + 3 = 6
        while window_sum > k and left <= right:  # right = 0: 1 > 3 → False
                                                 # right = 1: 3 > 3 → False
                                                 # right = 2: 6 > 3 and 0 ≤ 2 → True
            window_sum -= arr[left]              # right = 2: window_sum = 6 - 1 = 5
                                                 # Loop again: 5 > 3 and 1 ≤ 2 → True
                                                 # window_sum = 5 - 2 = 3
            left += 1                            # right = 2: left = 1, then left = 2
        if window_sum == k:                      # right = 0: 1 == 3 → False
                                                 # right = 1: 3 == 3 → True
                                                 # right = 2: 3 == 3 → True
            count += 1                           # right = 1: count = 1
                                                 # right = 2: count = 2
    return count                                 # Return 2

print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])

