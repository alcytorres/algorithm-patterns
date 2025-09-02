# Sliding Window Techniques in Python

# Generic Template for Dynamic Sliding Window problems.
def sliding_window(arr):
    left = 0          # Left bound of the window
    curr = 0          # Tracks constraint metric (e.g., sum, product, count)
    answer = 0        # Tracks the result (e.g., max length, count of subarrays)
    
    for right in range(len(arr)):  # Iterate right pointer over array
        # Do logic to "add" arr[right] to window (e.g., update sum, product, count)
        
        while WINDOW_CONDITION_BROKEN:  
        # Replace with condition for invalid window (e.g., curr > k)
        # Do logic to "remove" arr[left] from curr (e.g., window)
            left += 1  # Move left pointer forward
            
        # Do logic to update answer (e.g., max length, count subarrays)
    
    return answer  # Return final result

# Time: O(n) - Right and left pointers each move at most n times (amortized O(1) per iteration).

# Space: O(1) - Typically uses a constant number of variables, unless additional data structures are needed.



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Example 1: Longest Subarray with Sum Less Than or Equal to k
# Finds the length of the longest subarray with sum <= k using sliding window.
def longest_subarray_sum(nums, k):
    left = 0       # Left bound of the window
    curr = 0       # Tracks sum of current window
    ans = 0        # Tracks length of longest valid subarray
    
    for right in range(len(nums)):  # Iterate right pointer over array
        curr += nums[right]         # Add element to window sum
        
        while curr > k:            # Shrink window while sum exceeds k
            curr -= nums[left]     # Remove leftmost element from sum
            left += 1              # Move left pointer forward
            
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans

print(longest_subarray_sum([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))  
# Output: 4  -->  [4, 2, 1, 1]

# Time: O(n) - Right pointer moves n times, left pointer moves at most n times (amortized O(1) per iteration).
# Space: O(1) - Uses only three integer variables (left, curr, ans).


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Example 2: Longest Substring with At Most One "0"
# Finds the longest substring with at most one "0" by flipping at most one "0" to "1". 

# In other words "what is the longest substring that contains at most one "0"?

def longest_substring_one_zero(s):
    left = 0          # Left bound of the window
    curr = 0          # Tracks count of "0"s in current window
    ans = 0           # Tracks length of longest valid substring
    
    for right in range(len(s)):  # Iterate right pointer over string
        if s[right] == "0":      # If current character is "0"
            curr += 1            # Increment zero count
        
        while curr > 1:          # Shrink window while zeros exceed 1
            if s[left] == "0":   # If leftmost character is "0"
                curr -= 1        # Decrement zero count
            left += 1            # Move left pointer forward
            
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans

print(longest_substring_one_zero("11001011"))  
# Output: 4  --> Represents substring "1011" (indices 4-7, length 4), with one "0" flipped to "1" for all "1"s.

# Time: O(n) - Right pointer moves n times, left pointer moves at most n times (amortized O(1) per iteration).

# Space: O(1) - Uses only three integer variables (left, curr, ans).


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Example 3: Number of Subarrays with Product Less Than k
# Counts subarrays where product of elements is strictly less than k.

# Link: https://leetcode.com/problems/subarray-product-less-than-k/

def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:        # If k <= 1, no valid subarrays possible (since nums are positive)
        return 0
    
    left = 0          # Left bound of the window
    curr = 1          # Tracks product of current window
    ans = 0        # Tracks number of valid subarrays
    
    for right in range(len(nums)):  # Iterate right pointer over array
        curr *= nums[right]         # Multiply element to window product
        
        while curr >= k:           # Shrink window while product is >= k
            curr //= nums[left]    # Divide out leftmost element. 
            left += 1              # Move left pointer forward
            
        ans += right - left + 1  # Add number of valid subarrays ending at right
    
    return ans

print(num_subarrays_product_less_than_k([10, 5, 2, 6], 100))  
# Output: 8
# [10]
# [10, 5]
# [5]
# [5, 2]
# [2]
# [5, 2, 6]
# [2, 6]
# [6]

print(num_subarrays_product_less_than_k([2, 3], 7))  
# Output: 3  
# [2], [2, 3], [3]

# Time: O(n) - Right pointer moves n times, left pointer moves at most n times (amortized O(1) per iteration).

# Space: O(1) - Uses only three integer variables (left, curr, ans).


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Super simple demo of sliding window with multiplication and division
nums = [2, 4, 5]  # Basic array
curr = 1          # Start with product = 1
print("Initial curr:", curr)  # Output: 1

# Add elements to window (multiply)
curr *= nums[0]   # Include nums[0] (2), curr = 1 * 2
print("After curr *= nums[0]:", curr)  # Output: 2
curr *= nums[1]   # Include nums[1] (4), curr = 2 * 4
print("After curr *= nums[1]:", curr)  # Output: 8
curr *= nums[2]   # Include nums[2] (5), curr = 8 * 5
print("After curr *= nums[2]:", curr)  # Output: 40

# Remove element from window (divide)
curr //= nums[0]   # Remove nums[0] (2), curr = 40 / 2
print("After curr //= nums[0]:", curr)  # Output: 20.0
curr //= nums[1]   # Remove nums[1] (4), curr = 20 / 4
print("After curr //= nums[1]:", curr)  # Output: 5.0



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Example 4: Largest Sum of Subarray with Fixed Length k
# Finds the subarray of length k with the largest sum.
def find_best_subarray(nums, k):
    curr = 0          # Tracks sum of current window
    
    # Build first window of size k
    for i in range(k):  # Iterate over first k elements
        curr += nums[i]  # Add to window sum
    
    ans = curr       # Initialize answer with first window's sum
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):  # Start from index k
        curr += nums[i] - nums[i-k]     # Add the new element, subtract the leftmost element
        ans = max(ans, curr)  # Update max sum
    
    return ans

print(find_best_subarray([1, 4, 6, 2], 2))  
# Output: 10  →  4 + 6 = 10

# Time: O(n) - Builds first window in O(k), then slides n-k times with O(1) operations per iteration.

# Space: O(1) - Uses only two integer variables (curr, answer).





# ––––––––––––––––––––––––––––––––––––––––––––––––––
"""
How to Know Whether to Use 1 or 2 pointers in a Sliding Window?

Fixed Window: If the problem specifies a fixed window length (e.g., exactly k elements), use one pointer to slide a window of size k, updating by adding/removing elements at specific offsets.

Dynamic Window: If the problem involves finding subarrays/substrings with a constraint (e.g., sum, count, or product threshold), use two pointers (left, right) to adjust window size dynamically.


Key Indicator: Check if the problem defines a fixed window size (use one pointer) or a variable window based on a condition (use two pointers).
"""