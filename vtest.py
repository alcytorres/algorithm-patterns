
# Write a function that divides 3 number
def fn(a, b, c):
    return a / b / c

print(fn(10, 10, 10))



# Write a function that divides 3 number without using the divsion symbol?
def fn(a, b, c):
    return a * (1/b) * (1/c)

print(fn(10, 10, 10))






# algorithms.py
# ==========================================================
# Collection of common searching and sorting algorithms for interviews
# ==========================================================
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Binary Search (iterative version – most common in interviews)

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
# Linear Search

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
# Merge Sort
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
# Quick Sort

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
# Insertion Sort

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
# Bubble Sort

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









# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# “Count how many times a target appears in a sorted array.”

# Input: nums = [1, 2, 2, 2, 3, 4]
# target = 2
# Output: 3

def lower_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

def upper_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l

nums = [1, 2, 2, 2, 3, 4]
target = 2

print(upper_bound(nums, target) - lower_bound(nums, target))  # 3


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Given a sorted array that may contain duplicates, return the index of the FIRST occurrence of target.
# If target does not exist, return -1.

# Input: nums = [1, 2, 2, 2, 3]
# target = 2
# Output: 1

def first_occurrence(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    if l < len(nums) and nums[l] == target:
        return l
    return -1

nums = [1, 2, 2, 2, 3]
print(first_occurrence(nums, target))  # Output: 1


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Given a sorted array that may contain duplicates, return the index of the LAST occurrence of target.
# If target does not exist, return -1.

# Input: nums = [1, 2, 2, 2, 3]
# target = 2
# Output: 3

def last_occurrence(nums, target):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid

    if l - 1 >= 0 and nums[l - 1] == target:
        return l - 1
    return -1

nums = [1, 2, 2, 2, 3]
print(last_occurrence(nums, target))  # Output: 3