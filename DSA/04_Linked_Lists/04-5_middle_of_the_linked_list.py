# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
    # Input: head = [1, 2, 3, 4, 5]
    # Output: [3, 4, 5]
    # Explanation: The middle node of the list is node 3.

# Example 2:
    # Input: head = [1, 2, 3, 4, 5, 6]
    # Output: [4, 5, 6]
    # Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Solution: https://leetcode.com/problems/middle-of-the-linked-list/description/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def middleNode(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# --------------------------------------------
# EXAMPLE 1: Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1); b = ListNode(2); c = ListNode(3)
d = ListNode(4); e = ListNode(5)

# Link them together
a.next = b; b.next = c; c.next = d; d.next = e

# Run
result = middleNode(a)
curr = result
ans = []
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 1:", ans)   # [3, 4, 5]


# --------------------------------------------
# EXAMPLE 2: Linked list: 1 → 2 → 3 → 4 → 5 → 6
a = ListNode(1); b = ListNode(2); c = ListNode(3);
d = ListNode(4); e = ListNode(5); f = ListNode(6)

# Link them together
a.next = b; b.next = c; c.next = d; d.next = e; e.next = f

# Run
result = middleNode(a)
curr = result
ans = []
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 2:", ans)   # [4, 5, 6]

"""

Time: O(N)
  - Let N = number of nodes in the linked list.
  - The fast pointer moves twice as fast as the slow pointer.
  - The loop continues until the fast pointer reaches the end, meaning the slow pointer will be at the middle.
  - Each node is visited at most once by each pointer.
  - Overall: O(N).

Space: O(1)
  - Only two pointers (slow, fast) are used.
  - No additional data structures are required.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Two-pointer traversal finds the middle in a single pass.

Space: O(1)
  - Constant space — only two pointers are maintained.


  
---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5]

Step: Find middle node using slow and fast pointers
Iteration | slow.val | fast.val | fast.next exists | Action
----------|----------|----------|------------------|--------------------
0         | 1        | 1        | True             | slow=2, fast=3
1         | 2        | 3        | True             | slow=3, fast=5
2         | 3        | 5        | False            | Exit loop

Final: slow.val = 3, Output: [3, 4, 5]


---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5, 6]

Step: Find middle node using slow and fast pointers
Iteration | slow.val | fast.val | fast.next exists | Action
----------|----------|----------|------------------|--------------------
0         | 1        | 1        | True             | slow=2, fast=3
1         | 2        | 3        | True             | slow=3, fast=5
2         | 3        | 5        | True             | slow=4, fast=None
3         | 4        | None     | False            | Exit loop

Final: slow.val = 4, Output: [4, 5, 6]




---
Q: Why does the output show [3, 4, 5] instead of just 3?

LeetCode displays the linked list starting from the node you return.
  • So when you return the middle node (value 3),
  • it prints the entire list from that node onward: [3, 4, 5].

  • In other words, you're returning the node itself — not just its value.
  • The platform automatically shows the remaining nodes after it.



Q: How does this code ensure that if there are two middle nodes, it returns the second one?

  • The `fast` pointer moves 2 steps at a time while `slow` moves 1.
  • When the list has an even number of nodes, `fast` reaches the end AFTER `slow` passes the first middle node.

  • As a result, `slow` ends up pointing to the second middle node, which is what the problem asks for.

"""



# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown 
def middleNode(head):
    slow = fast = head        # Start both pointers at head

    while fast and fast.next: # Continue while fast and next node exist
        slow = slow.next      # Move slow pointer one step
        fast = fast.next.next # Move fast pointer two steps

    return slow               # Slow pointer is at middle node




# ––––––––––––––––––––––––––––––––––––––––––––––– 
# 876. Middle of the Linked List (MODIFIED)

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the FIRST middle node.

# Example 1:
    # Input: head = [1, 2, 3, 4, 5, 6]
    # Output: [3, 4, 5, 6]
    # Explanation: Since the list has two middle nodes with values 3 and 4, we return the FIRST one.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def middleNode_first(head):
    slow = fast = head

    # Move fast ahead only if fast.next and fast.next.next exist
    # This ensures slow stops one step earlier (the first middle)
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# --------------------------------------------
# EXAMPLE: Linked list: 1 → 2 → 3 → 4 → 5 → 6
a = ListNode(1); b = ListNode(2); c = ListNode(3)
d = ListNode(4); e = ListNode(5); f = ListNode(6)

# Link them together
a.next = b; b.next = c; c.next = d; d.next = e; e.next = f

# Run
result = middleNode_first(a)
curr = result
ans = []
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output:", ans)   # [3, 4, 5, 6]

"""
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5, 6]

Step: Find first middle node using slow and fast pointers
i  | slow.val | fast.val | fast.next exists | fast.next.next exists | Action
---|----------|----------|------------------|-----------------------|---------------
0  | 1        | 1        | True             | True                  | slow=2, fast=3
1  | 2        | 3        | True             | True                  | slow=3, fast=5
2  | 3        | 5        | True             | False                 | Exit loop

Final: slow.val = 3, Output: [3, 4, 5, 6]

"""