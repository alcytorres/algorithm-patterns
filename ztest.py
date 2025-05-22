# 5. Average of Sliding Window
"""
Task: Compute the list of averages for all contiguous subarrays of size k. If the input array is shorter than 'k' return [].

Example: [1, 2, 3, 4], k=2 → [1.5, 2.5, 3.5]

Why: Directly supports Maximum Average Subarray I.
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
print(sliding_window_average([2, 4, 6, 8], 2))  # Output: [3, 5, 7]
print(sliding_window_average([1, 2, 10], 2))  # Output: [1.5, 6.0]




