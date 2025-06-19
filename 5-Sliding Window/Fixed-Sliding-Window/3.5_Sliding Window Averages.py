# 3.5. Sliding Window Averages
"""
Task: Compute the list of averages for all contiguous subarrays of size k. 
    - If the input array is shorter than 'k' return [].

Example 1: [1, 2, 3, 4],  k=2 → [1.5, 2.5, 3.5]
Example 2: [2, 4, 6, 10], k=2 → [3, 5, 8]

Why: Practices efficient sliding window technique to compute averages without recalculating sums. Directly related to Maximum Average Subarray I.
"""

def sliding_window_average(arr, k):

    # 1️⃣ Check if array is too short
    if len(arr) < k:
        return []
    
    # 2️⃣ Compute the sum of the first window
    window_sum = sum(arr[:k])

    # 3️⃣ Compute the average of the first window
    averages = [window_sum / k]  

    # 4️⃣ Slide the window and compute averages for remaining windows
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        averages.append(window_sum / k)
    
    # 5️⃣ Return the list of averages
    return averages

print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]

# print(sliding_window_average([2, 4, 6, 10], 2))  # Output: [3, 5, 8]
# print(sliding_window_average([1, 2, 10], 2))  # Output: [1.5, 6.0]


# Simple Breakdown
def sliding_window_average(arr, k):   # Define the function that takes an array 'arr' and integer 'k'
    """
    Computes the average of all subarrays of size k.
    
    - Uses a sliding window to compute sums, then averages them.
    - Time Complexity: O(n), Space Complexity: O(n) for result.
    - Simple and beginner-friendly with clear steps.
    """

    # 1️⃣ Check if array is too short
    if len(arr) < k:       # Check if the array is shorter than 'k'
        return []          # Return an empty list since no subarrays of size k are possible
    
    # 2️⃣ Compute the sum of the first window
    window_sum = sum(arr[:k])  # Calculate the sum of the first k elements (first window)

    # 3️⃣ Compute the average of the first window
    averages = [window_sum / k]  # Add the average of the first window to the result list

    # 4️⃣ Slide the window and compute averages for remaining windows
    for i in range(k, len(arr)):  # Loop from index k to the end of the array
        window_sum += arr[i] - arr[i - k]  # Slide the window: subtract the leftmost element, add the new right element
        averages.append(window_sum / k)  # Calculate the new average and append it to the list

    # 5️⃣ Return the list of averages
    return averages        # Return the list of all averages


print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]


"""
How does this work?:  window_sum = window_sum - arr[i - k] + arr[i]: 
    - The line window_sum = window_sum - arr[i - k] + arr[i] slides a window of k numbers through the array. For [1, 2, 3], k=2, the window starts at [1, 2] (sum = 3). To get the next window [2, 3]:

        - Subtract the number leaving (arr[i - k], e.g., arr[0] = 1).
    
        - Add the number entering (arr[i], e.g., arr[2] = 3). So, 3 - 1 + 3 = 5 (sum of [2, 3]). It works because it updates the sum by only changing the one number that goes out and the one that comes in.
"""


# ----------------------------------------------------------------------------------
# Task: Compute the list of averages for all contiguous subarrays of size k.


def sliding_window_average(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

    # 1️⃣ Check if array is too short
    # If the array length is less than k, return an empty list
    # Why? We can't form any subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return []  # skip

    # 2️⃣ Compute the sum of the first window
    # Sum the first k elements to get the initial window sum
    # Why? We need the sum to calculate the average for the first subarray
    window_sum = sum(arr[:k])  # arr[:2] = [1, 2], window_sum = 1 + 2 = 3

    # 3️⃣ Compute the average of the first window
    # Initialize the list with the average of the first window
    # Why? We need to store the average (sum/k) for the first subarray
    averages = [window_sum / k]  # window_sum = 3, k = 2, 3 / 2 = 1.5
                                 # averages = [1.5]

    # 4️⃣ Slide the window and compute averages for remaining windows
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to compute averages for all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update sum: add new element, subtract the first element of the previous window
        # Why? This efficiently updates the sum without recalculating the entire window
        window_sum += arr[i] - arr[i - k]  # i = 2, arr[2] = 3, i-k = 2-2 = 0, arr[0] = 1
                                           # window_sum = 3 + 3 - 1 = 5

        # Compute and append the average for the current window
        # Why? We need to store the average for each window
        averages.append(window_sum / k)  # window_sum = 5, k = 2, 5 / 2 = 2.5
                                        # averages = [1.5, 2.5]
        # After Iteration 1: window_sum = 5, averages = [1.5, 2.5]
        # Current window: [2, 3] (sum = 5, average = 2.5)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update sum
            window_sum += arr[i] - arr[i - k]  # i = 3, arr[3] = 4, i-k = 3-2 = 1, arr[1] = 2
                                               # window_sum = 5 + 4 - 2 = 7

            # Compute and append the average
            averages.append(window_sum / k)  # window_sum = 7, k = 2, 7 / 2 = 3.5
                                            # averages = [1.5, 2.5, 3.5]
            # After Iteration 2: window_sum = 7, averages = [1.5, 2.5, 3.5]
            # Current window: [3, 4] (sum = 7, average = 3.5)

    # 5️⃣ Return the list of averages
    # Why? averages contains the average of each contiguous subarray of size k
    return averages  # averages = [1.5, 2.5, 3.5]


print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]


