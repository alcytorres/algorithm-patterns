"""
Sorting and Searching
Task: Find the index of the first occurrence of a target in a sorted array with duplicates.

Example 1: [1, 2, 2, 3], target=2 → 1
Example 2: [1, 2, 3, 4], target=5 → -1

Why: Introduces modified binary search for handling duplicates.
"""

def find_first_occurrence(arr, target):
    # 1️⃣ Initialize pointers and result variable
    left = 0
    right = len(arr) - 1
    result = -1
    
    # 2️⃣ Binary search with a twist: keep searching left when target is found
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid  # Record potential answer
            right = mid - 1  # Continue searching left for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # 3️⃣ Return the earliest index or -1 if not found
    return result

# Test the function
print(find_first_occurrence([1, 2, 2, 3], 2))  # Output: 1
print(find_first_occurrence([1, 2, 3, 4], 5))  # Output: -1

# Simple Breakdown
"""
Finds the first occurrence of a target in a sorted array.
- Modifies binary search to continue left when target is found.
- Time Complexity: O(log n), Space Complexity: O(1).
- Teaches adaptation of binary search for duplicates.
"""