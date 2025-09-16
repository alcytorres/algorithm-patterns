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

# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Soltuion: Using ''.join(sorted(s)) as key

from collections import defaultdict

def groupAnagrams(strs):
    buckets = defaultdict(list) 

    for s in strs:
        key = ''.join(sorted(s))   # canonical form
        buckets[key].append(s)

    return list(buckets.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



# from collections import defaultdict

# def groupAnagrams(strs):
#     groups = defaultdict(list)  # Notebook to group anagrams

#     for s in strs:
#         sorted_s = ''.join(sorted(s))  
#         groups[sorted_s].append(s)     

#     return list(groups.values())       


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(strs))



# Time: O(n * k log k)
# - For each of the n strings, sort it (O(k log k), where k = average length of a string).
# - Appending to the dictionary groups is O(1).
# - Overall: O(n * k log k) time.

# Space: O(n * k)
# - Dictionary 'buckets' stores up to n strings, grouped by their sorted key.
# - Each string (length k) is stored once in the dictionary lists → O(n * k) space.
# - A few variables (s, key) take O(1) space.
# - Overall: O(n * k) space.


"""
# Overview for Each Iteration
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Step: Group anagrams by sorted string key
# s     | key | buckets
# -     | -   | {}
# eat   | aet | {aet: [eat]}
# tea   | aet | {aet: [eat, tea]}
# tan   | ant | {aet: [eat, tea], ant: [tan]}
# ate   | aet | {aet: [eat, tea, ate], ant: [tan]}
# nat   | ant | {aet: [eat, tea, ate], ant: [tan, nat]}
# bat   | abt | {aet: [eat, tea, ate], ant: [tan, nat], abt: [bat]}
# Final: [[bat], [tan, nat], [eat, tea, ate]]



Most IMPORTANT thing to Understand:
    • Anagrams become the same string when their letters are sorted.  

    • We can use this sorted version as a "key" to group words that belong together.  

    • The dictionary groups all words that share the same sorted key.  

Why this code Works:
    • Hash map (buckets): key = sorted word, value = list of words with that key.  

    • Sorting step: ensures all anagrams collapse to the same key.  

    • Efficiency: O(n * k log k) because each of n words of length k is sorted once. Far faster than comparing every pair (O(n^2)).  

    • Intuition: Like sorting letters in names — if two names look identical after sorting, they're anagrams, so they go in the same bucket.  

TLDR:
    • Sort each word to create a key, then group words with the same key together.  

Quick Example Walkthrough:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]  

    Step 1: Process each word  
        • "eat" → "aet" → groups = {"aet": ["eat"]}  
        • "tea" → "aet" → groups = {"aet": ["eat", "tea"]}  
        • "tan" → "ant" → groups = {"aet": ["eat","tea"], "ant":["tan"]}  
        • "ate" → "aet" → groups = {"aet": ["eat","tea","ate"], "ant":["tan"]}  
        • "nat" → "ant" → groups = {"aet": ["eat","tea","ate"], "ant":["tan","nat"]}  
        • "bat" → "abt" → groups = {"aet": [...], "ant":[...], "abt":["bat"]}  

    Step 2: Collect grouped lists  
        [["bat"], ["tan","nat"], ["eat","tea","ate"]]  

    Final Answer: [["bat"], ["tan","nat"], ["eat","tea","ate"]]  

    


Why defaultdict(list)?






"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)    # Notebook to group anagrams

    for s in strs:
        key = ''.join(sorted(s))  # Sort letters to make key
        groups[key].append(s)     # Add string to its group

    return list(groups.values())       # Return all groups



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 








# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Solutions


# Using character counts as key
    # This is the MOST efficient solution

import collections

def groupAnagrams(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)

    return list(ans.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# Time: O(n * k)
# - For each string of length k, build a 26-length count array in O(k).
# - Using this tuple of counts as the dictionary key is O(1).
# - Overall: O(n * k) time (faster than sorting).

# Space: O(n * k)
# - Dictionary stores up to n strings in grouped lists.
# - Each string of length k is stored once → O(n * k).
# - Keys are 26-length tuples (constant size), so O(n) extra.
# - Overall: O(n * k) space.



# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Solution: Using tuple(sorted(s)) as key

import collections

def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    
    for s in strs:
        ans[tuple(sorted(s))].append(s)

    return list(ans.values())
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# Time: O(n * k log k)
# - For each of the n strings, sort it (O(k log k), where k = average string length).
# - Dictionary insert/append is O(1).
# - Overall: O(n * k log k) time.

# Space: O(n * k)
# - Dictionary stores up to n strings in grouped lists.
# - Each string of length k is stored once → O(n * k).
# - Keys are sorted tuples of length k, but reused, so O(n * k) dominates.
# - Overall: O(n * k) space.



# –––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground

s = "bat"
print(sorted(s))
# ['a', 'b', 't']

s = ['c', 'b', 'a']
print(sorted(s))
# Output: ['a', 'b', 'c']

s = [3, 2, 1]
print(sorted(s))
# Output: [1, 2, 3]