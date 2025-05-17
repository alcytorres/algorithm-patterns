# 2. Count Subarrays with Sum K
"""
Task: Count the number of contiguous subarrays that sum up to a given value k. Assume non-negative numbers.

Example 1: [1, 2, 3], k=3 → 2 ([1, 2], [3])
Example 2: [1, 2, 3], k=8 → 0 (no subarray sums to 8)
Example 3: [2, 2, 2, 2], k=4 → 3 ([2, 2], [2, 2], [2, 2])
Example 4: [0, 0, 0], k=0 → 3 ([0], [0], [0])
Example 5: [1, 3, 2, 1], k=3 → 2 ([3], [2, 1])
Why: Practices maintaining a window with a condition.
"""

def count_subarrays_with_sum(arr, k):
    # 1️⃣ Initialize variables
    count = 0
    window_sum = 0
    left = 0

    # 2️⃣ Iterate over array with right pointer
    for right in range(len(arr)):

        # 3️⃣ Add current element to window sum
        window_sum += arr[right]

        # 4️⃣ Shrink window if sum exceeds k
        while window_sum > k and left <= right:
            window_sum -= arr[left]  # Shrink window
            left += 1

        # 5️⃣ Check if window sum equals k
        if window_sum == k:
            count += 1

    # 6️⃣ Return total count
    return count


print(count_subarrays_with_sum([1, 2, 3], 3))     # Output: 2 ([1, 2], [3])
print(count_subarrays_with_sum([1, 2, 3], 8))     # Output: 0 (no subarray sums to 8)
print(count_subarrays_with_sum([2, 2, 2, 2], 4))  # Output: 3 ([2, 2], [2, 2], [2, 2])
print(count_subarrays_with_sum([0, 0, 0], 0))     # Output: 3 ([0], [0], [0])
print(count_subarrays_with_sum([1, 3, 2, 1], 3))  # Output: 2 ([3], [2, 1])

# print(count_subarrays_with_sum([1, 1, 1], 1))  # Output: 3
# print(count_subarrays_with_sum([1, 1, 1], 2))  # Output: 2
# print(count_subarrays_with_sum([1, 1, 1], 3))  # Output: 1



def count_subarrays_with_sum(arr, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    return count

# print(count_subarrays_with_sum([1, 1, 1], 2))  # Output: 2
