# Find Pair with Target Sum in Sorted Array

# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

def find_pair_sum(nums, target):
    left = 0                    
    right = len(nums) - 1       

    while left < right:         
        curr = nums[left] + nums[right]  
        if curr == target:   
            return True
        elif curr < target:  
            left += 1
        else:                
            right -= 1

    return False   

nums = [1, 3, 4, 6, 8, 10, 12]
target = 14
print(find_pair_sum(nums, target))  
# Output: True -> nums[2] + nums[5] = 4 + 10 = 14 matches the target.


"""
Time: O(n)
  - Two pointers (left, right) each move toward the center once.
  - Each iteration adjusts one pointer, so at most n steps total.
  - No nested loops.

Space: O(1)
  - Only a constant number of variables (left, right, curr) are used.
  - No additional data structures.
  - Overall: O(1) space.


---
Overview for Each Iteration
Input: nums = [1, 3, 4, 6, 8, 10, 12], target = 14

Step: Find pair summing to target using two pointers
l  | r | nums[l] | nums[r] | curr      | curr vs target | Action      | Result
---|---|---------|---------|-------- --|----------------|-------------|--------
0  | 6 | 1       | 12      | 13 (1+12) | < 14           | l+=1        | -
1  | 6 | 3       | 12      | 15 (3+12) | > 14           | r-=1        | -
1  | 5 | 3       | 10      | 13 (3+10) | < 14           | l+=1        | -
2  | 5 | 4       | 10      | 14 (4+10) | == 14          | Return True | True

Final: True ([4, 10])


---------------------------------------------------
Q: When does the loop stop and return True?
    • When nums[left] + nums[right] == target.

    • At that moment, the function immediately returns True and exits — no further pairs are checked.

    
Q: When does the loop stop and return False?
    • When the left and right pointers cross (left >= right).

    • This means every possible pair has been checked, and no pair sums to the target.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
  
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





# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Best Solution

def find_pair_sum(nums, target):
    left = 0                    
    right = len(nums) - 1       

    while left < right:         
        curr = nums[left] + nums[right]  
        if curr == target:   
            return True
        elif curr < target:  
            left += 1
        else:                
            right -= 1

    return False   

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
print(find_pair_sum(nums, target))  
# Output: True -> nums[2] + nums[5] = 4 + 9 = 13 matches the target.



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Given a sorted array of unique integers and a target, return True if a pair sums to the target, False otherwise.
# Example: nums = [1, 2, 4, 6, 8, 9, 14, 15], target = 13 → Output = True (nums[2] + nums[5] = 4 + 9 = 13)
# Why: Practices two-pointer technique on a sorted array to efficiently find a pair with a specific sum.

def find_pair_sum(nums, target):  # Example: nums = [1, 2, 4, 6, 8, 9, 14, 15], target = 13

    # 1️⃣ Initialize pointers
    # Start left pointer at the beginning of the array
    # Why? We need to check pairs starting with smaller numbers
    left = 0  # left = 0

    # Start right pointer at the end of the array
    # Why? We pair with larger numbers to find the target sum
    right = len(nums) - 1  # right = 8 - 1 = 7

    # 2️⃣ Iterate while pointers don't meet
    # Continue until left pointer is less than right pointer
    # Why? Once pointers meet, all possible pairs have been checked
    while left < right:  # left = 0, right = 7, 0 < 7 is true
        # --- Iteration 1 ---
        # Compute the sum of elements at left and right pointers
        # Why? We need to check if this pair sums to the target
        curr = nums[left] + nums[right]  # nums[0] = 1, nums[7] = 15, curr = 1 + 15 = 16

        # Check if current sum equals the target
        # Why? If equal, we've found a valid pair
        if curr == target:  # curr = 16, target = 13, 16 == 13 is false, skip
            return True  # skip
        # If sum is too small, move left pointer to increase sum
        # Why? A larger number is needed, and the array is sorted
        elif curr < target:  # curr = 16, target = 13, 16 < 13 is false, skip
            left += 1
        # If sum is too large, move right pointer to decrease sum
        # Why? A smaller number is needed, and the array is sorted
        else:  # curr = 16 > target = 13, true
            right -= 1  # right = 7 - 1 = 6
        # After Iteration 1: left = 0, right = 6
        # Current pair: nums[0] = 1, nums[6] = 14

        # --- Iteration 2 ---
        if left == 0 and right == 6:
            curr = nums[left] + nums[right]  # nums[0] = 1, nums[6] = 14, curr = 1 + 14 = 15
            if curr == target:  # curr = 15, target = 13, 15 == 13 is false, skip
                return True
            elif curr < target:  # curr = 15, target = 13, 15 < 13 is false, skip
                left += 1
            else:  # curr = 15 > target = 13, true
                right -= 1  # right = 6 - 1 = 5
            # After Iteration 2: left = 0, right = 5
            # Current pair: nums[0] = 1, nums[5] = 9

        # --- Iteration 3 ---
        if left == 0 and right == 5:
            curr = nums[left] + nums[right]  # nums[0] = 1, nums[5] = 9, curr = 1 + 9 = 10
            if curr == target:  # curr = 10, target = 13, 10 == 13 is false
                return True
            elif curr < target:  # curr = 10, target = 13, 10 < 13 is true
                left += 1  # left = 0 + 1 = 1
            else:
                right -= 1
            # After Iteration 3: left = 1, right = 5
            # Current pair: nums[1] = 2, nums[5] = 9

        # --- Iteration 4 ---
        if left == 1 and right == 5:
            curr = nums[left] + nums[right]  # nums[1] = 2, nums[5] = 9, curr = 2 + 9 = 11
            if curr == target:  # curr = 11, target = 13, 11 == 13 is false
                return True
            elif curr < target:  # curr = 11, target = 13, 11 < 13 is true
                left += 1  # left = 1 + 1 = 2
            else:
                right -= 1
            # After Iteration 4: left = 2, right = 5
            # Current pair: nums[2] = 4, nums[5] = 9

        # --- Iteration 5 ---
        if left == 2 and right == 5:
            curr = nums[left] + nums[right]  # nums[2] = 4, nums[5] = 9, curr = 4 + 9 = 13
            if curr == target:  # curr = 13, target = 13, 13 == 13 is true
                return True  # return True
            elif curr < target:
                left += 1
            else:
                right -= 1
            # After Iteration 5: return True (loop exits)

    # 3️⃣ Return False if no pair is found
    # Why? If pointers meet without finding a pair, no valid pair exists
    return False  # skip


nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
print(find_pair_sum(nums, target))  
# Output: True -> nums[2] + nums[5] = 4 + 9 = 13 matches the target.
