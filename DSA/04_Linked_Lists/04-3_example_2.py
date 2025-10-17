# 141. Linked List Cycle

# Example 2

# Given the head of a linked list, determine if the linked list has a cycle.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Solution: https://leetcode.com/problems/linked-list-cycle/description/

# Example 1
    # Input: head = [3, 2, 0, -4], pos = 1
    # Output: true
    # Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2
    # Input: head = [1, 2], pos = 0
    # Output: true
    # Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3
    # Input: head = [1], pos = -1
    # Output: false
    # Explanation: There is no cycle in the linked list.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# --------------------------------------------
# ✅ EXAMPLE 1: Create a cycle (1 → 2 → 3 → 4 → back to 2)
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = b   # cycle here

print(hasCycle(a))  # Output: True

# --------------------------------------------
# ✅ EXAMPLE 2: No cycle (1 → 2 → None)
x = ListNode(1)
y = ListNode(2)

x.next = y

print(hasCycle(x))  # Output: False
    

"""
Time: O(N)
  - Let N = number of nodes in the linked list.
  - The slow pointer moves one step at a time, and the fast pointer moves two steps.
  - In the worst case:
      • If there's no cycle, both pointers traverse the list once → O(N).
      • If there is a cycle, they will meet after at most O(N) steps (Floyd's Tortoise and Hare proof).
  - Overall: O(N).

Space: O(1)
  - Only two pointers (slow, fast) are used regardless of list size.
  - No extra data structures required.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Two-pointer technique traverses the list once to detect a cycle.

Space: O(1)
  - Constant space — only two pointers are used.


---
Overview for Each Iteration
Input: head = [1, 2, 3, 4], pos = 1 (cycle: 1 → 2 → 3 → 4 → 2)

Step: Detect cycle using Floyd's Tortoise and Hare algorithm
Iteration | slow.val | fast.val | fast.next exists | Action
----------|----------|----------|------------------|---------------------
0         | 1        | 1        | True             | slow=2, fast=3
1         | 2        | 3        | True             | slow=3, fast=2
2         | 3        | 2        | True             | slow=4, fast=4
3         | 4        | 4        | True             | slow=fast, return True

Final: True


---
Overview for Each Iteration
Input: head = [1, 2], pos = -1 (no cycle)

Step: Detect cycle using Floyd's Tortoise and Hare algorithm
Iteration | slow.val | fast.val | fast.next exists | Action
----------|----------|----------|------------------|---------------------
0         | 1        | 1        | True             | slow=2, fast=None
1         | 2        | None     | False            | Exit loop, return False

Final: False



---
Most IMPORTANT thing to Understand:
    • The goal is to detect if the linked list loops back on itself (a cycle).  

    • We use two pointers: one moves 1 step at a time (slow), the other 2 steps (fast).  

    • If the list has a cycle, fast will eventually “lap” and meet slow inside the loop.  
      
    • If there's no cycle, fast will hit None and stop.  

---
Why this code Works:
    • Data structure: Linked list nodes with pointers to the next node.  

    • Technique: Fast & slow pointer pattern — fast moves twice as fast as slow.  
      If a cycle exists, they'll meet at some point; if not, fast reaches the end.  

    • Efficiency: O(N) time (each node visited at most twice), O(1) space (no extra structures).  

    • Intuition: Think of two runners on a circular track — if there's a loop, the faster runner eventually catches up.  

---
TLDR (one sentence):
    • Move one pointer slowly and one quickly — if they ever meet, there's a cycle; if fast reaches the end, there isn't.  

---
Quick Example Walkthrough:

Example: 1 → 2 → 3 → 4 → back to 2

Step 1: slow = 1, fast = 1  
Step 2: slow = 2, fast = 3  
Step 3: slow = 3, fast = 2  
Step 4: slow = 4, fast = 4  → met → cycle found ✅  

Example (no cycle): 1 → 2 → None  
Step 1: slow = 1, fast = 1  
Step 2: slow = 2, fast = None → stop → no cycle ❌  

Final Answers:
• First list → True (has cycle)  
• Second list → False (no cycle)



"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def hasCycle(head):
    slow = head               # Start slow pointer at head
    fast = head               # Start fast pointer at head

    while fast and fast.next: # Continue while fast and next node exist
        slow = slow.next      # Move slow pointer one step
        fast = fast.next.next # Move fast pointer two steps
        if slow == fast:      # If pointers meet, cycle exists
            return True       # Return True for cycle
        
    return False              # Return False if no cycle found













# --------------------------------------------
# Alternative less good solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def hasCycle(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

# --------------------------------------------
# ✅ EXAMPLE 1: Create a cycle (1 → 2 → 3 → 4 → back to 1)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b   # cycle here

print(hasCycle(a))  # Output: True

# --------------------------------------------
# ✅ EXAMPLE 2: No cycle (1 → 2 → None)
x = ListNode(1)
y = ListNode(2)

x.next = y

print(hasCycle(x))  # Output: False