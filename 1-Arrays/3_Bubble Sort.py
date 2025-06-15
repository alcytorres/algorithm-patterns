"""
Sorting and Searching
Task: Implement bubble sort to sort an array in ascending order.

Example 1: [3, 2, 1] → [1, 2, 3]
Example 2: [4, 2, 5, 1] → [1, 2, 4, 5]

Why: Introduces basic sorting concepts and nested loops.
"""

def bubble_sort(arr):
    # 1️⃣ Get the length of the array
    n = len(arr)
    
    # 2️⃣ Outer loop: number of passes
    for i in range(n):
        # 3️⃣ Inner loop: compare and swap adjacent elements
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # If current element is greater than next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap them
    
    # 4️⃣ Return the sorted array
    return arr

# Test the function
print(bubble_sort([3, 2, 1]))      # Output: [1, 2, 3]
print(bubble_sort([4, 2, 5, 1]))  # Output: [1, 2, 4, 5]

# Simple Breakdown
"""
Sorts an array using bubble sort.
- Repeatedly compares and swaps adjacent elements to ‘bubble’ larger ones to the end.
- Time Complexity: O(n^2), Space Complexity: O(1).
- Simple and beginner-friendly, though not the most efficient.
"""