# common_algorithms.py
# ==========================================================
# Searching & Sorting Algorithms — Interview Reference
# Target: entry-level SWE at startups / mid-tier companies
# ==========================================================
#
# PRIORITY SUMMARY (for interview prep)
# ──────────────────────────────────────────────────────────
# Algorithm       | Time          | Space   | Priority     |
# ──────────────────────────────────────────────────────────
# Binary Search   | O(log n)      | O(1)    | CRITICAL     | 
# Linear Search   | O(n)          | O(1)    | SKIP         | 
# Merge Sort      | O(n log n)    | O(n)    | MODERATE     | 
# Quick Sort      | O(n log n)*   | O(log n)| LOW-MODERATE | 
# Insertion Sort  | O(n²)         | O(1)    | LOW          | 
# Bubble Sort     | O(n²)         | O(1)    | SKIP         | 
# ──────────────────────────────────────────────────────────
# * Quick Sort worst case is O(n²) when pivot is always min/max.
#
# Notes
# ──────────────────────────────────────────────────────────
#   - Binary Search: Most tested algo. Know variants cold.
#   - Linear Search: Just a for loop. You already know it.
#   - Merge Sort: Know concept + merge helper (reusable).
#   - Quick Sort: Know partition idea + trade-offs vs merge sort.
#   - Insertion Sort: Only relevant for "nearly sorted" discussions.
#   - Bubble Sort: No interview value. Don't study.
#
# HOW EACH ALGO WORKS (high-level)
# ──────────────────────────────────────────────────────────
#   Binary Search:
#     Requires a sorted array. Check the middle element — if it's the target,
#     done. If target is larger, discard the left half; if smaller, discard
#     the right half. Repeat until found or the search space is empty.
#
#   Linear Search:
#     Walk through the array one element at a time. Return the index
#     when you find the target. That's it — just a for loop.
#
#   Merge Sort:
#     Split the array in half repeatedly until each piece is 1 element.
#     Then merge those pieces back together in sorted order.
#     The "merge" step walks two sorted halves with two pointers,
#     always picking the smaller element. That's why it's stable and O(n log n).
#
#   Quick Sort:
#     Pick a pivot element. Partition the array so everything smaller
#     goes left of the pivot and everything larger goes right.
#     Then recursively sort the left and right sides.
#     Fast in practice but O(n²) if you always pick the worst pivot.
#
#   Insertion Sort:
#     Walk left to right. For each element, slide it backwards into
#     its correct position among the already-sorted elements to its left.
#     Like sorting cards in your hand. O(n) if the array is already sorted
#     because nothing needs to slide.
#
#   Bubble Sort:
#     Repeatedly walk through the array swapping adjacent elements
#     that are out of order. Largest elements "bubble up" to the end.
#     Repeat until no swaps are needed. Simple but slow.


# HIGHER-YIELD PATTERNS TO STUDY INSTEAD OF MEMORIZING SORTS:
#   - Hash maps (frequency counting, two-sum)
#   - Two pointers (sorted arrays, palindromes)
#   - Sliding window (subarray/substring problems)
#   - Binary search variants (leftmost, rightmost, insert position)
#   - Basic recursion / DFS (trees, backtracking)
#   - Stack problems (valid parentheses, monotonic stack)
#
# ==========================================================


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Binary Search (iterative) | Time: O(log N) | Space: O(1)
# CRITICAL — appears directly and as a pattern in many problems.
# Know: left <= right vs left < right, mid +/- 1 edge cases, variants.
# Variants: find first/last occurrence, search insert position, rotated array.

def binary_search(arr, target):
    """Binary Search - O(log n) on sorted array"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # not found

arr = [1, 3, 5, 7, 9]
target = 7
print("Binary Search (target 7):", binary_search(arr, 7))
# Output: 3


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Linear Search | Time: O(N) | Space: O(1)
# SKIP — it's just looping through an array. You already know this.

def linear_search(arr, target):
    """Linear Search - O(n), unsorted arrays"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found

arr = [4, 2, 7, 1, 9]
target = 7
print("Linear Search (target 7):", linear_search(arr, target))
# Output: 2


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Merge Sort | Time: O(N log N) | Space: O(N)
# MODERATE — unlikely to implement from scratch, but know the concept.
# Stable sort, uses extra space. The merge() helper is reusable
# (shows up in "merge two sorted lists/arrays" problems).
# Teaches divide-and-conquer pattern.
def merge_sort(arr):
    """Merge Sort - O(n log n), stable"""
    if len(arr) <= 1:
        return arr[:]
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [5, 2, 8, 3, 1]
print("Merge Sort:", merge_sort(arr))
# Output: [1, 2, 3, 5, 8]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Quick Sort | Time: O(N log N) avg, O(N²) worst | Space: O(log N) stack
# LOW-MODERATE — don't memorize full implementation.
# Know: in-place but NOT stable. Worst case when pivot is always min/max.
# The partition() idea is useful (appears in "sort colors", "kth largest").
# Be able to compare trade-offs vs merge sort if asked.

def quick_sort(arr, low=0, high=None):
    """Quick Sort - O(n log n) average, in-place"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

arr = [5, 1, 8, 3, 2]
print("Quick Sort:", quick_sort(arr[:]))
 # Output: [1, 2, 3, 5, 8]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Insertion Sort | Time: O(N²) avg, O(N) best | Space: O(1)
# LOW — know it's efficient for small or nearly sorted data.
# Best case O(n) when array is already sorted. That's the key fact.

def insertion_sort(arr):
    """Insertion Sort - O(n²), good for small/nearly sorted arrays"""
    arr = arr[:]  # avoid modifying original
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [4, 3, 1, 2]
print("Insertion Sort:", insertion_sort(arr))
# Output: [1, 2, 3, 4]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Bubble Sort | Time: O(N²) | Space: O(1)
# SKIP — no interview value. Slowest simple sort, no practical advantage.

def bubble_sort(arr):
    """Bubble Sort - O(n²), simple"""
    n = len(arr)
    arr = arr[:]  # avoid modifying original
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [4, 3, 1, 2]
print("Bubble Sort:", bubble_sort(arr))
# Output: [1, 2, 3, 4]


