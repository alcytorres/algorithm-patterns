







"""
============================
ARRAYS vs LINKED LISTS — Simple Guide
============================

Arrays and linked lists both store collections of data,
but they work *very differently* under the hood.
"""

# ----------------------------
# 🧠 ARRAY (Contiguous Memory)
# ----------------------------

"""
When you make an array:

    arr = [1, 2, 3]

Under the hood, the computer stores these values *back-to-back* in memory.

Each element sits right next to the previous one, with no gaps.

Example layout in memory:

Address →   100   104   108
Value   →   [1]   [2]   [3]

If each element takes 4 bytes, the next starts exactly 4 bytes later.

✅ Why this matters:
  • Because everything is evenly spaced, the computer can instantly jump to any position using simple math.

For example, to find the 3rd element arr[2]:
  • start_address + (2 * element_size)
    = 100 + (2 * 4)
    = 108

    ✅ arr[2] lives at address 108.
  • You don't have to count through all items — you just jump there directly using math:
  → This makes lookup by index very fast — constant time O(1).
"""


# ----------------------------
# 🔗 LINKED LIST (Scattered Memory)
# ----------------------------

"""
In a linked list, elements (called nodes) are NOT stored next to each other.
Each node contains:
  - data  (the actual value)
  - next  (a pointer: the memory address of the next node)

Example layout in memory:

    Node A (at 500):
    data: 1
    next: 720  → (points to Node B)

    Node B (at 720):
    data: 2
    next: 305  → (points to Node C)

    Node C (at 305):
    data: 3
    next: None (end)

💡 Notice: the nodes live at random addresses — 500, 720, 305.
    • They're scattered. You only find the next node by following pointers.
"""


# ----------------------------
# ⚙️ Traversal Example (Python-like)
# ----------------------------

"""
Here's a simple linked list chain in Python form:
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # will store reference to next Node

# Build a small linked list: 1 → 2 → 3
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

# Traversing requires following pointers one by one
curr = a
while curr:
    print(curr.data)
    curr = curr.next

"""
Output:
1
2
3

We can't “jump” to the 3rd element directly — we must walk through 1, then 2, then 3.
"""


# ----------------------------
# ⚡️ Big-O Comparison (Simple Intuition)
# ----------------------------

"""
✅ ARRAYS — Fast Random Access (O(1))
------------------------------------
Think of an array like a street of evenly spaced houses.
If you want house #3, you just calculate:
    start + (3 * house_width)
and jump straight there — instant access.

That's why indexing (arr[2]) is O(1).

But inserting or deleting in the middle of an array is slow (O(n)),because you may have to shift everything over to keep them in order.


✅ LINKED LISTS — Flexible for Insert/Remove (O(1) in some cases)
----------------------------------------------------------------
Think of a linked list like a treasure map:
  • Each node gives you directions to the next one.
  • They can live anywhere — not evenly spaced.

This makes insertion and deletion easier:
  • If you already know where you are, you just change a pointer.
  • You don't need to move anything else — no shifting required.

Example:
To insert “4” after node B:
    new_node.next = B.next
    B.next = new_node
Done — O(1).

But random access (like “give me the 5th node”) is slow (O(n)),
because you must start at the beginning and follow every pointer step by step.


✅ Summary:
-----------
  • Arrays → Great for fast lookups, poor for frequent insertions/removals.
  • Linked Lists → Great for flexible insertion/removal, slow for random access.
"""


# ----------------------------
# TL;DR VISUAL SUMMARY
# ----------------------------

"""
ARRAY (contiguous memory):
| 1 | 2 | 3 | → instant jumps by index (O(1))

LINKED LIST (scattered memory):
[1] → [2] → [3]
   ↳ must follow one by one (O(n))
"""

