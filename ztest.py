# 2. Count Subarrays with Sum K
"""
Task: Count the number of contiguous subarrays that sum up to a given value k. Assume non-negative numbers.

Example 1: [1, 2, 3]    k=3 → 2 ([1, 2], [3])
"""

def count_subarrays_with_sum(arr, k):
    

print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 (subarrays [1, 2] and [3] sum to 3)




def count_subarrays_with_sum(arr, k):
    count = 0
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > k and left <= right:
            window_sum -= arr[left]
            left += 1

        if window_sum == k:
            count += 1

    return count

print(count_subarrays_with_sum([1, 2, 3], 3))  # Output: 2 (subarrays [1, 2] and [3] sum to 3)

