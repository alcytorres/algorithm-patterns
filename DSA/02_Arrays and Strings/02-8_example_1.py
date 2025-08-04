# Example 1: Longest Subarray with Sum Less Than or Equal to k

# Finds the length of the longest subarray with sum <= k using sliding window.

# Example 1: nums = [1, 2, 1, 2, 4, 2], k = 6
# Output: 4 (subarray [2, 1, 2, 1], sum = 6)

# Example 2: nums = [3, 1, 2, 7, 4, 2, 1, 1, 5], k = 8
# Output = 4 (subarray [4, 2, 1, 1], sum = 8)

def longest_subarray_sum(nums, k):
    left = curr = ans = 0        
    
    for right in range(len(nums)): 
        curr += nums[right]         
        
        while curr > k:            
            curr -= nums[left]     
            left += 1             
            
        ans = max(ans, right - left + 1)  
    
    return ans


nums = [1, 2, 1, 2, 4, 2]
print(longest_subarray_sum(nums, 8))
# Output: 4  --> Subarray [1, 2, 1, 2] (length 4, sum 6) is the longest subarray with sum <= 6.

# Time: O(n) - Right pointer moves n times, left pointer moves at most n times (amortized O(1) per iteration).
# Space: O(1) - Uses only three integer variables (left, curr, ans).


# Trace Overview
# right = 0  0  1  2  3  4         5
# curr  = 0  1  3  4  6  10 9 7 6  8 6
# ans   = 0  1  2  3  4         4    4 
# left  = 0                 1 2 3    4

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def longest_subarray_sum(nums, k):
    left = 0          # Left bound of the window
    curr = 0          # Tracks sum of current window
    ans = 0           # Tracks length of longest valid subarray
    
    for right in range(len(nums)):  # Iterate right pointer over array
        curr += nums[right]         # Add element to window sum
        
        while curr > k:            # Shrink window while sum exceeds k
            curr -= nums[left]     # Remove leftmost element from sum
            left += 1              # Move left pointer forward
            
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans   # Return length of longest subarray


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the length of the longest contiguous subarray with sum <= k.
# Example: nums = [3, 1, 2, 7, 4, 2, 1, 1, 5], k = 8 → Output = 4 (subarray [4, 2, 1, 1], sum = 8)
# Why: Practices sliding window technique to find the longest subarray meeting a sum constraint.

def longest_subarray_sum(nums, k):  # Example: nums = [3, 1, 2, 7, 4, 2, 1, 1, 5], k = 8

    # 1️⃣ Initialize variables
    # Initialize left pointer for the sliding window
    # Why? We use left to shrink the window when the sum exceeds k
    left = 0  # left = 0

    # Initialize current sum of the window
    # Why? We track the sum of elements in the current window
    curr = 0  # curr = 0

    # Initialize answer to track the length of the longest valid subarray
    # Why? We need to store the maximum length of subarrays with sum <= k
    ans = 0  # ans = 0

    # 2️⃣ Iterate with right pointer
    # Loop through the array with right pointer to expand the window
    # Why? We process each element to build windows and track valid subarrays
    for right in range(len(nums)):  # right goes from 0 to 8 (len(nums) = 9)
        # --- Iteration 1: right = 0 ---
        # Add the current element to the window sum
        # Why? We expand the window by including the new element
        curr += nums[right]  # nums[0] = 3, curr = 0 + 3 = 3

        # Shrink window while sum exceeds k
        # Why? We need the sum to be <= k for valid subarrays
        while curr > k:  # curr = 3, k = 8, 3 > 8 is false, skip
            curr -= nums[left]  # skip
            left += 1  # skip
        # Update the maximum length of valid subarrays
        # Why? The current window length (right - left + 1) may be the longest so far
        ans = max(ans, right - left + 1)  # right = 0, left = 0, ans = max(0, 0 - 0 + 1) = 1
        # After Iteration 1: left = 0, curr = 3, ans = 1
        # Current window: [3] (sum = 3)

        # --- Iteration 2: right = 1 ---
        if right == 1:
            curr += nums[right]  # nums[1] = 1, curr = 3 + 1 = 4
            while curr > k:  # curr = 4, k = 8, 4 > 8 is false, skip
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)  # right = 1, left = 0, ans = max(1, 1 - 0 + 1) = 2
            # After Iteration 2: left = 0, curr = 4, ans = 2
            # Current window: [3, 1] (sum = 4)

        # --- Iteration 3: right = 2 ---
        if right == 2:
            curr += nums[right]  # nums[2] = 2, curr = 4 + 2 = 6
            while curr > k:  # curr = 6, k = 8, 6 > 8 is false, skip
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)  # right = 2, left = 0, ans = max(2, 2 - 0 + 1) = 3
            # After Iteration 3: left = 0, curr = 6, ans = 3
            # Current window: [3, 1, 2] (sum = 6)

        # --- Iteration 4: right = 3 ---
        if right == 3:
            curr += nums[right]  # nums[3] = 7, curr = 6 + 7 = 13
            while curr > k:  # curr = 13, k = 8, 13 > 8 is true
                curr -= nums[left]  # nums[0] = 3, curr = 13 - 3 = 10
                left += 1  # left = 0 + 1 = 1
                # Check again: curr = 10, k = 8, 10 > 8 is true
                curr -= nums[left]  # nums[1] = 1, curr = 10 - 1 = 9
                left += 1  # left = 1 + 1 = 2
                # Check again: curr = 9, k = 8, 9 > 8 is true
                curr -= nums[left]  # nums[2] = 2, curr = 9 - 2 = 7
                left += 1  # left = 2 + 1 = 3
                # Check again: curr = 7, k = 8, 7 > 8 is false, exit while
            ans = max(ans, right - left + 1)  # right = 3, left = 3, ans = max(3, 3 - 3 + 1) = 3
            # After Iteration 4: left = 3, curr = 7, ans = 3
            # Current window: [7] (sum = 7)

        # --- Iteration 5: right = 4 ---
        if right == 4:
            curr += nums[right]  # nums[4] = 4, curr = 7 + 4 = 11
            while curr > k:  # curr = 11, k = 8, 11 > 8 is true
                curr -= nums[left]  # nums[3] = 7, curr = 11 - 7 = 4
                left += 1  # left = 3 + 1 = 4
                # Check again: curr = 4, k = 8, 4 > 8 is false, exit while
            ans = max(ans, right - left + 1)  # right = 4, left = 4, ans = max(3, 4 - 4 + 1) = 3
            # After Iteration 5: left = 4, curr = 4, ans = 3
            # Current window: [4] (sum = 4)

        # --- Iteration 6: right = 5 ---
        if right == 5:
            curr += nums[right]  # nums[5] = 2, curr = 4 + 2 = 6
            while curr > k:  # curr = 6, k = 8, 6 > 8 is false, skip
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)  # right = 5, left = 4, ans = max(3, 5 - 4 + 1) = 3
            # After Iteration 6: left = 4, curr = 6, ans = 3
            # Current window: [4, 2] (sum = 6)

        # --- Iteration 7: right = 6 ---
        if right == 6:
            curr += nums[right]  # nums[6] = 1, curr = 6 + 1 = 7
            while curr > k:  # curr = 7, k = 8, 7 > 8 is false, skip
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)  # right = 6, left = 4, ans = max(3, 6 - 4 + 1) = 3
            # After Iteration 7: left = 4, curr = 7, ans = 3
            # Current window: [4, 2, 1] (sum = 7)

        # --- Iteration 8: right = 7 ---
        if right == 7:
            curr += nums[right]  # nums[7] = 1, curr = 7 + 1 = 8
            while curr > k:  # curr = 8, k = 8, 8 > 8 is false, skip
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)  # right = 7, left = 4, ans = max(3, 7 - 4 + 1) = 4
            # After Iteration 8: left = 4, curr = 8, ans = 4
            # Current window: [4, 2, 1, 1] (sum = 8)

        # --- Iteration 9: right = 8 ---
        if right == 8:
            curr += nums[right]  # nums[8] = 5, curr = 8 + 5 = 13
            while curr > k:  # curr = 13, k = 8, 13 > 8 is true
                curr -= nums[left]  # nums[4] = 4, curr = 13 - 4 = 9
                left += 1  # left = 4 + 1 = 5
                # Check again: curr = 9, k = 8, 9 > 8 is true
                curr -= nums[left]  # nums[5] = 2, curr = 9 - 2 = 7
                left += 1  # left = 5 + 1 = 6
                # Check again: curr = 7, k = 8, 7 > 8 is false, exit while
            ans = max(ans, right - left + 1)  # right = 8, left = 6, ans = max(4, 8 - 6 + 1) = 4
            # After Iteration 9: left = 6, curr = 7, ans = 4
            # Current window: [1, 1, 5] (sum = 7)

    # 3️⃣ Return the length of the longest valid subarray
    # Why? ans contains the length of the longest subarray with sum <= k
    return ans  # ans = 4


print(longest_subarray_sum([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))  # Output: 4
# Subarray [4, 2, 1, 1] (length 4, sum 8) is the longest subarray with sum <= 8.