# 771. Jewels and Stones

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Solution: https://leetcode.com/problems/jewels-and-stones/solutions/127766/jewels-and-stones/

# Example 1:
    # Input: jewels = "aA", stones = "aAAbbbb"
    # Output: 3

# Example 2:
    # Input: jewels = "z", stones = "ZZ"
    # Output: 0

# Constraints:
    # 1 <= jewels.length, stones.length <= 50
    # jewels and stones consist of only English letters.
    # All the characters of jewels are unique.






# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 

def numJewelsInStones(J, S):
    return sum(s in J for s in S)


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3

# Time Complexity: O(J.length∗S.length))
# Space Complexity: O(1) 




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solutions

# Hash Set 

def numJewelsInStones(J, S):
    Jset = set(J)
    return sum(s in Jset for s in S)


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3


# Time Complexity: O(J.length+S.length). The O(J.length) part comes from creating J. The O(S.length) part comes from searching S.

# Space Complexity: O(J.length)