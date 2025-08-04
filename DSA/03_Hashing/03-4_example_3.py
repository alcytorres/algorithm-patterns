# Numbers Without Adjacent Values

# Example 3: Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

# If a valid number x appears multiple times, you only need to include it in the answer once.

# Example:
# Input: nums = [2, 4, 6, 8]
# Output:       [2, 4, 6, 8]
# Explanation: For each x in nums, neither x+1 nor x-1 exists in nums (e.g., for x=2, 3 and 1 are absent; for x=4, 5 and 3 are absent). All numbers satisfy the condition, and duplicates are not an issue here.

def find_numbers(nums):
    seen = set(nums)  # {8, 2, 4, 6}
    ans = []
    for x in seen:
        if x+1 not in seen and x-1 not in seen:
            ans.append(x)
    return ans

l = [2, 4, 6, 8]
print(find_numbers(l))
# Output: [8, 2, 4, 6]

# Time: O(n)
# - Creating the set from nums: O(n).
# - Looping through 'seen': O(n) in the worst case.
# - Set lookups ('x+1 not in seen', 'x-1 not in seen') are O(1) on average.
# - Overall: O(n) time.

# Space: O(n)
# - Set 'seen' stores up to n elements: O(n) space.
# - List 'ans' can store up to n elements in the worst case: O(n) space.
# - A few variables (x) take O(1) space.
# - Overall: O(n) total space.



# Why do we use 'for x in seen'
    # To iterate over unique numbers in nums, ensuring each valid x is processed and added to the result only once, as required by the problem (duplicates are ignored).


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def find_numbers(nums):
    seen = set(nums)          # Convert array to set for O(1) lookups
    ans = []                  # Initialize empty result list
    for x in seen:            # Iterate over unique numbers in set
        if x+1 not in seen and x-1 not in seen:  # Check if x+1 and x-1 absent
            ans.append(x)     # Add x to result if condition met
    return ans                # Return list of numbers without adjacent values
