# 5. Partition Array into Equal Sums
"""
Task: Check if an array can be split into two non-empty contiguous parts with equal sums.
      i.e. Split an array into two next-to-each-other parts, where each part has at least one number and both parts add up to the same total.

Example 1: [1, 4, 2, 3]   → True (1 + 4 = 2 + 3)
Example 2: [1, 2, 3]      → True (1 + 2 = 3)
Example 3: [1, 4, 10, 15] → True (1 + 4 + 10 = 15)
Example 4: [1, 2, 6]      → False (no split gives equal sums)

Why: Reinforces cumulative sum usage.
"""

def can_partition(arr):

    # 1️⃣ Compute total sum and check if it can be split evenly
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    # 2️⃣ Calculate target sum for each part
    target = total_sum // 2

    # 3️⃣ Initialize prefix sum
    prefix_sum = 0

    # 4️⃣ Iterate through array to find split point
    for num in arr:
        prefix_sum += num
        if prefix_sum == target:
            return True
        
    # 5️⃣ Return False if no split point is found
    return False

print(can_partition([1, 4, 2, 3]))  # Output: True (1 + 4 = 2 + 3)