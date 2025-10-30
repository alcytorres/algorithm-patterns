# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
    # Input: head = [1, 2, 3]
    # Output: [3, 2, 1]

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
        # Reverse the Link
        temp = curr.next
        curr.next = prev

        # Advance the Pointers
        prev = curr
        curr = temp
        
    return prev

#  Output: 3 → 2 → 1

# --------------------------------------------
# EXAMPLE 1: Linked list: head = [1 → 2 → 3]
a = ListNode(1); b = ListNode(2); c = ListNode(3)

a.next = b; b.next = c;

# Reverse and collect output
result = reverseList(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 1:", ans)   # [3, 2, 1]


# --------------------------------------------
# EXAMPLE 2: Linked list: head = [1 → 2]
a = ListNode(1)
b = ListNode(2)
a.next = b

# Reverse and collect output
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
  - Uses only three pointers: prev, curr, and temp.
  - No additional data structures are created.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass reverses all node links.

Space: O(1)
  - Constant space — only a few pointer variables used.


---
Overview for Each Iteration
Input: head = [1, 2, 3]

Step: Reverse linked list by updating pointers
curr.val | temp.val | prev.val | Action                         | Linked List
---------|----------|----------|--------------------------------|-----------------
1        | 2        | None     | curr.next=None, prev=1, curr=2 | [1→None, 2→3]
2        | 3        | 1        | curr.next=1, prev=2, curr=3    | [2→1→None, 3]
3        | None     | 2        | curr.next=2, prev=3, curr=None | [3→2→1→None]

Final: [3, 2, 1]


---
Overview for Each Iteration
Input: head = [1, 2]

Step: Reverse linked list by updating pointers
curr.val | temp.val | prev.val | Action
---------|----------|----------|-------------------------------
1        | 2        | None     | curr.next=None, prev=1, curr=2
2        | None     | 1        | curr.next=1, prev=2, curr=None

Final: [2, 1]



---
Most IMPORTANT thing to Understand:
    • We reverse the direction of every link in the list — each node points to the one before it.

    • We track three things: the current node (curr), the one before it (prev), and the next one (temp).

    • When done, the old tail (last node) becomes the new head.

---
Why this code Works:
    • Data structure: Linked list with `.next` pointers connecting nodes.

    • Technique: Iterative reversal.
        • Save the next node (temp).
        • Reverse the link → curr.next = prev.
        • Move forward → prev = curr, curr = temp.

    • Efficiency: O(N) time (each node processed once), O(1) space (only 3 pointers).

    • Intuition: Like flipping arrows in a chain — one by one until they all point backward.

---
TLDR:
    • Traverse the list, reversing each node's pointer so all links point backward.

    
Quick Example Walkthrough:

Input: [1 → 2 → 3 → None]  ==>  [3 → 2 → 1 → None]

We use three pointers each iteration:
  • prev   : tail of the reversed part
  • curr   : current node we're reversing
  • temp   : saves curr.next so we don't lose the rest

    Start:
    prev = None
    curr = 1

    curr: 1 → 2 → 3 → None


    ——— Iteration 1 ———
        temp = 2
        curr.next = prev   (1.next = None)

        Reversed part: 1 → None
        Remaining    : 2 → 3 → None

        Move forward:
        prev = 1
        curr = 2


    ——— Iteration 2 ———
        temp = 3
        curr.next = prev   (2.next = 1)

        Reversed part: 2 → 1 → None
        Remaining    : 3 → None

        Move forward:
        prev = 2
        curr = 3


    ——— Iteration 3 ———
        temp = None
        curr.next = prev   (3.next = 2)

        Reversed part: 3 → 2 → 1 → None
        Remaining    : None

        Move forward:
        prev = 3
        curr = None  (stop)

    
Return prev (new head): [3 → 2 → 1 → None]

✅ Final: [3, 2, 1] 



---
Q: Why do we return 'prev' instead of 'curr' or 'head'?

  • 'head' never changes — it always points to the original first node (which becomes the tail).

  • 'curr' keeps moving forward and ends up as None when the loop finishes.

  • 'prev' tracks the node most recently reversed — by the end, it points to the new head.

  • Therefore, returning 'prev' gives us the fully reversed linked list.

  


Q: Why do we use `while curr:` instead of `while curr and curr.next:`?
    • We must process every node — including the last one.

    • `while curr:` continues until `curr` becomes None, ensuring all nodes are reversed.

    • `while curr and curr.next:` stops one node early, leaving the final node's link unreversed.

    • So `while curr:` is correct and necessary for a complete reversal.


"""



# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Breakdown 
def reverseList(head):
    prev = None             # Initialize previous pointer as None
    curr = head             # Start at head of list

    while curr:             # Iterate until end of list

        # Reverse the Link
        temp = curr.next    # Store next node temporarily
        curr.next = prev    # Reverse link to point to previous node

        # Advance the Pointers
        prev = curr         # Move prev to current node
        curr = temp         # Move curr to next node

    return prev             # Return new head of reversed list










# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Alternative Solution

def reverseList(self, head):
    if (not head) or (not head.next):
        return head
    
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p