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
        key = ''.join(sorted(s))  
        buckets[key].append(s)

    return list(buckets.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


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
Overview for Each Iteration
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Step: Group anagrams by sorted string key
s     | key | buckets
-     | -   | {}
eat   | aet | {aet: [eat]}
tea   | aet | {aet: [eat, tea]}
tan   | ant | {aet: [eat, tea], ant: [tan]}
ate   | aet | {aet: [eat, tea, ate], ant: [tan]}
nat   | ant | {aet: [eat, tea, ate], ant: [tan, nat]}
bat   | abt | {aet: [eat, tea, ate], ant: [tan, nat], abt: [bat]}
Final: [[bat], [tan, nat], [eat, tea, ate]]


Step-by-Step Walkthrough:
For strs = ["eat", "tea", "tan", "ate", "nat", "bat"]:
  • Start: buckets = {} (empty notebook).

  • Process each word:
    "eat": sorted("eat") = ['a', 'e', 't'], ''.join(['a', 'e', 't']) = "aet", buckets["aet"] = ["eat"].
    "tea": sorted("tea") = ['a', 'e', 't'], ''.join(['a', 'e', 't']) = "aet", buckets["aet"] = ["eat", "tea"].
    "tan": sorted("tan") = ['a', 'n', 't'], ''.join(['a', 'n', 't']) = "ant", buckets["ant"] = ["tan"].
    "ate": sorted("ate") = ['a', 'e', 't'], ''.join(['a', 'e', 't']) = "aet", buckets["aet"] = ["eat", "tea", "ate"].
    "nat": sorted("nat") = ['a', 'n', 't'], ''.join(['a', 'n', 't']) = "ant", buckets["ant"] = ["tan", "nat"].
    "bat": sorted("bat") = ['a', 'b', 't'], ''.join(['a', 'b', 't']) = "abt", buckets["abt"] = ["bat"].

Return: list(buckets.values()) = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].



Most IMPORTANT thing to Understand:
    • Anagrams become the same string when their letters are sorted.  

    • We can use this sorted version as a "key" to group words that belong together.  

    • The dictionary groups all words that share the same sorted key.  

Why this code Works:
    • Hash map (buckets): key = sorted word, value = list of words with that key.  

    • Sorting step: ensures all anagrams collapse to the same key.  

    • Efficiency: O(n * k log k) because each of n words of length k is sorted once. Far faster than comparing every pair (O(n^2)).  

    Intuition: If two words look the same after sorting their letters, they must be anagrams → group them together.

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

    

Q: Why defaultdict(list)?
    • defaultdict(list) gives [] for new keys (good for grouping)
        • defaultdict(int) gives 0 for new keys (good for counting)
    • Here it means we can always do buckets[key].append(word) without checking if the key exists first

    
Q: Why sort the string to make the key?
    • Because sorting makes all anagrams look identical
    • "eat", "tea", "ate" all become "aet". 
    • This guarantees that anagrams collapse into the same dictionary bucket.

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

from collections import defaultdict

def groupAnagrams(strs):
    buckets = defaultdict(list)    # Notebook to group anagrams

    for s in strs:                 # Go through each word in the list
        key = ''.join(sorted(s))   # Sort the letters and join them back into a string so anagrams (same letters, different order) share the same key
        buckets[key].append(s)     # Add the original word into the correct group (bucket)

    return list(buckets.values())  # Return just the grouped words (ignore the keys)



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

# Sorted
s = "bat"
print(sorted(s))
# ['a', 'b', 't']

s = ['c', 'b', 'a']
print(sorted(s))
# Output: ['a', 'b', 'c']

s = [3, 2, 1]
print(sorted(s))
# Output: [1, 2, 3]


# .join
# Example 1: Joining words with a space separator
def fn(words):
    return " ".join(words)

words = ["Hello", "world", "from", "Python"]
print(fn(words))  # Output: Hello world from Python


# Example 2: Joining characters with no separator
def fn(c):
    return "".join(c)

c = ["P", "y", "t", "h", "o", "n"]
print(fn(c))  # Output: Python

