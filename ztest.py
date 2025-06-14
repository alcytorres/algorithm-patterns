# Task: Find the maximum difference (max - min) in any group of k consecutive elements in an array.
# If the array has fewer than k elements, return None.
# Example: arr = [1, 2, 6], k = 2 → Output = 4 (subarray [2, 6] has max 6, min 2, difference 6 - 2 = 4)
# Why: Practices sliding window technique to compute differences efficiently.

def max_difference_sliding_window(arr, k):  # Example: arr = [1, 2, 6], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 3, k = 2, 3 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Take the first k elements as the initial window
    # Why? We need to compute the difference for the first subarray of size k
    window = arr[:k]  # arr[:2] = [1, 2], window = [1, 2]

    # 3️⃣ Compute initial result for first window
    # Calculate the difference between max and min of the first window
    # Why? This is the starting point for comparing differences across all windows
    max_diff = max(window) - min(window)  # max([1, 2]) = 2, min([1, 2]) = 1
                                         # max_diff = 2 - 1 = 1

    # 4️⃣ Slide the window across the array and update result
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 3, i goes from 2 to 2
        # --- Iteration 1: i = 2 ---
        # Get the next window of k elements
        # Why? We need the current subarray to compute its max-min difference
        window = arr[i - k + 1:i + 1]  # i = 2, i-k+1 = 2-2+1 = 1, i+1 = 3
                                       # arr[1:3] = [2, 6], window = [2, 6]

        # Compute the difference for the current window
        # Why? We need to compare this window's difference with the maximum found
        current_diff = max(window) - min(window)  # max([2, 6]) = 6, min([2, 6]) = 2
                                                 # current_diff = 6 - 2 = 4

        # Update the maximum difference if the current difference is larger
        # Why? We want the largest difference across all windows
        max_diff = max(max_diff, current_diff)  # max(1, 4) = 4
                                                # max_diff = 4
        # After Iteration 1: max_diff = 4, window = [2, 6]

    # 5️⃣ Return the maximum difference
    # Why? max_diff contains the largest difference found in any k-sized subarray
    return max_diff  # max_diff = 4


# Test the function
print(max_difference_sliding_window([1, 2, 6], 2))  # Output: 4
# ([2, 6] has max=6, min=2, diff=6-2=4)
