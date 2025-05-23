"""
Use the Fixed Sliding Window templates to solve these problems 

# Maximum Difference (max -min) in K Consecutive Elements
# Maximum Product of K Consecutive Elements
# Maximum Subarray Average of Size K
# Maximum Subarray Sum of Size K
# Minimum Subarray Sum of Size K

"""

"""
Task: Given an integer array nums and an integer k, find maximum average of any contiguous subarray of size k. If the array has fewer than k elements, return None.
Example 1: [1, 2, 3, 4], k=2 → 3.5
Example 2: [10, 2, 4],   k=2 → 6
"""

# Fixed-size sliding window Template
def sliding_window_fixed(arr, k):      

    # Input Validation  
    if len(arr) < k:                      
        return None            
                
    # Initialize the first window
    window_sum = sum(arr[:k])           
    
    # Compute initial result for first window
    max_result = window_sum / k       
    
    # Slide the window across the array and update result
    for i in range(k, len(arr)):                                      
        window_sum = window_sum - arr[i - k] + arr[i]  # Add new element, remove old element
        current_average = window_sum / k   
        max_result = max(max_result, current_average)  # Update max_result
    
    return max_result                      # Return highest average found


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5
# print(sliding_window_fixed([10, 2, 4], 2))    # Output: 6


# ----------------------------------------------------------------------------------
# Fixed-size sliding window Template with annotations → (Moving forward use this template as a starting point and cut out what is not needed)

def sliding_window_fixed(arr, k):          # arr = [1, 2, 3, 4], k = 2
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




# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# Incremental Sliding Window Template

def sliding_window_fixed(arr, k):          # arr = [1, 2, 3, 4], k = 2
    if len(arr) < k:                      
        return None                       
    
    # Initialize the first window
    window_sum = 0                       

    # Compute initial result for first window
    for i in range(k):                                                        
        window_sum += arr[i]               

    max_result = window_sum / k           
    
    # Slide the window across the array
    for i in range(k, len(arr)):                      
        window_sum += arr[i] - arr[i - k]  
        current_average = window_sum / k   
        max_result = max(max_result, current_average)  
    
    return max_result                      # Return 3.5 (highest average found)


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 3.5

# ----------------------------------------------------------------------------------
# Incremental Sliding Window Template with annoations 


def sliding_window_fixed(arr, k):          # arr = [1, 2, 3, 4], k = 2
    if len(arr) < k:                       # Is len(arr) = 4 < k = 2? No
        return None                        # skip
    
    # Initialize the first window
    window_sum = 0                         # window_sum = 0 (start with no total)
    
    # Compute initial result for first window
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

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------