# 5. Average of Sliding Window
"""
Task: Compute the list of averages for all contiguous subarrays of size k. If the input array is shorter than 'k' return [].
Example: [1, 2, 3], k=2 → [1.5, 2.5]
Why: Directly supports Maximum Average Subarray I.
"""

def sliding_window_average(arr, k):
    if len(arr) < k:
        return []
    window_sum = sum(arr[:k])
    averages = [window_sum / k]  # First window average
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        averages.append(window_sum / k)
    return averages

print(sliding_window_average([1, 2, 3], 2))  # Output: [1.5, 2.5]
print(sliding_window_average([1, 2, 10], 2))  # Output: [1.5, 6.0]


# Solution
def sliding_window_average(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Computes the average of all subarrays of size k.
    
    - Uses a sliding window to compute sums, then averages them.
    - Time Complexity: O(n), Space Complexity: O(n) for result.
    - Simple and beginner-friendly with clear steps.
    """
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return []          # Return an empty list since no subarrays of size k are possible
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements (first window)
    averages = [window_sum / k]  # Add the average of the first window to the result list
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        averages.append(window_sum / k)  # Calculate the new average and append it to the list
    return averages        # Return the list of all averages

# Test the function
print(sliding_window_average([1, 2, 3], 2))  # Output: [1.5, 2.5]


# ----------------------------------------------------------------------------------
# Solution with output 

def sliding_window_average(arr, k):         # arr = [1, 2, 3], k = 2
    if len(arr) < k:                        # Is len(arr) = 3 < k = 2? No → False
        return []                           # skip
    window_sum = sum(arr[:k])               # arr[:2] = [1, 2] → window_sum = 1 + 2 = 3
    averages = [window_sum / k]             # averages = [3 / 2] = [1.5]
    for i in range(k, len(arr)):            # i = 2 to 2 (k = 2, len = 3)
                                            # Iteration 1: i = 2
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 3 - arr[0] + arr[2] = 3 - 1 + 3 = 5
        averages.append(window_sum / k)     # append 5 / 2 = 2.5 → averages = [1.5, 2.5]
    return averages                         # Return [1.5, 2.5]

print(sliding_window_average([1, 2, 3], 2))  # Output: [1.5, 2.5]

# ----------------------------------------------------------------------------------
# Solution with output 

def sliding_window_average(arr, k):          # arr = [1, 2, 10], k = 2
    if len(arr) < k:                        # Is len(arr) = 3 < k = 2? No → False
        return []                           # skip
    window_sum = sum(arr[:k])               # arr[:2] = [1, 2] → window_sum = 1 + 2 = 3
    averages = [window_sum / k]             # averages = [3 / 2] = [1.5]
    for i in range(k, len(arr)):            # i = 2 to 2 (k = 2, len = 3)
                                            # Iteration 1: i = 2
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 3 - arr[0] + arr[2] = 3 - 1 + 10 = 12
        averages.append(window_sum / k)     # append 12 / 2 = 6.0 → averages = [1.5, 6.0]
    return averages                         # Return [1.5, 6.0]

print(sliding_window_average([1, 2, 10], 2))  # Output: [1.5, 6.0]
