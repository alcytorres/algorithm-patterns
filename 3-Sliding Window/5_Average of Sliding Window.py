# 5. Average of Sliding Window
"""
Task: Compute the list of averages for all contiguous subarrays of size k. If the input array is shorter than 'k' return [].

Example 1: [1, 2, 3], k=2 → [1.5, 2.5]
Example 2: [1, 2, 3, 4], k=2 → [1.5, 2.5, 3.5]

Why: Practices efficient sliding window technique to compute averages without recalculating sums
     Directly supports Maximum Average Subarray I.
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

print(sliding_window_average([1, 2, 3], 2))  # Output: [1.5, 2.5]
print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]
# print(sliding_window_average([2, 4, 6, 8], 2))  # Output: [3, 5, 7]
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
        window_sum = window_sum - arr[i - k] + arr[i]  # Slide the window: subtract the leftmost element, add the new right element
        averages.append(window_sum / k)  # Calculate the new average and append it to the list

    # 5️⃣ Return the list of averages
    return averages        # Return the list of all averages


print(sliding_window_average([1, 2, 3], 2))  # Output: [1.5, 2.5]


"""
How does this work?:  window_sum = window_sum - arr[i - k] + arr[i]: 
    - The line window_sum = window_sum - arr[i - k] + arr[i] slides a window of k numbers through the array. For [1, 2, 3], k=2, the window starts at [1, 2] (sum = 3). To get the next window [2, 3]:
        - Subtract the number leaving (arr[i - k], e.g., arr[0] = 1).
        - Add the number entering (arr[i], e.g., arr[2] = 3). So, 3 - 1 + 3 = 5 (sum of [2, 3]). It works because it updates the sum by only changing the one number that goes out and the one that comes in.
"""



# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown
# Task: Compute the list of averages for all contiguous subarrays of size k.
# Example: arr = [1, 2, 3, 4], k = 2 → Output = [1.5, 2.5, 3.5]

def sliding_window_average(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

    # 1️⃣ Check if array is too short
    # If the array length is less than k, return an empty list
    # Why? We can't form any subarray of size k if the array is too small
    if len(arr) < k:        # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return []           # skip

    # 2️⃣ Compute the sum of the first window
    # Sum the first k elements to get the initial window sum
    # Why? This gives us the sum for the first subarray of size k
    window_sum = sum(arr[:k])  # arr[:2] = [1, 2], sum = 1 + 2 = 3
                               # window_sum = 3

    # 3️⃣ Compute the average of the first window
    # Create a list with the average of the first window
    # Why? We need to store the average (sum/k) for the first subarray
    averages = [window_sum / k]  # window_sum = 3, k = 2, 3/2 = 1.5
                                 # averages = [1.5]

    # 4️⃣ Slide the window and compute averages for remaining windows
    # Loop through the array starting from index k to process each window
    # Why? Each iteration slides the window by one element to compute the next average
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 0: i = 2 ---
        # Update the window sum by removing the first element of the previous window
        # and adding the current element
        # Why? This efficiently updates the sum without recalculating the entire window
        window_sum = window_sum - arr[i - k] + arr[i]  # i = 2, i-k = 2-2 = 0
                                                       # arr[0] = 1, arr[2] = 3
                                                       # window_sum = 3 - 1 + 3 = 5

        # Compute the average for the current window and append it
        # Why? We need the average (sum/k) for this window
        averages.append(window_sum / k)  # window_sum = 5, k = 2, 5/2 = 2.5
                                        # averages = [1.5, 2.5]
        # After Iteration 0: window_sum = 5, averages = [1.5, 2.5]
        # Current window: [2, 3] (sum = 5, average = 2.5)

        # --- Iteration 1: i = 3 ---
        if i == 3:
            window_sum = window_sum - arr[i - k] + arr[i]  # i = 3, i-k = 3-2 = 1
                                                           # arr[1] = 2, arr[3] = 4
                                                           # window_sum = 5 - 2 + 4 = 7

            averages.append(window_sum / k)  # window_sum = 7, k = 2, 7/2 = 3.5
                                            # averages = [1.5, 2.5, 3.5]
            # After Iteration 1: window_sum = 7, averages = [1.5, 2.5, 3.5]
            # Current window: [3, 4] (sum = 7, average = 3.5)

    # 5️⃣ Return the list of averages
    # Why? averages contains the average of each contiguous subarray of size k
    return averages            # averages = [1.5, 2.5, 3.5]


print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]







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

def sliding_window_average(arr, k):         # arr = [1, 2, 3, 4], k = 2
    if len(arr) < k:                        # Is len(arr) = 4 < k = 2? No → False
        return []                           # skip
    window_sum = sum(arr[:k])               # arr[:2] = [1, 2] → window_sum = 1 + 2 = 3
    averages = [window_sum / k]             # averages = [3 / 2] = [1.5]
    for i in range(k, len(arr)):            # i = 2 to 3 (k = 2, len = 4)
                                            # Iteration 1: i = 2
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 3 - arr[0] + arr[2] = 3 - 1 + 3 = 5
        averages.append(window_sum / k)     # append 5 / 2 = 2.5 → averages = [1.5, 2.5]
                                            # Iteration 2: i = 3
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 5 - arr[1] + arr[3] = 5 - 2 + 4 = 7
        averages.append(window_sum / k)     # append 7 / 2 = 3.5 → averages = [1.5, 2.5, 3.5]

    return averages                         # Return [1.5, 2.5, 3.5]

print(sliding_window_average([1, 2, 3, 4], 2))  # Output: [1.5, 2.5, 3.5]

# ----------------------------------------------------------------------------------
# Solution with output 

def sliding_window_average(arr, k):         # arr = [2, 4, 6, 8], k = 2
    if len(arr) < k:                        # Is len(arr) = 4 < k = 2? No → False
        return []                           # skip
    window_sum = sum(arr[:k])               # arr[:2] = [2, 4] → window_sum = 2 + 4 = 6
    averages = [window_sum / k]             # averages = [6 / 2] = [3.0]
    for i in range(k, len(arr)):            # i = 2 to 3 (k = 2, len = 4)
                                            # Iteration 1: i = 2
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 6 - arr[0] + arr[2] = 6 - 2 + 6 = 10
        averages.append(window_sum / k)     # append 10 / 2 = 5.0 → averages = [3.0, 5.0]
                                            # Iteration 2: i = 3
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 10 - arr[1] + arr[3] = 10 - 4 + 8 = 14
        averages.append(window_sum / k)     # append 14 / 2 = 7.0 → averages = [3.0, 5.0, 7.0]

    return averages                         # Return [3.0, 5.0, 7.0]

print(sliding_window_average([2, 4, 6, 8], 2))  # Output: [3, 5, 7]

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
