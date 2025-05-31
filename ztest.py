# 2. Check if Array is Sorted
"""
# Task: Determine if an array is sorted in ascending order. If not return false.
# Example: [1, 2, 3, 4] → True,  [1, 3, 2] → False

# Why: Practices moving pointers to compare adjacent elements.
"""

def is_sorted(arr):
    # 1️⃣ Handle edge cases: empty or single-element arrays are always sorted
    if len(arr) < 2:
        return True
    
    # 2️⃣ Initialize pointers for comparing adjacent elements
    left, right = 0, 1

    # 3️⃣ Loop through the array to compare adjacent elements
    while right < len(arr):
        if arr[left] > arr[right]:
            return False
        left += 1
        right += 1

    # 4️⃣ Return result
    return True

print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False


def is_sorted(arr):

    if len(arr) < 2:
        return True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    # 4️⃣ Return result
    return True

print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([1, 3, 2]))     # Output: False
