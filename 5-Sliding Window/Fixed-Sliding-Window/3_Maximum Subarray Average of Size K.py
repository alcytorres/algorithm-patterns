# Maximum Subarray Average of Size K
"""
Task: Given an integer array nums and an integer k, find maximum average of any contiguous subarray of size k. 
    - If the array has fewer than k elements, return None.

Example 1: [1, 2, 3, 4], k=2 → 3.5
Example 2: [10, 2, 4],   k=2 → 6

Why: Practices sliding window technique to compute averages efficiently.
"""

def sliding_window_fixed(arr, k):        
    
    # 1️⃣ Input Validation  
    if len(arr) < k:                      
        return None            
                
    # 2️⃣ Initialize the first window
    window_sum = sum(arr[:k])           
    
    # 3️⃣ Compute initial result for first window
    max_result = window_sum / k        
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):                                      
        window_sum += arr[i] - arr[i - k]
        current_average = window_sum / k   
        max_result = max(max_result, current_average)
    
    # 5️⃣ Return max_result
    return max_result                     


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5

# print(sliding_window_fixed([10, 2, 4], 2))    # Output: 6


# Simple Breakdown
def sliding_window_fixed(arr, k):        
    
    # 1️⃣ Input Validation  
    if len(arr) < k:                      
        return None            
                
    # 2️⃣ Initialize the first window
    window_sum = sum(arr[:k])           
    
    # 3️⃣ Compute initial result for first window
    max_result = window_sum / k   # Initialize result      
    
    # 4️⃣ Slide the window across the array
    for i in range(k, len(arr)):                                      
        window_sum += arr[i] - arr[i - k]  # Add new element, remove old element
        current_average = window_sum / k   # Calculate the current average
        max_result = max(max_result, current_average)  # Update max_result
    
    # 5️⃣ Return max_result
    return max_result                     


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5



# ----------------------------------------------------------------------------------
# Task: Find the maximum average of any contiguous subarray of size k in an array. If the array has fewer than k elements, return None.


def sliding_window_fixed(arr, k):  # Example: arr = [1, 2, 3, 4], k = 2

    # 1️⃣ Input Validation
    # Check if the array has fewer than k elements
    # Why? We can't form a subarray of size k if the array is too small
    if len(arr) < k:  # len(arr) = 4, k = 2, 4 < 2 is false, proceed
        return None  # skip

    # 2️⃣ Initialize the first window
    # Compute the sum of the first k elements
    # Why? We need the sum of the first subarray to calculate its average
    window_sum = sum(arr[:k])  # arr[:2] = [1, 2], window_sum = 1 + 2 = 3

    # 3️⃣ Compute initial result for first window
    # Calculate the average of the first window
    # Why? This is the starting point for comparing averages across all windows
    max_result = window_sum / k  # window_sum = 3, k = 2, max_result = 3 / 2 = 1.5

    # 4️⃣ Slide the window across the array
    # Iterate from index k to the end to process each subsequent window
    # Why? We slide the window one element at a time to check all k-sized subarrays
    for i in range(k, len(arr)):  # k = 2, len(arr) = 4, i goes from 2 to 3
        # --- Iteration 1: i = 2 ---
        # Update sum: add new element, subtract the first element of the previous window
        # Why? This efficiently updates the sum without recomputing the entire window
        window_sum += arr[i] - arr[i - k]  # i = 2, arr[2] = 3, i-k = 2-2 = 0, arr[0] = 1
                                           # window_sum = 3 + 3 - 1 = 5

        # Compute the average for the current window
        # Why? We need to compare this window's average with the maximum found
        current_average = window_sum / k  # window_sum = 5, k = 2, current_average = 5 / 2 = 2.5

        # Update the maximum average if the current average is larger
        # Why? We want the largest average across all windows
        max_result = max(max_result, current_average)  # max_result = max(1.5, 2.5) = 2.5
        # After Iteration 1: window_sum = 5, max_result = 2.5
        # Current window: [2, 3] (sum = 5, average = 2.5)

        # --- Iteration 2: i = 3 ---
        if i == 3:
            # Update sum
            window_sum += arr[i] - arr[i - k]  # i = 3, arr[3] = 4, i-k = 3-2 = 1, arr[1] = 2
                                               # window_sum = 5 + 4 - 2 = 7

            # Compute current average
            current_average = window_sum / k  # window_sum = 7, k = 2, current_average = 7 / 2 = 3.5

            # Update maximum average
            max_result = max(max_result, current_average)  # max_result = max(2.5, 3.5) = 3.5
            # After Iteration 2: window_sum = 7, max_result = 3.5
            # Current window: [3, 4] (sum = 7, average = 3.5)

    # 5️⃣ Return max_result
    # Why? max_result contains the largest average found in any k-sized subarray
    return max_result  # max_result = 3.5


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5


