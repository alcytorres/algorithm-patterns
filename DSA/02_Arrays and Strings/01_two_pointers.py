# Two Pointers: Move Pointers from Edges Toward Center
# Illustrates two-pointer technique with pointers starting at array ends, moving inward.
def two_pointers_edges(arr):
    left = 0                    # Start left pointer at index 0
    right = len(arr) - 1        # Start right pointer at last index

    while left < right:         # Continue until pointers meet
        # Problem-specific logic here
        # Decide to:
        # 1. left += 1
        # 2. right -= 1
        # 3. Both left += 1 and right -= 1
        pass

# Time: O(n) - Pointers start n elements apart and meet after at most n/2 iterations, with O(1) work per iteration.
# Space: O(1) - Uses only two integer pointers, regardless of input size.



# Check if a String is a Palindrome
# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# Checks if string s is a palindrome by comparing characters from both ends.
def is_palindrome(s):
    left = 0                    # Start left pointer at index 0
    right = len(s) - 1          # Start right pointer at last index

    while left < right:         # Continue until pointers meet
        if s[left] != s[right]: # If characters don't match, not a palindrome
            return False
        left += 1               # Move left pointer inward
        right -= 1              # Move right pointer inward
    return True                 # String is a palindrome

print(is_palindrome("racecar"))  # Output: True

# Time: O(n) - Checks up to n/2 character pairs in a string of length n, with O(1) comparisons per iteration.
# Space: O(1) - Uses only two integer pointers (left, right), with no additional data structures.



# Find Pair with Target Sum in Sorted Array
# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

# Checks if sorted array has two numbers summing to target using two pointers.
def find_pair_sum(nums, target):
    left = 0                    # Start left pointer at index 0
    right = len(nums) - 1       # Start right pointer at last index

    while left < right:         # Continue until pointers meet
        # curr is the current sum
        curr = nums[left] + nums[right]  # Sum of elements at pointers
        if curr == target:   # Found a pair
            return True
        elif curr < target:  # Sum too small, need larger number
            left += 1
        else:                # Sum too large, need smaller number
            right -= 1
    return False             # No pair found

print(find_pair_sum([1, 2, 4, 6, 8, 9, 14, 15], 13))  # Output: True

# Time: O(n) - Pointers traverse a sorted array of length n, meeting after at most n iterations, with O(1) operations per iteration.
# Space: O(1) - Uses only two integer pointers (left, right) and a constant amount of extra space.



# Two Pointers: Move Along Two Arrays Simultaneously
# Demonstrates two-pointer technique for two arrays, moving pointers forward.
def two_pointers_two_arrays(arr1, arr2):
    i = 0                       # Pointer for arr1, starts at index 0
    j = 0                       # Pointer for arr2, starts at index 0

    while i < len(arr1) and j < len(arr2):  # Continue until one array is exhausted
        # Problem-specific logic here
        # Decide to:
        # 1. i += 1
        # 2. j += 1
        # 3. Both i += 1 and j += 1
        pass

    # Handle remaining elements in arr1
    while i < len(arr1):
        # Problem-specific logic here
        i += 1

    # Handle remaining elements in arr2
    while j < len(arr2):
        # Problem-specific logic here
        j += 1

# Time: O(n + m) - Processes all elements of two arrays (lengths n and m) in a single pass, with O(1) work per iteration.
# Space: O(1) - Uses only two integer pointers (i, j), with no additional data structures beyond input/output.



# Merge Two Sorted Arrays into One Sorted Array
# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

# Merges two sorted arrays into a new sorted array using two pointers.
def merge_sorted_arrays(arr1, arr2):
    ans = []                 # Result array to store merged elements
    i = j = 0                # Pointer for arr1, and arr2 starts at index 0

    # Compare elements while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Add smaller element from arr1
            ans.append(arr1[i])
            i += 1
        else:                   # Add smaller element from arr2
            ans.append(arr2[j])
            j += 1

    # Add remaining elements from arr1, if any
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans                  # Return merged sorted array

print(merge_sorted_arrays([1, 4, 7, 20], [3, 5, 6]))

# Time: O(n + m) - Iterates through all elements of two arrays (lengths n and m) once, with O(1) operations per iteration.
# Space: O(n + m) - Stores the merged result in an output array of size n + m, excluding input arrays as per convention.



# Alternative Solution: Merge Two Sorted Arrays into One Sorted Array
def merge_sorted_arrays(arr1, arr2):
    ans = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    ans.extend(arr1[i:])
    ans.extend(arr2[j:])

    return ans

print(merge_sorted_arrays([1, 4, 7, 20], [3, 5, 6]))  
# Output [1, 3, 4, 5, 6, 7, 20]



# Check if String s is a Subsequence of String t
# Example 4: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# Checks if s is a subsequence of t by tracking matching characters in order.
def is_subsequence(s, t):
    i = j = 0            # Pointer for string s, and t starts at index 0

    while i < len(s) and j < len(t):  # Continue until s or t is exhausted
        if s[i] == t[j]:        # Match found, move s pointer
            i += 1
        j += 1                  # Always move t pointer

    return i == len(s)          # True if all characters in s were found

string1 = "ace"
string2 = "abcde"
print(is_subsequence(string1, string2))


# Time: O(n + m) - Scans string t (length m) once while checking for characters of s (length n), with O(1) comparisons per iteration.
# Space: O(1) - Uses only two integer pointers (i, j) for tracking positions in s and t.
