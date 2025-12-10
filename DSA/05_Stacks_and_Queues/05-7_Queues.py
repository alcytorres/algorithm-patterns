# ===============================================
# My TOP PREFERENCES FOR GUIDES
# ===============================================
"""
My Preferences for my Guides:

- Structured, readable, and visually clear — with clear section headers (🧩, 📦, 💡, 🔁, etc.).

- Intuitive and beginner-friendly, written in plain English with simple analogies (like boxes or train cars).

- Formatted for scanning — tables, bullet points, and “mental picture” sections.

- Concise but complete — no jargon, no redundancy, every section should feel necessary and educational.

- Chronological and visual — you like seeing the flow of code execution (step-by-step or line-by-line).

- Repeat key takeaways at the end (like the TL;DR cheat sheet) for quick future review.

"""


"""
📘 Queue Basics (FIFO)

Queue = [front → back]

Enqueue → add to back
Dequeue → remove from front
"""

from collections import deque

queue = deque()         # []
queue.append(1)         # Enqueue → [1]
queue.append(2)         # Enqueue → [1, 2]
queue.append(3)         # Enqueue → [1, 2, 3]

print(queue.popleft())  # Dequeue → removes 1
print(queue)            # [2, 3]



"""
---
Q: What is the best way to build a queue in python?

    • from collections import deque

    • deque = the fast, correct way to do a queue.
    • Always use it when you need FIFO (First In, First Out).

    """




# ============================================================
# Queues Guide
# ============================================================

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4516/


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Queue Declaration: we will use deque from the collections module
from collections import deque


# If you want to initialize it with some initial values:
queue = deque([1, 2, 3])

# Enqueueing/adding elements:
queue.append(4)
queue.append(5)
# print(queue)  # deque([1, 2, 3, 4, 5])

# Dequeuing/removing elements:
queue.popleft() # 1
queue.popleft() # 2
# print(queue)  # deque([3, 4, 5])

# Check element at front of queue (next element to be removed)
queue[0] # 3

# Get size
len(queue) # 3


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Queue Example Run (Using deque)
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # deque([1, 2, 3])

while queue:
    print(queue.popleft())
    
if not queue:
    print("Queue is empty!")

# Output:
# 1
# 2
# 3
# Queue is empty!

print(queue)  # deque([]) 



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# BUILT-IN FUNCTION: 
deque()
# What it does: Double-ended queue with O(1) append/pop from both ends.
# Why use it: Fast stack, queue, or sliding window operations.
# How it works: Linked list of blocks; O(1) left/right access.
# When to use: BFS, sliding window, monotonic queue, LRU cache.
# Time/Space: O(1) per operation, O(n) space.

# Syntax:
from collections import deque
deque(iterable)  # Creates deque from iterable

# Basic Example 1 (From List):
from collections import deque
d = deque([1, 2, 3])
print(d)  # Output: deque([1, 2, 3])

# Basic Example 2 (Empty):
from collections import deque
d = deque()
print(d)  # Output: deque([])

# Basic Example 3 (String):
from collections import deque
d = deque("abc")
print(d)  # Output: deque(['a', 'b', 'c'])

# DSA Example (Sliding Window):
from collections import deque
window = deque()
for i in range(3):
    window.append(i)
print(window)     # Output: deque([0, 1, 2])
window.popleft()  # Remove oldest
print(window)     # Output: deque([1, 2])


# DEQUE METHOD: .
append()
# What it does: Adds element to right end.
# Why use it: O(1) push to end.
# How it works: Appends to right.
# When to use: Stack push, queue enqueue.

# Syntax:
deque.append(item)

# Example:
d = deque()
d.append(1)
d.append(2)
print(d)  # Output: deque([1, 2])


# DEQUE METHOD: 
.appendleft()
# What it does: Adds element to left end.
# Why use it: O(1) push to front.
# How it works: Inserts at start.
# When to use: Monotonic queue, BFS.

# Syntax:
deque.appendleft(item)

# Example:
d = deque([2])
d.appendleft(1)
print(d)  # Output: deque([1, 2])


# DEQUE METHOD: 
.pop()
# What it does: Removes and returns rightmost element.
# Why use it: O(1) pop from end.
# How it works: Removes from right.
# When to use: Stack pop.

# Syntax:
deque.pop()

# Example:
d = deque([1, 2])
print(d.pop())  # Output: 2
print(d)        # Output: deque([1])


# DEQUE METHOD: 
.popleft()
# What it does: Removes and returns leftmost element.
# Why use it: O(1) pop from front.
# How it works: Removes from left.
# When to use: Queue dequeue, sliding window.

# Syntax:
deque.popleft()

# Example:
d = deque([1, 2])
print(d.popleft())  # Output: 1
print(d)            # Output: deque([2])
