"""
Task: Given a string, find the length of the longest substring without any repeating characters.
Example 1: s = "abcabccc" → Output = 3 (substring "abc")
"""
def lengthOfLongestSubstring(s):    
    # 1️⃣ Initialize pointers & tracking variables
    left = 0
    longest_substring = 0
    sett = set()
    n = len(s)
    
    # 2️⃣ Expand window by moving `right` & update conditions
    for right in range(n):

        # 3️⃣ Shrink window when condition is violated
        while s[right] in sett:
            sett.remove(s[left])
            left += 1

        # 4️⃣ Update result with current window
        current_longest_substring = (right - left) + 1
        longest_substring = max(longest_substring, current_longest_substring)
        sett.add(s[right])
     
    # 5️⃣ Return final result
    return longest_substring

print(lengthOfLongestSubstring("abcabccc"))    # Output: 3



# def lengthOfLongestSubstring(s):
    
#     # 1️⃣ Initialize pointers & tracking variables
#     left = 0
#     longest_substring = 0
#     sett = set()
#     n = len(s)
    
#     # 2️⃣ Expand window by moving `right` & update conditions
#     for right in range(n):

#         # 3️⃣ Shrink window when condition is violated
#         while s[right] in sett:
#             sett.remove(s[left])
#             left += 1
     
#         # 4️⃣ Update result with current window
#         current_longest_substring = (right - left) + 1
#         longest_substring = max(longest_substring, current_longest_substring)
#         sett.add(s[right])
     
#     # 5️⃣ Return final result
#     return longest_substring
 

# print(lengthOfLongestSubstring("abcabccc"))    # Output: 3