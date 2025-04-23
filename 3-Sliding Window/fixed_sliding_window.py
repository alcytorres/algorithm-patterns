"""
Use the Fixed Sliding Window and Dynamic Sliding Window templates to solve these problems 
"""

"""
Task: Given an integer array nums and an integer k, find maximum average of any contiguous subarray of size k
Example: [1, 2, 3, 4], k=2 → 3.5
"""

# Fixed-size sliding window
def sliding_window_fixed(arr, k):
    # Initialize
    window_sum = sum(arr[:k]) 
    
    # # Set up the initial window
    average = window_sum / k  
    
    max_result = window_sum # Initialize result
    
    # Slide the window across the array
    for i in range(k, len(arr)):          
        window_sum = window_sum - arr[i - k] + arr[i]  # Add new element, remove old element
        max_result = max(max_result, window_sum)  # Update max_result
    
    return max_result / k

print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5


# ----------------------------------------------------------------------------------
# Concise Solution with annotations → (I used the template as a starting point and cut out what I did not need)
def sliding_window_fixed(arr, k):          # arr = [1, 2, 3, 4], k = 2
    # Initialize
    window_sum = sum(arr[:k])              # arr[:2] = [1, 2] → window_sum = 1 + 2 = 3
    
    # Set up the initial window
    max_result = window_sum / k            # max_result = 3 / 2 = 1.5 (average of [1, 2])
    
    # Slide the window across the array
    for i in range(k, len(arr)):           # i = 2 to 3 (k = 2, len = 4)
                                           # Iteration 1: i = 2
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 3 - arr[0] + arr[2] = 3 - 1 + 3 = 5
        current_average = window_sum / k   # current_average = 5 / 2 = 2.5 (average of [2, 3])
        max_result = max(max_result, current_average)  # max(1.5, 2.5) = 2.5, max_result = 2.5
                                           # Iteration 2: i = 3
        window_sum = window_sum - arr[i - k] + arr[i]  # window_sum = 5 - arr[1] + arr[3] = 5 - 2 + 4 = 7
        current_average = window_sum / k   # current_average = 7 / 2 = 3.5 (average of [3, 4])
        max_result = max(max_result, current_average)  # max(2.5, 3.5) = 3.5, max_result = 3.5
    
    return max_result                      # Return 3.5 (highest average found)


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5


# ----------------------------------------------------------------------------------
# Full Solution with annotations 

def sliding_window_fixed(arr, k):          # arr = [1, 2, 3, 4], k = 2
    # Initialize
    window_sum = 0                         # window_sum = 0 (start with no total)
    
    # Set up the initial window
    for i in range(k):                     # i = 0 to 1 (k = 2)
                                           # Iteration 1: i = 0
        window_sum += arr[i]               # window_sum = 0 + arr[0] = 0 + 1 = 1
                                           # Iteration 2: i = 1
        window_sum += arr[i]               # window_sum = 1 + arr[1] = 1 + 2 = 3
    
    max_result = window_sum / k            # max_result = 3 / 2 = 1.5 (average of [1, 2])
    
    # Slide the window across the array
    for i in range(k, len(arr)):           # i = 2 to 3 (k = 2, len = 4)
                                           # Iteration 1: i = 2
        window_sum += arr[i] - arr[i - k]  # window_sum = 3 + arr[2] - arr[0] = 3 + 3 - 1 = 5
        current_average = window_sum / k   # current_average = 5 / 2 = 2.5 (average of [2, 3])
        max_result = max(max_result, current_average)  # max(1.5, 2.5) = 2.5, max_result = 2.5
                                           # Iteration 2: i = 3
        window_sum += arr[i] - arr[i - k]  # window_sum = 5 + arr[3] - arr[1] = 5 + 4 - 2 = 7
        current_average = window_sum / k   # current_average = 7 / 2 = 3.5 (average of [3, 4])
        max_result = max(max_result, current_average)  # max(2.5, 3.5) = 3.5, max_result = 3.5
    
    return max_result                      # Return 3.5 (highest average found)


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5
