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










# ============================================================
# MY GUIDES
# ============================================================

# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Tutorial: defaultdict(list)

defaultdict(list) is a dictionary that automatically creates an empty list [] for any missing key.

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
📘 Tutorial: collections.Counter

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
"""
📘 Tutorial: True = 1 and False = 0 in Python

- In Python, booleans are a subclass of integers.
- True behaves like 1, False behaves like 0.
"""

# Example:
print(True + True)    # 2
print(False + True)   # 1
print(3 * True)       # 3
print(3 * False)      # 0




# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Tutorial: sum(condition for x in items)

- You can use sum() with a generator expression to count matches.

- Each condition produces True (1) or False (0).

- sum() adds them up → count of items where condition is True.
"""

# Example: condition for x in items:
nums = [1, 2, 3, 4]
evens = sum(x % 2 == 0 for x in nums)
print(evens)   # Output 2 (since 2 and 4 are even)


# Example: condition for x in items:
def fn(nums):
    return sum(num % 2 == 0 for num in nums)

nums = [1, 2, 3, 4]
print(fn(nums))   # Output 2 (since 2 and 4 are even)




# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Tutorial: @staticmethod in Python

- A @staticmethod is just a normal function stored inside a class.
- It does NOT get 'self' automatically.
- You can call it from the class OR from an instance.
- Key idea: instance calls would break without @staticmethod
  because Python would try to pass the instance as 'self'.
"""

# Example 1: Dog class
class Dog:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def bark_times(n):
        print("Woof! " * n)

d1 = Dog(3)

print(d1.bark_times(3))   # Instance call
# Without @staticmethod this breaks:
# Python would secretly do: Dog.bark_times(d1, 3)
# 'd1' becomes self → too many arguments → error


# Works both ways:
Dog.bark_times(3)         # Class call


"""
Without @staticmethod:
    • d1.bark_times(3) becomes Dog.bark_times(d1, 3)
    • That means 2 arguments get sent in
    • But the method only expects (n)
    • → TypeError

With @staticmethod:
    • Python does NOT pass 'self'
    • d1.bark_times(3) just passes (3)
    • Works from instance OR class
    • Acts like a normal function stored inside a class
"""


# Example 2: Math class
class Math:

    @staticmethod
    def add(a, b):
        return a + b

m1 = Math()
print(m1.add(1, 2))     # Instance call
# Without @staticmethod this breaks:
# Python would secretly do: Math.add(m1, 1, 2)
# That extra 'm1' becomes self → too many arguments → error


# Works both ways:
print(Math.add(1, 2))   # Class call


"""
Without @staticmethod:
    • Calling m1.add(1, 2) secretly becomes Math.add(m1, 1, 2)
    • That means 3 arguments get sent in
    • But the function only expects (a, b)
    • → TypeError

With @staticmethod:
    • Python does NOT pass 'self'
    • m1.add(1, 2) just passes (1, 2)
    • Works from instance OR class
    • Acts like a normal function stored inside a class

"""




# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Tutorial: When to Use `continue` in LeetCode

  • `continue` skips the *rest of the loop* and jumps to the next item.

  • Use it when you want to ignore certain cases early and keep your logic clean.

  • Great for filtering: skip blanks, skip invalid input, skip no-op values.
"""

# Example 1: Skip negative numbers
nums = [-1, 2, -3, 4]
result = []
for n in nums:
    if n < 0:
        continue      # skip negatives
    result.append(n)
print(result)  # Output: [2, 4]


# Example 2: Skip empty strings
words = ["hi", "", "code", ""]
clean = []
for w in words:
    if w == "":
        continue      # skip blanks
    clean.append(w)
print(clean)  # Output: ["hi", "code"]


# Example 3: Skip '.' and '' in Simplify Path
def simplifyPath(path):
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue    # skip meaningless parts
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)

print(simplifyPath("/a/./b//c/../"))  # Output: "/a/b"



# ––––––––––––––––––––––––––––––––––––––––––––––
"""
Tutorial: .split() + .join() in LeetCode

  - .split() turns string into list of parts
  - .join() turns list back into string with separator
  
  - Use together to clean, reorder, or rebuild strings
"""

# Example 1: Reverse Words
def reverse_words(s):
    words = s.split()           # → ['sky', 'is', 'blue']
    words.reverse()             # → ['blue', 'is', 'sky']
    return " ".join(words)      # → "blue is sky"

print(reverse_words("sky is blue"))


# Example 2: Remove Extra Spaces
def clean_spaces(s):
    words = s.split()           # → ['hello', 'world'] (removes extra spaces)
    return " ".join(words)      # → "hello world"

print(clean_spaces("  hello   world  "))


# Example 3: Build Path from string
def build_path(s):
    parts = s.split("/")           # → ['', 'home', 'user', 'docs']
    parts = [p for p in parts if p]  # remove empty
    return "/" + "/".join(parts)

print(build_path("/home/user/docs/"))  # "/home/user/docs"


# Example 3: Build Path from string (no list comprehension)
def build_path(s):
    parts = s.split("/")           # ['', 'home', 'user', 'docs']
    stack = []
    for p in parts:
        if p:                      # skip empty strings
            stack.append(p)
    return "/" + "/".join(stack)

print(build_path("/home/user/docs/"))  # "/home/user/docs"



# ––––––––––––––––––––––––––––––––––––––––––––––
"""
GUIDE: float('inf') AND float('-inf')
----------------------------------------------

WHAT IS float('inf')?
    • Python's version of +∞ (positive infinity).
    • Larger than any real number.
    • Best starting value when you want to track the **minimum**.

WHAT IS float('-inf')?
    • Python;s version of -∞ (negative infinity).
    • Smaller than any real number.
    • Best starting value when you want to track the **maximum**.

WHY THIS MATTERS IN LEETCODE:
    • You often scan through a list and want to keep updating a “best so far.”
    • Using ±∞ ensures the very first element replaces your starting value.
    • Cleaner and safer than manually using the first element of the array.

MOST COMMON USE CASES (Beginner Level)
    1) Tracking a MIN value  ← MOST COMMON for float('inf')
         - Stock problems (best buy price)
         - Running minimum in number arrays

    2) Tracking a MAX value  ← MOST COMMON for float('-inf')
         - Max subarray variations
         - Running maximum in arrays

ANALOGY:
    • Tracking MIN: start with “infinite price” so the first real price is always better.
    • Tracking MAX: start with “lowest possible number” so the first real number is bigger.

CHEAT CODE:
    • Need MIN → float('inf')
    • Need MAX → float('-inf')
"""

# --------------------------------------------------------
# Example 1 (MOST COMMON): Track running minimum
# --------------------------------------------------------
def min_element(nums):
    m = float('inf')          # Start absurdly high
    for n in nums:
        if n < m:
            m = n
    return m

print(min_element([4, 2, 9, -1, 6]))  # → -1

# --------------------------------------------------------
# Example 2 (2nd most common): Track running maximum
# --------------------------------------------------------
def max_element(nums):
    m = float('-inf')         # Start absurdly low
    for n in nums:
        if n > m:
            m = n
    return m

print(max_element([4, 2, 9, -1, 6]))  # → 9

# --------------------------------------------------------
# Example 3 (very common beginner pattern): Stock problem
# --------------------------------------------------------
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # → 5



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
            square = nums[r]
            r -= 1
        else:
            square = nums[l]
            l += 1

        # place square in correct sorted position
        ans[i] = square * square

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




# ––––––––––––––––––––––––––––––––––––––––––––––




# ––––––––––––––––––––––––––––––––––––––––––––––













# ============================================================
# 📘 Algorithm Tools You Should Know
        # Keep adding to the Algorithm Tools You Should Know
# ============================================================

"""
These are universal DSA mini-tools that clean up solutions and reduce bugs.
They're not tied to Python syntax — they're patterns that make solutions cleaner.
"""

# ------------------------------------------------------------
# 1) Sentinel Values (float('inf'), float('-inf'))
"""
For tracking running MIN/MAX without special cases.

• Need MIN → float('inf')
• Need MAX → float('-inf')
"""

def track_min(nums):
    m = float('inf')
    for x in nums:
        if x < m:
            m = x
    return m

def track_max(nums):
    m = float('-inf')
    for x in nums:
        if x > m:
            m = x
    return m

# ------------------------------------------------------------
# 2) Early-Exit Conditions (“guard clauses”)
"""
Ends function early instead of nesting logic.
Keeps code cleaner and avoids unnecessary work.
"""

def safe_divide(a, b):
    if b == 0:       # early exit if invalid
        return None
    return a / b

print(safe_divide(10, 2))  # → 5
print(safe_divide(10, 0))  # → None


# ------------------------------------------------------------
# 3) Counting With Booleans (sum(condition))
"""
True = 1, False = 0 → lets you count matches with zero extra code.
"""

def count_evens(nums):
    return sum(x % 2 == 0 for x in nums)

print(count_evens([1, 2, 3, 4]))  # → 2


# ------------------------------------------------------------
# 4) Using Sets for O(1) Lookup
"""
Use sets anytime the question is:
    “Is x in the list?”
List check → O(N)
Set check → O(1)
"""

def check_membership(nums, targets):
    nums_set = set(nums)
    return [t in nums_set for t in targets]

print(check_membership([3, 7, 9], [7, 2, 9]))  
# → [True, False, True]






























# ============================================================
# DELETE THIS: IT has A LOT OF things I DO NOT NEED to KNOW
# ============================================================
"""
🔥 LeetCode Python Patterns — Ranked (most useful → least)
"""

# 0) CORE LOOPS + ITERATION BASICS
# --------------------------------
# range(n): range object; list(range(5)) -> [0,1,2,3,4]
# len(lst): number of items
# enumerate(lst): (index, item) pairs
for i in range(len(a)): ...
for i, x in enumerate(a): ...
for x in a: ...


# 1) HASH SET / HASH MAP (presence + counting)
# --------------------------------------------
from collections import defaultdict, Counter

seen = set();  seen.add(x);  if y in seen: ...
freq = defaultdict(int)
for x in nums: freq[x] += 1
cnt = Counter(nums);  cnt['a']  # frequency


# 2) SLIDING WINDOW (Two Pointers on string/array)
# ------------------------------------------------
def longest_no_repeat(s):
    seen = set(); left = 0; best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left]); left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best


# Count condition in window (>= K distinct, etc.)
from collections import defaultdict
def at_most_k_distinct(nums, K):
    count = defaultdict(int); left = 0; res = 0
    for right, x in enumerate(nums):
        count[x] += 1
        while len(count) > K:
            count[nums[left]] -= 1
            if count[nums[left]] == 0: del count[nums[left]]
            left += 1
        res += right - left + 1
    return res


# 3) TWO POINTERS (sorted arrays / linked lists)
# ----------------------------------------------
i = j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]: i += 1
    elif A[i] > B[j]: j += 1
    else:  # equal
        i += 1; j += 1


# 4) PREFIX SUM / DIFF ARR / RUNNING COUNT
# ----------------------------------------
pref = [0]
for x in nums: pref.append(pref[-1] + x)  # prefix sum
# Subarray sum(i..j) = pref[j+1] - pref[i]

# Running balance example
first = {0: -1}; bal = 0; best = 0
for i, x in enumerate(nums):
    bal += 1 if x == 1 else -1
    if bal in first: best = max(best, i - first[bal])
    else: first[bal] = i


# 5) STACK PATTERNS (monotonic, parentheses)
# ------------------------------------------
# Valid parentheses
stack = []
pairs = {')':'(', ']':'[', '}':'{'}
for c in s:
    if c in '([{': stack.append(c)
    elif not stack or stack.pop() != pairs[c]: 
        return False
    return not stack

# Monotonic stack (next greater)
res = [-1]*len(nums); st = []
for i, x in enumerate(nums):
    while st and nums[st[-1]] < x:
        res[st.pop()] = x
    st.append(i)


# 6) BINARY SEARCH (bisect)
# --------------------------
import bisect
i = bisect.bisect_left(a, x)
j = bisect.bisect_right(a, x)

# Search answer space
lo, hi = 0, 10**9
while lo < hi:
    mid = (lo + hi)//2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1


# 7) SORTING & CUSTOM KEYS
# -------------------------
arr.sort(key=lambda t: (t[0], -t[1]))


# 8) HEAP (Top-K, K-way merge)
# ----------------------------
import heapq
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > K: heapq.heappop(heap)


# 9) COMPREHENSIONS + ANY/ALL + SUM(conditions)
# ----------------------------------------------
# Collect
evens = [x for x in nums if x % 2 == 0]
# Transform
squares = [x*x for x in nums]
# Count matches
even_count = sum(x % 2 == 0 for x in nums)
# Existence / universal checks
has_dup = any(freq[x] > 1 for x in freq)
all_pos  = all(x > 0 for x in nums)


# 10) SET OPS (intersection/union/diff)
# -------------------------------------
A, B = set(a), set(b)
both = A & B; either = A | B; onlyA = A - B


# 11) MATRIX TRAVERSAL (grid)
# ---------------------------
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
for r in range(R):
    for c in range(C):
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                ...


# 12) DEQUE (sliding window max, BFS)
# -----------------------------------
from collections import deque
dq = deque()
for i, x in enumerate(nums):
    while dq and nums[dq[-1]] <= x: dq.pop()
    dq.append(i)
    if dq[0] <= i - k: dq.popleft()
    if i >= k-1: window_max = nums[dq[0]]

# BFS queue
q = deque([start])
visited = {start}
while q:
    u = q.popleft()
    for v in graph[u]:
        if v not in visited:
            visited.add(v); q.append(v)


# 13) DICT TRICKS: get / setdefault
# ---------------------------------
d = {}
d[x] = d.get(x, 0) + 1
adj = {}
adj.setdefault(u, []).append(v)


# 14) EDGE-SAFE LIST INIT + COPY
# ------------------------------
grid = [[0]*C for _ in range(R)]  # avoid shared rows
b = a[:]  # shallow copy
import copy; deep = copy.deepcopy(obj)


# 15) SMALL BUT CLUTCH
# --------------------
mx = max(arr, default=float('-inf'))
mn = min(arr, default=float('inf'))

pairs = sorted(pairs)  # tuples sort lexicographically

for x in arr:
    if bad(x): break
else:
    # no break occurred
    pass


"""
Mini Cheats you asked about
---------------------------
- Counting with sum:
  sum(cond(x) for x in items)

- Collecting with list-comprehension:
  [x for x in items if cond(x)]

- Basics you listed:
  print(range(5))              # range(0,5)
  print(list(range(5)))        # [0,1,2,3,4]
  print(len(grocery_list))     # size
  for i, item in enumerate(grocery_list): ...
  [0]*5                        # list repeat
  [1,2] + [5,4,7]              # concat
"""

