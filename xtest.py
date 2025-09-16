# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
    # Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]

# Explanation:
    # There is no string in strs that can be rearranged to form "bat".
    # The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    # The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Solution: https://leetcode.com/problems/group-anagrams/description/


from collections import defaultdict

def groupAnagrams(strs):
    buckets = defaultdict(list)

    for s in strs:
        key = " ".join(sorted(s))
        buckets[key].append(s)
    
    return list(buckets.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# buckets = {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
