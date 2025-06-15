"""
Guide to Solving Two-Pointer Problems

Key Strategies:
   
   1. Identify the Goal: Determine if the problem involves comparing, swapping, or finding pairs (e.g., sum, difference, merging).

   2. Choose Pointer Placement:
   - Opposite Ends: For problems like reversing (`reverse_array`) or summing first/last (`sum_first_last`).
   - Adjacent/Same Direction: For checking order (`is_sorted`) or finding pairs in sorted arrays (`find_pair_with_difference`).
   - Two Arrays: For merging sorted arrays (`merge_sorted_arrays`).

   3. Move Pointers Smartly:
   - Move based on conditions (e.g., `diff < target` → `right += 1` in `find_pair_with_difference`).
   - Avoid overlap with `if left == right: right += 1` when distinct elements are needed.

   4. Handle Edge Cases:
   - Empty arrays (`if not arr: return 0` in `sum_first_last`).
   - Single elements (`if len(arr) < 2: return True` in `is_sorted`).
   - Array too short (`if len(arr) < k: return None`).

   5. Sort if Needed: Sort for pair-finding problems to simplify pointer logic (e.g., `arr.sort()` in `find_pair_with_difference`).

Key Plan in Your Head:
   1. Ask: Does the problem involve pairs, order, or merging? (e.g., reverse → opposite ends, merge → two arrays).

   2. Set up pointers: Decide if they start at ends, adjacent, or separate arrays.

   3. Loop: Use `while` or `for` to move pointers based on a condition (e.g., `while left < right` or `while right < len(arr)`).

   4. Act: Compare (`arr[i] > arr[j]`), swap (`arr[left], arr[right] = arr[right], arr[left]`), or collect (`result.append()`).

   5. Check Overlap: If pointers might collide, add `if left == right: right += 1`.

   6. Handle Leftovers: For merging, add remaining elements (`result.extend(arr1[i:])`).

   7. Test Edges: Empty, single-element, or invalid inputs.

Key Lines of Code to Know:

   1. Initialize Pointers:
   - Opposite ends: `left, right = 0, len(arr) - 1` (e.g., `reverse_array`)
   - Adjacent: `i, j = 0, 1` (e.g., `is_sorted`, `find_pair_with_difference`)
   - Two arrays: `i, j = 0, 0` (e.g., `merge_sorted_arrays`)

   2. Loop Structure:
   - `while left < right:` (opposite ends, e.g., `reverse_array`)
   - `while right < len(arr):` (same direction, e.g., `find_pair_with_difference`)
   - `while i < len(arr1) and j < len(arr2):` (two arrays, e.g., `merge_sorted_arrays`)

   3. Action:
   - Compare: `if arr[i] > arr[j]:` (e.g., `is_sorted`)
   - Swap: `arr[left], arr[right] = arr[right], arr[left]` (e.g., `reverse_array`)
   - Collect: `result.append(arr[i])` (e.g., `merge_sorted_arrays`)
   - Compute: `diff = arr[right] - arr[left]` (e.g., `find_pair_with_difference`)

   4. Move Pointers:
   - `left += 1; right -= 1` (opposite, e.g., `reverse_array`)
   - `i += 1; j += 1` (adjacent, e.g., `is_sorted`)
   - `right += 1` or `left += 1` (conditional, e.g., `find_pair_with_difference`)

   5. Avoid Overlap:
   - `if left == right: right += 1` (e.g., `find_pair_with_difference`)

   6. Handle Leftovers:
   - `result.extend(arr1[i:]); result.extend(arr2[j:])` (e.g., `merge_sorted_arrays`)

   7. Edge Cases:
   - `if not arr: return 0` (e.g., `sum_first_last`)
   - `if len(arr) < 2: return True` (e.g., `is_sorted`)

Other Key Notes:
   - Sorting: Use `arr.sort()` for pair-finding (e.g., `find_pair_with_difference`) to make pointer movement predictable (O(n log n)).
   
   - Array Order: Sorting is not always needed (e.g., `reverse_array`, `is_sorted` work on unsorted arrays).

   - Efficiency: Two pointers often give O(n) time (or O(n log n) with sorting) and O(1) space (excluding output).

   - Visualize: Think of pointers as fingers moving on the array, either toward each other, together, or across two arrays.
"""


# Template 1: Two Pointers from Opposite Ends
def two_pointer_opposite(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
    # Process the pair (arr[left], arr[right]).
    # For example, compare sum to target, or check if they match some condition.
    # if <some condition based on arr[left] and arr[right]>:
    # Maybe return True/indices or record the result.
        return (left, right)
    elif <condition to move left pointer>:
        left += 1 # Move left pointer to the right
    else:
        right -= 1 # Move right pointer to the left
    # If we exit the loop, either we found a result or there is no valid pair.
    return None



# Template 2: Two Pointers moving in the Same Direction
def two_pointer_same_direction(arr):
    i = 0
    # j will move from 0 to n-1 (or 1 to n-1 if i starts at 0)
    for j in range(len(arr)):
    # Use j to explore and i to build or compare
    if <some condition involving arr[j] (and maybe arr[i])>:
    # If condition met, update arr[i] or record result
    arr[i] = arr[j] # (for example, keep this element)
    i += 1 # move the slow pointer
    # After loop, first i elements of arr might be the result,
    # or use i as a count of valid elements.
    return i



