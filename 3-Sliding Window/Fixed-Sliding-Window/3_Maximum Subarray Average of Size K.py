# Maximum Subarray Average of Size K
"""
Task: Given an integer array nums and an integer k, find maximum average of any contiguous subarray of size k. If the array has fewer than k elements, return None.
Example 1: [1, 2, 3, 4], k=2 → 3.5
Example 2: [10, 2, 4],   k=2 → 6
"""

# Fixed-size sliding window
def sliding_window_fixed(arr, k):        

    if len(arr) < k:                      
        return None            
                
    # Initialize the first window
    window_sum = sum(arr[:k])           
    
    # Compute initial result for first window
    max_result = window_sum / k   # Initialize result      
    
    # Slide the window across the array
    for i in range(k, len(arr)):                                      
        window_sum = window_sum - arr[i - k] + arr[i]  # Add new element, remove old element
        current_average = window_sum / k   
        max_result = max(max_result, current_average)  # Update max_result
    
    return max_result                      # Return highest average found


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5
# print(sliding_window_fixed([10, 2, 4], 2))    # Output: 6


# ----------------------------------------------------------------------------------
# Concise Solution with annotations → (I used the template as a starting point and cut out what I did not need)

def sliding_window_fixed(arr, k):          # arr = [1, 2, 3, 4], k = 2

    # Input Validation  
    if len(arr) < k:                       # Is len(arr) = 4 < k = 2? No
        return None                        # skip
    
    # Initialize the first window
    window_sum = sum(arr[:k])              # arr[:2] = [1, 2] → window_sum = 1 + 2 = 3
    
    # Compute initial result for first window
    max_result = window_sum / k            # max_result = 3 / 2 = 1.5 (average of [1, 2])
    
    # Slide the window across the array
    for i in range(k, len(arr)):           # i = 2 to 3
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

