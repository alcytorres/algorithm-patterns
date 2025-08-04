# 1004. Max Consecutive Ones III 
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]

# Solution: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/409192/max-consecutive-ones-iii/

def longestOnes(nums, k):
    left = ans = curr = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
# Output: 6

# Time: O(n) - Right pointer moves n times, left moves at most n times (amortized O(1) per iteration).
# Space: O(1) - Uses only three integer variables (left, ans, curr).



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def longestOnes(nums, k):
    left = ans = curr = 0  # Left bound, max length, count of 0's in window
    
    for right in range(len(nums)):  # Iterate right pointer over array
        if nums[right] == 0:       # If current element is 0
            curr += 1              # Increment 0's count
        
        while curr > k:            # Shrink window if 0's exceed k
            if nums[left] == 0:    # If leftmost element is 0
                curr -= 1          # Decrement 0's count
            left += 1              # Move left pointer forward
        
        ans = max(ans, right - left + 1)  # Update max window size
    
    return ans   # Return the maximum length of consecutive 1's possible



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the maximum length of consecutive 1's in a binary array after flipping at most k 0's.
# Example: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 → Output = 6 (flip two 0's to get [1,1,1,1,1,1,1,1,1,1,0])
# Why: Practices sliding window technique to maximize consecutive 1's with a constraint on flips.

def longestOnes(nums, k):  # Example: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

    # 1️⃣ Initialize variables
    # Initialize left pointer for the sliding window
    # Why? We use left to shrink the window when we exceed k zeros
    left = 0  # left = 0

    # Initialize answer to track the maximum length of consecutive 1's
    # Why? We need to store the longest valid window
    ans = 0  # ans = 0

    # Initialize current count of zeros in the window
    # Why? We track zeros to ensure we don't use more than k flips
    curr = 0  # curr = 0

    # 2️⃣ Iterate with right pointer
    # Loop through the array with right pointer to expand the window
    # Why? We process each element to build windows and track valid subarrays
    for right in range(len(nums)):  # right goes from 0 to 10 (len(nums) = 11)
        # --- Iteration 1: right = 0 ---
        # Increment curr if the current element is 0
        # Why? We need to count zeros to enforce the k-flip limit
        if nums[right] == 0:  # nums[0] = 1, not 0, skip
            curr += 1  # skip
        # Shrink window if we have more than k zeros
        # Why? We need to maintain at most k zeros in the window
        while curr > k:  # curr = 0, k = 2, 0 > 2 is false, skip
            if nums[left] == 0:
                curr -= 1
            left += 1
        # Update maximum length of valid window
        # Why? The window length (right - left + 1) may be the longest so far
        ans = max(ans, right - left + 1)  # right = 0, left = 0, ans = max(0, 0 - 0 + 1) = 1
        # After Iteration 1: left = 0, curr = 0, ans = 1
        # Current window: [1] (0 zeros, length 1)

        # --- Iteration 2: right = 1 ---
        if right == 1:
            if nums[right] == 0:  # nums[1] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 0, k = 2, 0 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 1, left = 0, ans = max(1, 1 - 0 + 1) = 2
            # After Iteration 2: left = 0, curr = 0, ans = 2
            # Current window: [1, 1] (0 zeros, length 2)

        # --- Iteration 3: right = 2 ---
        if right == 2:
            if nums[right] == 0:  # nums[2] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 0, k = 2, 0 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 2, left = 0, ans = max(2, 2 - 0 + 1) = 3
            # After Iteration 3: left = 0, curr = 0, ans = 3
            # Current window: [1, 1, 1] (0 zeros, length 3)

        # --- Iteration 4: right = 3 ---
        if right == 3:
            if nums[right] == 0:  # nums[3] = 0, true
                curr += 1  # curr = 0 + 1 = 1
            while curr > k:  # curr = 1, k = 2, 1 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 3, left = 0, ans = max(3, 3 - 0 + 1) = 4
            # After Iteration 4: left = 0, curr = 1, ans = 4
            # Current window: [1, 1, 1, 0] (1 zero, length 4)

        # --- Iteration 5: right = 4 ---
        if right == 4:
            if nums[right] == 0:  # nums[4] = 0, true
                curr += 1  # curr = 1 + 1 = 2
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 4, left = 0, ans = max(4, 4 - 0 + 1) = 5
            # After Iteration 5: left = 0, curr = 2, ans = 5
            # Current window: [1, 1, 1, 0, 0] (2 zeros, length 5)

        # --- Iteration 6: right = 5 ---
        if right == 5:
            if nums[right] == 0:  # nums[5] = 0, true
                curr += 1  # curr = 2 + 1 = 3
            while curr > k:  # curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[0] = 1, not 0, skip
                    curr -= 1
                left += 1  # left = 0 + 1 = 1
                # Check again: curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[1] = 1, not 0, skip
                    curr -= 1
                left += 1  # left = 1 + 1 = 2
                # Check again: curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[2] = 1, not 0, skip
                    curr -= 1
                left += 1  # left = 2 + 1 = 3
                # Check again: curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[3] = 0, true
                    curr -= 1  # curr = 3 - 1 = 2
                left += 1  # left = 3 + 1 = 4
                # Check again: curr = 2, k = 2, 2 > 2 is false, exit while
            ans = max(ans, right - left + 1)  # right = 5, left = 4, ans = max(5, 5 - 4 + 1) = 5
            # After Iteration 6: left = 4, curr = 2, ans = 5
            # Current window: [0, 0] (2 zeros, length 2)

        # --- Iteration 7: right = 6 ---
        if right == 6:
            if nums[right] == 0:  # nums[6] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 6, left = 4, ans = max(5, 6 - 4 + 1) = 5
            # After Iteration 7: left = 4, curr = 2, ans = 5
            # Current window: [0, 0, 1] (2 zeros, length 3)

        # --- Iteration 8: right = 7 ---
        if right == 7:
            if nums[right] == 0:  # nums[7] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 7, left = 4, ans = max(5, 7 - 4 + 1) = 5
            # After Iteration 8: left = 4, curr = 2, ans = 5
            # Current window: [0, 0, 1, 1] (2 zeros, length 4)

        # --- Iteration 9: right = 8 ---
        if right == 8:
            if nums[right] == 0:  # nums[8] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 8, left = 4, ans = max(5, 8 - 4 + 1) = 5
            # After Iteration 9: left = 4, curr = 2, ans = 5
            # Current window: [0, 0, 1, 1, 1] (2 zeros, length 5)

        # --- Iteration 10: right = 9 ---
        if right == 9:
            if nums[right] == 0:  # nums[9] = 1, not 0, skip
                curr += 1
            while curr > k:  # curr = 2, k = 2, 2 > 2 is false, skip
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)  # right = 9, left = 4, ans = max(5, 9 - 4 + 1) = 6
            # After Iteration 10: left = 4, curr = 2, ans = 6
            # Current window: [0, 0, 1, 1, 1, 1] (2 zeros, length 6)

        # --- Iteration 11: right = 10 ---
        if right == 10:
            if nums[right] == 0:  # nums[10] = 0, true
                curr += 1  # curr = 2 + 1 = 3
            while curr > k:  # curr = 3, k = 2, 3 > 2 is true
                if nums[left] == 0:  # nums[4] = 0, true
                    curr -= 1  # curr = 3 - 1 = 2
                left += 1  # left = 4 + 1 = 5
                # Check again: curr = 2, k = 2, 2 > 2 is false, exit while
            ans = max(ans, right - left + 1)  # right = 10, left = 5, ans = max(6, 10 - 5 + 1) = 6
            # After Iteration 11: left = 5, curr = 2, ans = 6
            # Current window: [0, 1, 1, 1, 1, 0] (2 zeros, length 6)

    # 3️⃣ Return the maximum length
    # Why? ans contains the length of the longest window with at most k zeros
    return ans  # ans = 6


print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  
# Output: 6