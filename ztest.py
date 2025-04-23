# """
# Use the Fixed Sliding Window and Dynamic Sliding Window templates to solve these problems 
# """

# """
# Task: Given an integer array nums and an integer k, find maximum average of any contiguous subarray of size k
# Example: [1, 2, 3, 4], k=2 → 3.5
# """


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


print(sliding_window_fixed([1, 2, 3, 4], 2))  # Output: 


def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    max_result = window_sum / k
    print(f"Initial: window_sum={window_sum}, max_result={max_result}")
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        current_average = window_sum / k
        print(f"i={i}, window_sum={window_sum}, current_average={current_average}")
        max_result = max(max_result, current_average)
    return max_result

print(sliding_window_fixed([1, 2, 3, 4], 2))
