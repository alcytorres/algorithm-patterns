# ============================================================
# DSA COURSE TEMPLATES
# ============================================================

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

arr = ['a', 'b', 'c', 'd']
print(fn(arr))
# Output: abcd



# ====================================
# Fixed Sliding Window Template
# ====================================
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

# Ex: Largest Sum of Subarray with Fixed Length k
def find_best_subarray(nums, k):
    curr = 0    
    
    for i in range(k): 
        curr += nums[i]  
    
    ans = curr       
    
    # Slide window, maintaining size k
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]   
        ans = max(ans, curr) 
    
    return ans 

nums = [1, 4, 6, 2]
k = 2
print(find_best_subarray(nums, k))  
# Output: 10  →  Subarray [4, 6] (length 2, sum 4 + 6 = 10) is the largest sum for k=2.


# ====================================
# Dynamic Sliding Window Template
# ====================================
def fn(arr):
    left = curr = ans = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans
    
    return ans


# Ex: Longest Substring with At Most One "0"
def longest_substring_one_zero(s):
    left = curr = ans = 0        
        
    for right in range(len(s)): 
        if s[right] == "0":     
            curr += 1            
        
        while curr > 1:          
            if s[left] == "0":   
                curr -= 1        
            left += 1            
            
        ans = max(ans, right - left + 1)  
    
    return ans

s = "10101"
print(longest_substring_one_zero(s))
# Output: 3  →  Substring "101" (length 3) is the longest with at most one "0".



# ––––––––––––––––––––––––––––––––––––––––––––––
"""
🔥 Dynamic Sliding Window Templates (2 Types)
Use these for LeetCode substring/subarray problems (subarrays / substrings).

🎯 Core Rule:
    • Rule checks the WINDOW as a whole (sum, #distinct) → Add first, then shrink
    • Rule checks the NEW element (duplicates)          → Shrink first, then add
"""

# ========================================================
# 🧠 TYPE 1 — "Add First, Then Shrink"
# Use when the rule is about the WINDOW as a whole:
#   • sum ≤ K
#   • at most K distinct characters
#   • total count / total cost / total something
#
# Pattern:
#   1) Add arr[right] into the window
#   2) While the window breaks the rule → shrink from the left
#   3) Update the answer
#
# Example use cases:
#   • Longest subarray with sum ≤ K
# ========================================================

def sliding_window_add_first(arr, LIMIT):
    left = curr = ans = 0

    for right in range(len(arr)):
        # ✅ Step 1: Add current element to the window
        curr += arr[right]

        # 🚨 Step 2: Shrink while the WINDOW is invalid
        while curr > LIMIT:     # condition about the whole window
            curr -= arr[left]
            left += 1

        # ✅ Step 3: Update answer using current valid window
        ans = max(ans, right - left + 1)
    
    return ans


# ========================================================
# 🧩 TYPE 2 — "Shrink Before Add"
# Use when the rule is about the NEW ELEMENT:
#   • no duplicates allowed
#   • something about s[right] itself must be safe before entering
#
# Pattern:
#   1) While s[right] would break the rule → shrink from the left
#   2) Add s[right] into the window
#   3) Update the answer
#
# Example use case:
#   • Longest substring without repeating characters
# ========================================================

def sliding_window_shrink_before_add(s):
    seen = set()
    left = ans = 0

    for right in range(len(s)):
        # 🚨 Step 1: Shrink until s[right] can safely enter
        while s[right] in seen:     # condition about the new element
            seen.remove(s[left])
            left += 1

        # ✅ Step 2: Add current element (window is now valid)
        seen.add(s[right])

        # ✅ Step 3: Update answer using current valid window
        ans = max(ans, right - left + 1)
    
    return ans


"""
🎯 Sliding Window Rule of Thumb

• If the rule checks the WINDOW as a whole (sum, #distinct)
    ➜ Add first
    ➜ Then shrink if the window becomes invalid

• If the rule checks the NEW element (duplicates)
    ➜ Shrink first
    ➜ Then add the new element
"""



# ––––––––––––––––––––––––––––––––––––––––––––––
# Find number of subarrays that fit an exact criteria
from collections import defaultdict

def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans


# ––––––––––––––––––––––––––––––––––––––––––––––
# Linked list: fast and slow pointer
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next
    
    return ans


# ––––––––––––––––––––––––––––––––––––––––––––––
# Reversing a linked list

def fn(head):
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp 
        
    return prev

"""
Trick to remember:
  • In the while loop
  • Each line picks up where the last one left off
  • curr.next → prev → curr
"""


