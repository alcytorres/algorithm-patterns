# Two pointers: one input, opposite ends

def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return ans


# ––––––––––––––––––––––––––––––––––––––––––––––
# Two pointers: two inputs, exhaust both

def fn(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if CONDITION:
            i += 1
        else:
            j += 1
    
    while i < len(arr1):
        # do logic
        i += 1
    
    while j < len(arr2):
        # do logic
        j += 1
    
    return ans


# ––––––––––––––––––––––––––––––––––––––––––––––
# Dynamic Sliding Window Template
def fn(arr):
    left = curr = ans = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans
    
    return ans

# ––––––––––––––––––––––––––––––––––––––––––––––
# Fixed Sliding Window Template
def fn(arr, k):
    curr = 0

    # Build first window
    for i in range(k):
        # Add arr[i] to curr
        pass

    ans = curr  # Compute initial result for first window

    # Slide window
    for i in range(k, len(arr)):
        # Update curr: add arr[i], remove arr[i-k]
        pass
        # Update ans
        pass

    return ans

# ––––––––––––––––––––––––––––––––––––––––––––––
# Build a prefix sum Template 1
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix

arr = [1, 2, 3, 4, 5]  # [1, 3, 6, 10, 15]
print(fn(arr))


# Build a prefix sum Template 2
def fn(arr):
    prefix = [arr[0]]
    curr = arr[0]    
    
    for i in range(1, len(arr)):  
        curr += arr[i]
        prefix.append(curr)
    
    return prefix

arr = [1, 2, 3, 4, 5]  # [1, 3, 6, 10, 15]
print(fn(arr))


# ––––––––––––––––––––––––––––––––––––––––––––––
# Efficient string building
# arr is a list of characters
def fn(arr):
    ans = []
    for c in arr:
        ans.append(c)
    
    return "".join(ans)

print(fn(['a', 'b', 'c', 'd']))
# Output: abcd



# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Quick Tutorial: defaultdict(list)

defaultdict(list) is a dictionary that automatically creates
an empty list [] for any missing key.

Main use case: grouping items by a key.

Example: Group words by their first letter.
"""

from collections import defaultdict

# Create defaultdict where each value starts as []
groups = defaultdict(list)

words = ["apple", "ant", "banana", "bat", "car"]

for w in words:
    key = w[0]            # key = first letter
    groups[key].append(w) # no need to check if key exists

print(groups)
# Output:
# defaultdict(<class 'list'>,
#   {'a': ['apple', 'ant'], 'b': ['banana', 'bat'], 'c': ['car']})



# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Quick Tutorial: collections.Counter

Counter is a dictionary subclass for counting hashable objects.
It automatically tallies how many times each item appears.

Main use case: counting characters, words, or elements.
"""

from collections import Counter

# Example: Count letters in a word
word = "mississippi"
letter_counts = Counter(word)

print(letter_counts)
# Output:
# Counter({'i':4, 's':4, 'p':2, 'm':1})

# Example: Count words in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)

print(word_counts)
# Output:
# Counter({'apple':3, 'banana':2, 'orange':1})


# ––––––––––––––––––––––––––––––––––––––––––––––



# ––––––––––––––––––––––––––––––––––––––––––––––



# ––––––––––––––––––––––––––––––––––––––––––––––