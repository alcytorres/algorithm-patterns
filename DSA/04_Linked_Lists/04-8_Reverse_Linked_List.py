# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
    # Input: head = [1, 2, 3, 4, 5]
    # Output: [5, 4, 3, 2, 1]

# Example 2:
    # Input: head = [1, 2]
    # Output: [2, 1]

# Example 3:
    # Input: head = []
    # Output: []

# Solution: https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
        
    return prev


# --------------------------------------------
# ✅ EXAMPLE 1: Linked list: head = [1 → 2 → 3 → 4 → 5]
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b; b.next = c; c.next = d; d.next = e

# Reverse and collect output
result = reverseList(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 1:", ans)   # [5, 4, 3, 2, 1]


# --------------------------------------------
# ✅ EXAMPLE 2: Linked list: head = [1 → 2]
a = ListNode(1)
b = ListNode(2)
a.next = b

result = reverseList(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 2:", ans)   # [2, 1]

 
"""
Time: O(N)
  - Let N = number of nodes in the linked list.
  - The algorithm traverses the list once.
  - For each node, one pointer reversal is performed → O(1) per step.
  - Overall: O(N).

Space: O(1)
  - Uses only three pointers: prev, curr, and next_temp.
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass reverses all node links.

Space: O(1)
  - Constant space — only a few pointer variables used.


---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5]

Step: Reverse linked list by updating pointers
curr.val | next_temp.val | prev.val | Action                         | Linked List
---------|---------------|----------|--------------------------------|-----------------
1        | 2             | None     | curr.next=None, prev=1, curr=2 | 1→None, 2→3→4→5
2        | 3             | 1        | curr.next=1, prev=2, curr=3    | 2→1→None, 3→4→5
3        | 4             | 2        | curr.next=2, prev=3, curr=4    | 3→2→1→None, 4→5
4        | 5             | 3        | curr.next=3, prev=4, curr=5    | 4→3→2→1→None, 5
5        | None          | 4        | curr.next=4, prev=5, curr=None | 5→4→3→2→1→None

Final: [5, 4, 3, 2, 1]


---
Overview for Each Iteration
Input: head = [1, 2]

Step: Reverse linked list by updating pointers
curr.val | next_temp.val | prev.val | Action
---------|---------------|----------|------------------
1        | 2             | None     | curr.next=None, prev=1, curr=2
2        | None          | 1        | curr.next=1, prev=2, curr=None

Final: [2, 1]



---
Most IMPORTANT thing to Understand:
    • We reverse the direction of every link in the list — each node points to the one before it.

    • We track three things: the current node (curr), the one before it (prev), and the next one (next_temp).

    • When done, the old tail (last node) becomes the new head.

---
Why this code Works:
    • Data structure: Linked list with `.next` pointers connecting nodes.

    • Technique: Iterative reversal.
        • Save the next node (next_temp).
        • Reverse the link → curr.next = prev.
        • Move forward → prev = curr, curr = next_temp.

    • Efficiency: O(N) time (each node processed once), O(1) space (only 3 pointers).

    • Intuition: Like flipping arrows in a chain — one by one until they all point backward.

---
TLDR:
    • Traverse the list, reversing each node's pointer so all links point backward.

---
Quick Example Walkthrough:

Input: [1 → 2 → 3 → 4 → 5]

    Start: prev = None, curr = 1

    Step 1: next_temp = 2 → curr.next = None → prev = 1 → curr = 2  
    List: 1→None, 2→3→4→5  

    Step 2: next_temp = 3 → curr.next = 1 → prev = 2 → curr = 3  
    List: 2→1→None, 3→4→5  

    Step 3: next_temp = 4 → curr.next = 2 → prev = 3 → curr = 4  
    List: 3→2→1→None, 4→5  

    Step 4: next_temp = 5 → curr.next = 3 → prev = 4 → curr = 5  
    List: 4→3→2→1→None, 5  

    Step 5: next_temp = None → curr.next = 4 → prev = 5 → curr = None  
    List: 5→4→3→2→1→None ✅  

Final Answer: [5, 4, 3, 2, 1]

"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def reverseList(head):
    prev = None               # Initialize previous pointer as None
    curr = head               # Start at head of list

    while curr:               # Iterate until end of list
        next_temp = curr.next # Store next node temporarily
        curr.next = prev      # Reverse link to point to previous node
        prev = curr           # Move prev to current node
        curr = next_temp      # Move curr to next node

    return prev               # Return new head of reversed list




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Solution

def reverseList(self, head):
    if (not head) or (not head.next):
        return head
    
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p