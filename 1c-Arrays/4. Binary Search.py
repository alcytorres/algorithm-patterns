# Sorting and Searching: Binary Search
"""
Task: Implement binary search on a sorted array to find the index of a target element.

Example 1: [1, 2, 3, 4], target=3 → 2
Example 2: [1, 2, 3, 4], target=5 → -1

Why: Teaches efficient searching in sorted data.
"""

def binary_search(arr, target):
    # 1️⃣ Initialize two pointers for the search range
    left = 0
    right = len(arr) - 1
    
    # 2️⃣ Search until pointers cross
    while left <= right:
        mid = (left + right) // 2  # Calculate middle index
        if arr[mid] == target:  # Target found
            return mid
        elif arr[mid] < target:  # Target is in the right half
            left = mid + 1
        else:  # Target is in the left half
            right = mid - 1
    
    # 3️⃣ Target not found
    return -1

print(binary_search([1, 2, 3, 4], 3))  # Output: 2
print(binary_search([1, 2, 3, 4], 5))  # Output: -1


# Simple Breakdown
"""
Finds a target in a sorted array using binary search.
- Repeatedly halves the search space by comparing the middle element.
- Time Complexity: O(log n), Space Complexity: O(1).
- Efficient and introduces logarithmic searching.
"""