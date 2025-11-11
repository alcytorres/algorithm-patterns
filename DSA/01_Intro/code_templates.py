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

"""
🔥 Dynamic Sliding Window Templates (2 Types)
Use these for LeetCode substring/subarray problems.

========================================================
🧠 TYPE 1 — "Add First, Then Shrink"
When to use:
- Condition is about counts, sums, distinct count ≤ K, etc.
- You add arr[right] first, then check if window breaks.
- Example: "Longest Subarray with Sum ≤ K" or "At most K distinct chars"

Why:
- Adding a new element may cause violation (sum > K, count > K)
- So you shrink AFTER adding.
"""

def sliding_window_add_first(arr):
    left = curr = ans = 0

    for right in range(len(arr)):
        # ✅ Step 1: Add current element
        curr += arr[right]

        # 🚨 Step 2: Shrink while window is invalid
        while curr > SOME_LIMIT:   # example condition
            curr -= arr[left]
            left += 1

        # ✅ Step 3: Update answer
        ans = max(ans, right - left + 1)
    
    return ans

"""
========================================================
🧩 TYPE 2 — "Shrink Before Add"
When to use:
- Condition is about uniqueness (no duplicates)
- You must ensure the element you add doesn't break the rule.
- Example: "Longest Substring Without Repeating Characters"

Why:
- Adding s[right] itself could break the rule.
- So you shrink BEFORE adding it.
"""

def sliding_window_shrink_before_add(s):
    seen = set()
    left = ans = 0

    for right in range(len(s)):
        # 🚨 Step 1: Shrink until s[right] can safely enter
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # ✅ Step 2: Add current element (now window is valid)
        seen.add(s[right])

        # ✅ Step 3: Update answer
        ans = max(ans, right - left + 1)
    
    return ans

s = "abbabcb"
print(sliding_window_shrink_before_add(s))  
# Output: 3 → "abc" is the Longest substring without repeats in "abbabcb".

"""
✅ Quick Summary:
- Use "Add First, Then Shrink" → when condition depends on totals/counts (e.g., sum > K, distinct > K)
- Use "Shrink Before Add" → when condition depends on current element validity (e.g., duplicates)
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





# ––––––––––––––––––––––––––––––––––––––––––––––




# ––––––––––––––––––––––––––––––––––––––––––––––
