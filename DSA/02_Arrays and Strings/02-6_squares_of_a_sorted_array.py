# 977. Squares of a Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
Example:
    Input: nums = [-4, -1, 0, 3, 10]
    Output:       [0, 1, 9, 16, 100]
    Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
    After sorting, it becomes [0, 1, 9, 16, 100]

Solution: https://leetcode.com/problems/squares-of-a-sorted-array/description/
"""

def sortedSquares(nums):
    n = len(nums)
    ans = [0] * n
    l = 0
    r = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[l]) < abs(nums[r]):
            val = nums[r]
            r -= 1
        else:
            val = nums[l]
            l += 1
        
        ans[i] = val * val
    
    return ans

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  
# Output: [0, 1, 9, 16, 100]

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def sortedSquares(nums):
    n = len(nums)         # Get length of input array
    ans = [0] * n         # Initialize ans array of size n with zeros
    left = 0              # Left pointer starts at beginning of array
    right = n - 1         # Right pointer starts at end of array
    
    for i in range(n - 1, -1, -1):    # Iterate backwards from n-1 to 0 to fill ans
        if abs(nums[left]) < abs(nums[right]):  # Compare absolute values at pointers
            val = nums[right]      # Use right element if its absolute value is larger
            right -= 1                # Move right pointer inward
        else:
            val = nums[left]       # Use left element if its absolute value is larger or equal
            left += 1                 # Move left pointer inward
            
        ans[i] = val * val      # Square the chosen number and store in ans
    return ans                        # Return sorted array of squares


"""
Time: O(N)
  - Let N = length of nums.
  - Two-pointer approach scans from both ends toward the center.
  - Each element is visited and squared exactly once → O(N).
  - No additional sorting step is needed (sorted automatically during construction).
  - Overall: O(N).

Space: O(N)
  - The output array 'ans' holds N squared values.
  - Only a few pointer variables (l, r, i, val) use O(1) space.
  - Overall: O(N).

  - Space: O(1) if output array is ignored

  
Interview Answer: Worst Case

Time: O(N)
  - Each element is processed once.

Space: O(N)
  - Output array stores N squared values.



---
Most IMPORTANT thing to Understand:

• The biggest squared value ALWAYS comes from the number with the largest absolute value.

• Since the array is already sorted:
      • the most negative number is on the LEFT
      • the biggest positive number is on the RIGHT

• Negative numbers become positive after squaring.
  Example:
      (-10)^2 = 100

• So the largest square must come from either:
      • nums[left]
      • nums[right]

• We compare absolute values because:
      abs(-10) = 10
      abs(3) = 3

• We fill the answer array BACKWARDS because we discover the
  largest squares first.


---
Why this code Works:

• Two pointers:
      • left starts at beginning
      • right starts at end

• At every step:
      • compare abs(nums[left]) and abs(nums[right])
      • whichever absolute value is larger produces the larger square

• That larger square belongs at the END of the answer array.

• After using a number:
      • move that pointer inward

• Since we always place the current largest square first,
  the final array becomes automatically sorted.

• No extra sorting is needed.

• Efficiency:
      • Each element is processed once
      • Time: O(N)
      • Better than:
            square everything → sort again
            O(N log N)

• Intuition:
      • Think of it like choosing the strongest player from
        either end of a line.

      • The stronger player (larger absolute value)
        gets placed into the highest remaining position.


---
TLDR:
• This solution works because the largest square must come from either the leftmost negative number or the rightmost positive number, so we compare both ends and fill the result array from back to front.


---
Quick Example Walkthrough:

nums = [-4, -1, 0, 3, 10]

Initial State:

    left = 0  → -4
    right = 4 → 10

    ans = [0, 0, 0, 0, 0]


--------------------------------------------------
Iteration 1:

Compare:
    abs(-4) = 4
    abs(10) = 10

10 is larger.

Square it:
    10^2 = 100

Put at end:
    ans[4] = 100

Move right pointer:
    right = 3

ans:
    [0, 0, 0, 0, 100]


--------------------------------------------------
Iteration 2:

Compare:
    abs(-4) = 4
    abs(3) = 3

4 is larger.

Square it:
    (-4)^2 = 16

Put into ans[3]

Move left pointer:
    left = 1

ans:
    [0, 0, 0, 16, 100]


--------------------------------------------------
Iteration 3:

Compare:
    abs(-1) = 1
    abs(3) = 3

3 is larger.

Square:
    3^2 = 9

Put into ans[2]

Move right:
    right = 2

ans:
    [0, 0, 9, 16, 100]


--------------------------------------------------
Iteration 4:

Compare:
    abs(-1) = 1
    abs(0) = 0

1 is larger.

Square:
    (-1)^2 = 1

Put into ans[1]

Move left:
    left = 2

ans:
    [0, 1, 9, 16, 100]


--------------------------------------------------
Iteration 5:

Only 0 remains.

Square:
    0^2 = 0

Put into ans[0]

Final ans:
    [0, 1, 9, 16, 100]







---
Overview for Each Iteration
Input: nums = [-4, -1, 0, 3, 10]

Step: Square numbers and sort in non-decreasing order
i | l | r | abs(nums[l]) | abs(nums[r]) | val | ans
--|---|---|--------------|--------------|--------|-------------------
- | 0 | 4 | -            | -            | -      | [0, 0, 0, 0, 0]
4 | 0 | 4 | 4            | 10           | 10     | [0, 0, 0, 0, 100]
3 | 0 | 3 | 4            | 3            | -4     | [0, 0, 0, 16, 100]
2 | 1 | 3 | 1            | 3            | 3      | [0, 0, 9, 16, 100]
1 | 1 | 2 | 1            | 0            | -1     | [0, 1, 9, 16, 100]
0 | 2 | 2 | 0            | 0            | 0      | [0, 1, 9, 16, 100]

Final: [0, 1, 9, 16, 100]


"""





# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Tutorial: for i in range(n - 1, -1, -1)

This pattern means:
- Start at index n-1 (the LAST index)
- Stop at -1 (but not including -1)
- Move by -1 each time (counting backwards)

Why it's useful:
- Lets you fill an array from RIGHT → LEFT
- Perfect when the largest values are picked first (like in sortedSquares)
- Removes the need to reverse the final result

Think of it as: "Give me all valid indices, but backwards."
"""

# ---------------------------------------------------------
# Basic Example
# ---------------------------------------------------------
# Goal: Fill an array from RIGHT to LEFT using range(n-1, -1, -1)
n = 5
ans = [None] * n

# Fill ans with its own indices, but backwards.
for i in range(n - 1, -1, -1):
    print(ans)
    ans[i] = i

print(ans)
# Output:
# [None, None, None, None, None]
# [None, None, None, None, 4]
# [None, None, None, 3, 4]
# [None, None, 2, 3, 4]
# [None, 1, 2, 3, 4]
# → [0, 1, 2, 3, 4]

# ---------------------------------------------------------
# Example in a Function (Real DSA Use Case)
# ---------------------------------------------------------
# 977. Squares of a Sorted Array
# Two-pointer trick + fill from the back using range(n-1, -1, -1)

def sortedSquares(nums):
    n = len(nums)
    ans = [0] * n
    l, r = 0, n - 1

    # i goes from last index → 0
    for i in range(n - 1, -1, -1):
        # pick the bigger square from the ends
        if abs(nums[l]) < abs(nums[r]):
            val = nums[r]
            r -= 1
        else:
            val = nums[l]
            l += 1

        # place square in correct sorted position
        ans[i] = val * val

    return ans

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
# Output: [0, 1, 9, 16, 100]

"""
Key takeaways:
  - range(n-1, -1, -1) = indices in reverse order
  - Ideal when your algorithm produces biggest → smallest results
  - Lets you build the final sorted array in ONE pass without reversing
"""





# ––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Valid Solution

def sortedSquares(nums):
    n = len(nums)
    ans = []
    l = 0
    r = n - 1

    while l <= r:
        if abs(nums[l]) < abs(nums[r]):
            val = nums[r]
            r -= 1
        else:
            val = nums[l]
            l += 1
    
        ans.append(val * val)
    
    return ans[::-1]

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  
# Output: [0, 1, 9, 16, 100]











# ––––––––––––––––––––––––––––––––––––––––––––––––
# Less efficeint solution

def sortedSquares(nums):
    return sorted(x*x for x in nums)  # Square each element and sort in one line

nums = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(nums)) 
# Output: [1, 4, 16, 25, 49, 100]


# Time: O(n log n) - Generates n squared values in O(n) time, followed by sorting with Python's Timsort algorithm in O(n log n).

# Space: O(n) - Stores n squared values in the output list, with O(log n) auxiliary space used by Timsort for sorting operations.

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Less efficeint solution

def sortedSquares(nums):
    ans = []
    for num in nums:
        ans.append(num * num)
    
    ans.sort()
    return ans

numbers = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(numbers))  
# Output: [1, 4, 16, 25, 49, 100]

# Time: O(n log n) - Iterates through n elements to square in O(n) time, followed by sorting the ans array in O(n log n) using Timsort.

# Space: O(n) - Uses a ans array of size n to store squared values, with O(log n) auxiliary space for Timsort’s sorting process.
