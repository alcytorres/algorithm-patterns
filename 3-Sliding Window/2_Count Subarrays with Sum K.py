# 2. Count Subarrays with Sum K
"""
Task: Count the number of contiguous subarrays that sum up to a given value k. Assume non-negative numbers.
Example: [1, 1],    k=1 → 2 ([1], [1])
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


print(count_subarrays_with_sum([1, 1], 1))  # Output: 2 ([1], [1])
# print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])


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
"""

# ----------------------------------------------------------------------------------
# Solution with output 

def count_subarrays_with_sum(arr, k):      # arr = [1, 1], k = 1
    count = 0                              # count = 0 (start with no subarrays found)
    window_sum = 0                         # window_sum = 0 (start with no total)
    left = 0                               # left = 0 (left pointer at start)
    for right in range(len(arr)):          # right = 0 to 1 (len = 2)
                                           # Iteration 1: right = 0
        window_sum += arr[right]           # window_sum = 0 + arr[0] = 0 + 1 = 1
        while window_sum > k and left <= right:  # Is 1 > 1 and 0 <= 0? No
            window_sum -= arr[left]        # skip
            left += 1                      # skip
        if window_sum == k:                # Is 1 == 1? Yes
            count += 1                     # count = 0 + 1 = 1 (found subarray [1])
                                           # Iteration 2: right = 1
        window_sum += arr[right]           # window_sum = 1 + arr[1] = 1 + 1 = 2
        while window_sum > k and left <= right:  # Is 2 > 1 and 0 <= 1? Yes
            window_sum -= arr[left]        # window_sum = 2 - arr[0] = 2 - 1 = 1
            left += 1                      # left = 0 + 1 = 1
        while window_sum > k and left <= right:  # Is 1 > 1 and 1 <= 1? No
            window_sum -= arr[left]        # skip
            left += 1                      # skip
        if window_sum == k:                # Is 1 == 1? Yes
            count += 1                     # count = 1 + 1 = 2 (found subarray [1])
    return count                           # Return 2 (total subarrays found)

# Test the function
print(count_subarrays_with_sum([1, 1], 1))  # Output: 2 ([1], [1])

# ----------------------------------------------------------------------------------
# Solution with output 

def count_subarrays_with_sum(arr, k):      # arr = [1, 2, 3], k = 3
    count = 0                              # count = 0 (start with no subarrays found)
    window_sum = 0                         # window_sum = 0 (start with no total)
    left = 0                               # left = 0 (left pointer at start)
    for right in range(len(arr)):          # right = 0 to 2 (len = 3)
                                           # Iteration 1: right = 0
        window_sum += arr[right]           # window_sum = 0 + arr[0] = 0 + 1 = 1
        while window_sum > k and left <= right:  # Is 1 > 3 and 0 <= 0? No
            window_sum -= arr[left]        # skip
            left += 1                      # skip
        if window_sum == k:                # Is 1 == 3? No
            count += 1                     # skip
                                           # Iteration 2: right = 1
        window_sum += arr[right]           # window_sum = 1 + arr[1] = 1 + 2 = 3
        while window_sum > k and left <= right:  # Is 3 > 3 and 0 <= 1? No
            window_sum -= arr[left]        # skip
            left += 1                      # skip
        if window_sum == k:                # Is 3 == 3? Yes
            count += 1                     # count = 0 + 1 = 1 (found subarray [1, 2])
                                           # Iteration 3: right = 2
        window_sum += arr[right]           # window_sum = 3 + arr[2] = 3 + 3 = 6
        while window_sum > k and left <= right:  # Is 6 > 3 and 0 <= 2? Yes
            window_sum -= arr[left]        # window_sum = 6 - arr[0] = 6 - 1 = 5
            left += 1                      # left = 0 + 1 = 1
        while window_sum > k and left <= right:  # Is 5 > 3 and 1 <= 2? Yes
            window_sum -= arr[left]        # window_sum = 5 - arr[1] = 5 - 2 = 3
            left += 1                      # left = 1 + 1 = 2
        while window_sum > k and left <= right:  # Is 3 > 3 and 2 <= 2? No
            window_sum -= arr[left]        # skip
            left += 1                      # skip
        if window_sum == k:                # Is 3 == 3? Yes
            count += 1                     # count = 1 + 1 = 2 (found subarray [3])
    return count                           # Return 2 (total subarrays found)


print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 ([1, 2], [3])