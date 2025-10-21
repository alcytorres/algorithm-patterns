# Find the Middle Node in a Singly Linked List

# Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.

# --------------------------------------------
# FIND MIDDLE NODE OF A LINKED LIST
# --------------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

# --------------------------------------------
# ✅ EXAMPLE Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = e

# Print Result
print(get_middle(a))
# Output: 3


"""
Time: O(N)
  - Let N = number of nodes in the linked list.
  - Both slow and fast pointers start at the head.
  - The fast pointer moves two steps while the slow pointer moves one step.
  - When the fast pointer reaches the end, the slow pointer will be at the middle.
  - Each node is visited at most once by each pointer.
  - Overall: O(N).

Space: O(1)
  - Only two pointers (slow, fast) are used.
  - No extra data structures or recursive calls are needed.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Two-pointer traversal finds the middle in one pass.

Space: O(1)
  - Constant space — only two pointers used.

  
---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5]

Step: Find middle node using slow and fast pointers
Iteration | slow.val | fast.val | fast.next exists | Action
----------|----------|----------|------------------|----------------
0         | 1        | 1        | True             | slow=2, fast=3
1         | 2        | 3        | True             | slow=3, fast=5
2         | 3        | 5        | False            | Exit loop

Final: 3 (slow.val)



Most IMPORTANT thing to Understand:
    • We use two pointers — `slow` moves one step at a time, `fast` moves two steps.

    • When `fast` reaches the end, `slow` will be at the middle.

    • Works for both even and odd lengths — for even, it returns the *second* middle node.

---
Why this code Works:
    • Data structure: singly linked list.

    • Technique: “fast and slow pointers.”
        - `fast` moves twice as fast as `slow`.
        - By the time `fast` finishes the list, `slow` has gone halfway.

    • Efficiency: O(N) time (each node visited at most once), O(1) space (just two pointers).

    • Intuition: Like two runners — one runs twice as fast; when the fast one finishes, the slower is halfway.

---
TLDR (one sentence):
    • Move one pointer twice as fast as the other; when the fast one finishes, the slow one points to the middle.

---
Quick Example Walkthrough:

Linked List: [1 → 2 → 3 → 4 → 5]

    Step 0: slow = 1, fast = 1  
    Step 1: slow = 2, fast = 3  
    Step 2: slow = 3, fast = 5  
    fast.next = None → stop.

Final: slow = 3 → return 3

"""


# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown 
def get_middle(head):
    slow = head               # Start slow pointer at head
    fast = head               # Start fast pointer at head

    while fast and fast.next: # Continue while fast and next node exist
        slow = slow.next      # Move slow pointer one step
        fast = fast.next.next # Move fast pointer two steps

    return slow.val           # Return value of middle node




# --------------------------------------------
# Alternative less good Solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val

# --------------------------------------------
# ✅ EXAMPLE Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = e

# Print Result
print(get_middle(a))
# Output: 3



# --------------------------------------------
# Brute Force
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr[len(arr) // 2]

# --------------------------------------------
# ✅ EXAMPLE Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = e

# Print Result
print(get_middle(a))
# Output: 3