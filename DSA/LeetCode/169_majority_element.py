# 169. Majority Element
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3, 2, 3]
    Output: 3

Example 2:
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Example 3:
    Input: nums = [3, 2, 2, 3]
    Output: Invalid Input. There must be a majority for this algo to work even if running it outputs 2 or 3. 

# Why: Practices Boyer-Moore Voting Algorithm for efficient majority element detection.

https://www.youtube.com/watch?v=c1B3LZQtZ_s

Solution: https://leetcode.com/problems/majority-element/description/
"""

def majority_element(nums): 
    # 1️⃣ Initialize variables
    answer = -1
    count = 0

    # 2️⃣ Iterate through the array
    for num in nums:
        if count == 0:
            answer = num
        
        # 3️⃣ Update count: increment if num matches answer, decrement otherwise
        if answer == num:
            count += 1
        else:
            count -= 1

    # 4️⃣ Return the majority element
    return answer

print(majority_element([2, 1, 2, 2, 2, 3]))  # Output: 2

# Time: O(N)
# Space: O(1)


# Test Solution
# answer = -1    
# count  = 0    


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def majority_element(nums): 
    # 1️⃣ Initialize variables
    answer = -1
    count = 0

    # 2️⃣ Iterate through the array
    for num in nums:
        if count == 0:
            answer = num
        
        # 3️⃣Update count: increment if num matches answer, decrement otherwise
        if answer == num:
            count += 1
        else:
            count -= 1

    # 4️⃣ Return the majority element
    return answer

print(majority_element([2, 1, 2, 2, 2, 3]))  # Output: 2

# print(majority_element([3, 2, 3]))  # Output: 3
# print(majority_element([3, 2, 1, 1, 2, 2, 2, 3, 2]))  # Output: 2




# --------------------------------------------------------------
# Brute Force
def majority_element_brute_force(nums):
    n = len(nums)  # Get length of array
    threshold = n // 2  # Majority requires > n/2 occurrences

    # Count occurrences of each number
    for num in nums:  # Check each number
        count = 0  # Reset count for current number
        for other in nums:  # Count how many times num appears
            if other == num:  # If numbers match
                count += 1  # Increment count
            if count > threshold:  # If count exceeds n/2
                return num  # Return majority element

    return -1  # Return -1 if no majority (though problem guarantees one)

    # Time: O(n²)
    # Space: O (1)




# --------------------------------------------------------------
# Task: Find the majority element in an array, which appears more than ⌊n / 2⌋ times.
# Assumption: The majority element always exists in the array.
# Example: nums = [2, 1, 2, 2, 2, 3] → Output = 2 (2 appears 4 times, ⌊6/2⌋ = 3, 4 > 3)

def majority_element(nums):  # Example: nums = [2, 1, 2, 2, 2, 3]

    # 1️⃣ Initialize variables
    # Initialize answer to -1 to store the candidate for majority element
    # Why? We need a placeholder for the potential majority element
    answer = -1  # answer = -1

    # Initialize count to track the "vote" count for the current candidate
    # Why? Boyer-Moore algorithm uses a counter to eliminate non-majority elements
    count = 0  # count = 0

    # 2️⃣ Iterate through the array
    # Loop through each number in the array
    # Why? We process each element to identify the majority element
    for num in nums:  # num takes values [2, 1, 2, 2, 2, 3]
        # --- Iteration 1: num = 2 ---
        # If count is 0, set the current number as the new candidate
        # Why? A count of 0 means previous candidates were canceled out
        if count == 0:  # count = 0, true
            answer = num  # answer = 2
        # Update count: increment if num matches answer, decrement otherwise
        # Why? This simulates "pairing" majority and non-majority elements
        if answer == num:  # answer = 2, num = 2, true
            count += 1  # count = 0 + 1 = 1
        else:
            count -= 1  # skip
        # After Iteration 1: answer = 2, count = 1

        # --- Iteration 2: num = 1 ---
        if num == 1:
            if count == 0:  # count = 1, false, skip
                answer = num
            if answer == num:  # answer = 2, num = 1, false
                count += 1  # skip
            else:
                count -= 1  # count = 1 - 1 = 0
            # After Iteration 2: answer = 2, count = 0

        # --- Iteration 3: num = 2 ---
        if num == 2:
            if count == 0:  # count = 0, true
                answer = num  # answer = 2 (unchanged, but reaffirmed)
            if answer == num:  # answer = 2, num = 2, true
                count += 1  # count = 0 + 1 = 1
            else:
                count -= 1
            # After Iteration 3: answer = 2, count = 1

        # --- Iteration 4: num = 2 ---
        if num == 2:
            if count == 0:  # count = 1, false, skip
                answer = num
            if answer == num:  # answer = 2, num = 2, true
                count += 1  # count = 1 + 1 = 2
            else:
                count -= 1
            # After Iteration 4: answer = 2, count = 2

        # --- Iteration 5: num = 2 ---
        if num == 2:
            if count == 0:  # count = 2, false, skip
                answer = num
            if answer == num:  # answer = 2, num = 2, true
                count += 1  # count = 2 + 1 = 3
            else:
                count -= 1
            # After Iteration 5: answer = 2, count = 3

        # --- Iteration 6: num = 3 ---
        if num == 3:
            if count == 0:  # count = 3, false, skip
                answer = num
            if answer == num:  # answer = 2, num = 3, false
                count += 1  # skip
            else:
                count -= 1  # count = 3 - 1 = 2
            # After Iteration 6: answer = 2, count = 2

    # 3️⃣ Return the majority element
    # Why? The Boyer-Moore algorithm guarantees that answer is the majority element if it exists
    return answer  # answer = 2


print(majority_element([2, 1, 2, 2, 2, 3]))  # Output: 2