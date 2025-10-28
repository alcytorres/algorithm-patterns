"""
🚨 LINKED LIST CODE RED 🚨
Always DRAW the linked list with pen and paper before coding.

For each iteration, sketch:
    1. What the list looks like before the change.
    2. Which nodes (prev, curr, next) the pointers refer to.
    3. What should happen after the current operation.

    This helps you *see* pointer movement, avoid confusion, and debug logically.


Loop Conditions
    • Use while fast: when checking if fast reaches the end (None), e.g., finding the kth node from the end.

    • Use while fast and fast.next: when accessing fast.next.next (e.g., middle node), to ensure both are non-None and avoid errors.

"""


"""
===========================================
FAST & SLOW POINTERS — Simple, Scan-Friendly Guide
===========================================

Fast & slow pointers are a flavor of the two-pointers technique.
Instead of moving together, the pointers move differently (e.g., different speeds).
This often turns multi-pass problems into elegant one-pass O(N), O(1)-space solutions.
"""


# ----------------------------
# 🧩 Core Pattern (Pseudocode)
# ----------------------------
"""
// head is the head node of a linked list
function fn(head):
    slow = head
    fast = head

    while fast and fast.next:
        Do something here
        slow = slow.next
        fast = fast.next.next

Key safety check:
- We also check fast.next so fast.next.next is safe (no null.next error).
"""


# ======================================================
# Example 1 — Find the middle node (odd-length list)
# ======================================================

"""
Problem:
Given the head of a linked list with an odd number of nodes, return the
value of the middle node.

Example: 1 → 2 → 3 → 4 → 5  → return 3
"""

# -------- Provided “array conversion” (cheating) approach (as-is) --------
"""
function fn(head):
    array = int[]
    while head:
        array.push(head.val)
        head = head.next

    return array[array.length // 2]
"""

# -------- Provided two-pass (length, then step) Python solution (as-is) --------
def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val


# -------- Provided fast & slow pointer Python solution (as-is) --------
def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val


# -------- Minimal ListNode + input to verify outputs --------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

def build_list(values):
    """Helper to build singly linked list from Python list."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

# ✅ Test Example 1
print("Example 1 — Middle of odd-length list")
head_odd = build_list([1, 2, 3, 4, 5])
print(get_middle(head_odd))  # Expected: 3
print("-" * 40)


# ======================================================
# Example 2 — 141. Linked List Cycle (Floyd’s Tortoise & Hare)
# ======================================================

"""
Idea:
- Move slow by 1, fast by 2.
- If there is a cycle, they must eventually meet.
- If fast reaches the end (None), no cycle.

Why fast cannot "skip over" slow:
- Once inside the cycle, fast reduces the gap to slow by exactly 1 each step.
- The gap hits 0 (they meet) before it can skip past.
"""

# -------- Provided Floyd’s cycle detection solution (as-is) --------
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional['ListNode']) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


"""
Alternative (hashing):
- Iterate and store visited nodes in a set.
- If you see the same node again → cycle.
- Uses O(N) space (worse than O(1) of Floyd’s), but simple to reason about.
"""

# -------- Provided hashing solution (as-is) --------
class Solution:
    def hasCycle(self, head: Optional['ListNode']) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


# -------- Inputs to verify cycle detection --------
def build_cycle_list(values, pos):
    """
    Build a list from values and connect tail to node at index `pos`.
    pos = -1 → no cycle.
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

print("Example 2 — Cycle detection")
cyclic_head    = build_cycle_list([3, 2, 0, -4], pos=1)  # tail connects to node with val=2
acyclic_head   = build_cycle_list([1, 2, 3, 4], pos=-1)  # no cycle

# Recreate the Floyd class (since we overwrote Solution with hashing)
class FloydSolution:
    def hasCycle(self, head: Optional['ListNode']) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

print(FloydSolution().hasCycle(cyclic_head))   # Expected: True
print(FloydSolution().hasCycle(acyclic_head))  # Expected: False
print("-" * 40)


# ======================================================
# Example 3 — Kth node from the end (single pass)
# ======================================================

"""
Trick:
- Advance fast by k steps to create a gap.
- Move slow and fast together until fast hits the end.
- Slow will now point at the kth-from-end node.
"""

# -------- Provided k-th from end solution (as-is) --------
def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# -------- Inputs to verify kth-from-end --------
print("Example 3 — Kth from end")
head_5 = build_list([1, 2, 3, 4, 5])
node_k2 = find_node(head_5, 2)  # Expect node with val=4
print(node_k2.val)              # Expected: 4

node_k1 = find_node(head_5, 1)  # Expect node with val=5
print(node_k1.val)              # Expected: 5
print("-" * 40)


# ----------------------------
# ⏱️ Complexity Summary
# ----------------------------
"""
- Middle node (fast/slow):       O(N) time, O(1) space
- Cycle detection (Floyd’s):     O(N) time, O(1) space
- Kth from end (two pointers):   O(N) time, O(1) space
"""


# ----------------------------
# 🧠 Quick Visuals (ASCII)
# ----------------------------
"""
Middle:
slow: 1 step → 1, 2, 3, ...
fast: 2 steps → 1, 3, 5, (end)
=> slow lands at middle.

Cycle:
Inside cycle, fast closes gap by 1 each loop → must meet slow → cycle exists.

Kth from end:
fast moves k ahead; then both move together;
when fast hits None, slow is k-from-end.
"""


# ----------------------------
# ✅ TL;DR
# ----------------------------
"""
Use different pointer speeds or offsets to:
- Find the middle in one pass.
- Detect cycles without extra memory.
- Grab the kth-from-end node in one pass.

Pattern to remember:
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
"""













def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val



def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    



def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow