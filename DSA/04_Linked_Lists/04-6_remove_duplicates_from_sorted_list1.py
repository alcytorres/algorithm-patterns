# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
 
# Example 1:
    # Input: head = [1, 1, 2]
    # Output: [1, 2]

# Example 2:
    # Input: head = [1, 1, 2, 3, 3]
    # Output: [1, 2, 3]

# Solution: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    curr = head
    
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next   # skip the duplicate
        else:
            curr = curr.next

    return head

# --------------------------------------------
# EXAMPLE 1: Linked list: head = [1 → 1 → 2]
a = ListNode(1); b = ListNode(1); c = ListNode(2)

# Link them together
a.next = b; b.next = c

# Run
result = deleteDuplicates(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output:", ans)   # [1, 2]


# --------------------------------------------
# EXAMPLE 2: Linked list: head = [1 → 1 → 2 → 3 → 3]
a = ListNode(1); b = ListNode(1); c = ListNode(2)
d = ListNode(3); e = ListNode(3)

# Link them together
a.next = b; b.next = c; c.next = d; d.next = e

# Run
result = deleteDuplicates(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output:", ans)   # [1, 2, 3]


"""
Time: O(N)
  - Let N = number of nodes in the linked list.
  - The algorithm traverses the list once using a single pointer (curr).
  - For each node, at most one comparison and possibly one link adjustment are made → O(1) per step.
  - Overall: O(N).

Space: O(1)
  - Only one pointer variable (curr) is used to traverse the list.
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass removes duplicates in one traversal.

Space: O(1)
  - Constant space — only one pointer used.


---
Overview for Each Iteration
Input: head = [1, 1, 2]

Step: Remove duplicates from sorted linked list
curr.val | curr.next.val | curr.val == curr.next.val | Action
---------|---------------|---------------------------|------------------------------
1        | 1             | True                      | Skip duplicate, curr.next = 2
1        | 2             | False                     | Move curr to 2
2        | None          | -                         | Exit loop

Final: [1, 2]


---
Overview for Each Iteration
Input: head = [1, 1, 2, 3, 3]

Step: Remove duplicates from sorted linked list
curr.val | curr.next.val | curr.val == curr.next.val | Action
---------|---------------|---------------------------|---------------------------------
1        | 1             | True                      | Skip duplicate, curr.next = 2
1        | 2             | False                     | Move curr to 2
2        | 3             | False                     | Move curr to 3
3        | 3             | True                      | Skip duplicate, curr.next = None
3        | None          | -                         | Exit loop

Final: [1, 2, 3]


---
Overview for Each Iteration
Input: head = [1, 1, 1, 2, 3]

Step: Remove duplicates from sorted linked list
curr.val | curr.next.val | curr.val == curr.next.val | Action                       | Linked List
---------|---------------|---------------------------|------------------------------|-------------
1        | 1             | True                      | Skip duplicate, curr.next=1  | [1→1→2→3]
1        | 1             | True                      | Skip duplicate, curr.next=2  | [1→2→3]
1        | 2             | False                     | Move curr to 2               | [1→2→3]
2        | 3             | False                     | Move curr to 3               | [1→2→3]
3        | None          | -                         | Exit loop                    | [1→2→3]

Final: [1, 2, 3]




---
Most IMPORTANT thing to Understand:
    • The list is already sorted — so duplicates are always next to each other.

    • We only need to remove consecutive nodes with the same value.

    • We do this in-place by skipping over duplicates instead of creating a new list.

---
Why this code Works:
    • Data structure: Linked list with nodes connected by `.next` pointers.

    • Technique: Iterate through the list with a pointer `curr`.
        • If curr.val == curr.next.val → duplicate → skip it using `curr.next = curr.next.next`.
        • Else → move forward to next node.

    • Efficiency: O(N) time since we scan the list once, and O(1) space since we modify in place.

    • Intuition: Like cleaning up consecutive repeats — if you see the same number twice in a row, erase the extra one.

---
TLDR:
    • Walk through the list once and skip nodes that have the same value as the current node.

---
Quick Example Walkthrough:

Example: head = [1 → 1 → 2 → 3 → 3]

    Step 1: curr = 1 → next = 1 → duplicate → skip → list becomes [1 → 2 → 3 → 3]  
    Step 2: curr = 1 → next = 2 → move to 2  
    Step 3: curr = 2 → next = 3 → move to 3  
    Step 4: curr = 3 → next = 3 → duplicate → skip → list becomes [1 → 2 → 3]  

Final Answer: [1, 2, 3]



---
Q: Where do we set `head` to point to the first node?

- When we call the function like this:
    result = deleteDuplicates(a)

- The variable `a` represents the first node in the linked list (value = 1).

- Inside the function definition:
    def deleteDuplicates(head):

  the parameter `head` now points to whatever we passed in — in this case, node `a`.

- So, `head` automatically becomes a reference to the first node
  at the moment the function is called.

✅ In short:
  • We don't manually write `head = a` in our code,
  • because it happens implicitly when we call `deleteDuplicates(a)`.


  
---
Q: Why return `head`?
  • `head` always points to the first node of the list.
  
  • Even though `curr` moves, `head` never changes.
  
  • After deleting duplicates, the list still starts at that same first node.

👉 Returning `head` gives back the entire updated list from its beginning.



---
Q: Why does 'while curr and curr.next:' work, but 'while curr:' does NOT?

    - Because 'while curr and curr.next:' checks that both the current node and the next node exist before comparing values.

    - This prevents accessing curr.next.val when curr.next is None (at the end of the list).

    - In contrast, 'while curr:' keeps looping even when curr.next is None, causing an AttributeError.

    - So the safe version stops before the end, while the broken one tries to read past it.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Same Solution rewirtten 
def deleteDuplicates(head):
    curr = head

    while curr is not None and curr.next is not None:
        if curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head



# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown 
def deleteDuplicates(head):
    curr = head               # Start at head of list

    while curr and curr.next: # Iterate while current and next nodes exist
        if curr.val == curr.next.val:  # If current value equals next value
            curr.next = curr.next.next # Skip duplicate by updating next pointer
        else:
            curr = curr.next    # Move to next node if no duplicate

    return head                 # Return head of modified list






# –––––––––––––––––––––––––––––––
# Comparing ListNode Class Initializations: Mandatory vs. Optional Parameters
# –––––––––––––––––––––––––––––––

# First ListNode class
class ListNode1:
    def __init__(self, val):
        self.val = val
        self.next = None

# Second ListNode class
class ListNode2:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Initialize nodes to show differences
# ListNode1: Requires val, next is always None
node1 = ListNode1(5)  # Works: val=5, next=None
# node1 = ListNode1()  # Error: val is required
print("ListNode1:", node1.val, node1.next)  # Output: ListNode1: 5 None

# ListNode2: val optional (defaults to 0), next optional
node2a = ListNode2()  # Works: val=0, next=None
node2b = ListNode2(10)  # Works: val=10, next=None
node2c = ListNode2(20, node2b)  # Works: val=20, next=node2b
print("ListNode2a:", node2a.val, node2a.next)  # Output: ListNode2a: 0 None
print("ListNode2b:", node2b.val, node2b.next)  # Output: ListNode2b: 10 None
print("ListNode2c:", node2c.val, node2c.next.val if node2c.next else None)  # Output: ListNode2c: 20 10
