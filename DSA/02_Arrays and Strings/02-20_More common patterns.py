# Arrays and Strings O(n) string building

# O(n) String Building
# Strings are immutable, so adding chars one by one is slow (O(n) per add).
# Direct concatenation: Adding chars builds a new string each time, making it O(n²).
# Better way: Use a list to add chars (O(1) each) then join them (O(n)), total O(n).

# Direct Concatenation
def build_string_concat(s):
    result = ""
    for c in s:
        result += c
    return result
# - Time: O(n²) - Each concatenation copies the entire string, summing to n + (n-1) + ... + 1 = O(n²).
# - Space: O(n) - Stores the final string, O(n).

# List Method
def build_string_list(s):
    arr = []
    for c in s:
        arr.append(c)
    return "".join(arr)
    # return arr.join("")  # Note: arr.join() won't work, use "".join(arr)
# - Time: O(n) - Append is O(1), join is O(n), total O(n).
# - Space: O(n) - List stores characters, then joined, O(n).

# Example usage
s = "forest"
print("Concat:", build_string_concat(s))  # Output: forest
print("List:", build_string_list(s))      # Output: forest

# Subarrays/Substrings
# These are contiguous parts of arrays/strings (e.g., [1,2] from [1,2,3]).
# Use sliding window for problems with sum limits or length goals.
# Prefix sums help calculate multiple subarray sums fast.

# Subsequences
# Non-contiguous parts keeping order (e.g., [1,3] from [1,2,3]).
# Trickier, often use two pointers. More on this later with dynamic programming!

# Subsets
# Any group of elements, order doesn’t matter (e.g., [2,3] from [1,2,3]).
# Useful for backtracking. Can sort since order isn’t key.

# Closing Tip
# This is just the start! We’ll build on these ideas (like sliding windows with hash maps) later. Try the quiz next!


# Example 344. Reverse String
def reverseString(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s

s1 = ["h","e","l","l","o"]
print(reverseString(s1))   # Output: ["o","l","l","e","h"]

# Efficient String Reversal
def reverseStrings(s):
    # Optional: Build reversed string for output
    result = []
    for char in s:
        result.append(char)
    return "".join(result)
    
s2 = ["h","e","l","l","o"]
print(reverseStrings(s1))  # Output: olleh