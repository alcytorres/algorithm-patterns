# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 
# Solution: https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Example 1:
    # Input: head = [1, 2, 3, 4]
    # Output: [2, 1, 4, 3]
    # Explanation: View image

# Example 2:
    # Input: head = []
    # Output: []

# Example 3:
    # Input: head = [1]
    # Output: [1]

# Example 4:
    # Input: head = [1, 2, 3]
    # Output: [2, 1, 3]


# HINT: Draw the linked list at each iteration to see how the pointers change

# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Approach 1: Swap Nodes in Pairs (Dummy Node Version)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # Dummy node acts as the prev node for the head node
    # of the list and hence stores pointer to the head node.
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    while head and head.next:

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Reinitializing the head and prev for next swap
        prev = first_node
        head = first_node.next

    # Return the new head node.
    return dummy.next


# Helper: Convert linked list to list for printing
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# --------------------------------------------
# EXAMPLE 1: head = [1, 2, 3, 4]
a = ListNode(1); b = ListNode(2)
c = ListNode(3); d = ListNode(4)

a.next = b; b.next = c; c.next = d

result = swapPairs(a)
print("Output 1:", to_list(result))  # [2, 1, 4, 3]

# --------------------------------------------
# EXAMPLE 2: head = [1]
a = ListNode(1)

result = swapPairs(a)
print("Output 2:", to_list(result))  # [1]

# --------------------------------------------
# EXAMPLE 3: head = [1, 2, 3]
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b; b.next = c

result = swapPairs(a)
print("Output 3:", to_list(result))  # [2, 1, 3]


"""
Time: O(N)
  - Count occurrences of all numbers → O(N).
  - Loop through dictionary of U unique numbers → O(U), where U ≤ N.
  - Overall: O(N).

Space: O(U) ≈ O(N)
  - Dictionary 'counts' stores up to U unique numbers.
  - A few variables (max_unique, num) use O(1).
  - Overall: O(U), which in the worst case is O(N).

  
Interview Answer

Time: O(N)
  - Count elements and scan counts once.

Space: O(N)
  - Dictionary stores up to N unique numbers.



Overview for Each Iteration
Input: head = [1, 2, 3, 4]

Step: Swap pairs of nodes in linked list
prev.val | head.val | first.val | second.val | Action                                       
---------|----------|-----------|------------|--------------------------------------------
-1       | 1        | 1         | 2          | prev.next=2, first.next=3, second.next=1    
1        | 3        | 3         | 4          | prev.next=4, first.next=None, second.next=3

Linked List
-------------
[-1 → 2 → 1 → 3 → 4]
[-1 → 2 → 1 → 4 → 3]

Final: [2, 1, 4, 3]



---
Most IMPORTANT thing to Understand:
    • We're swapping *pairs of nodes* (not just their values).

    • Use a dummy node to simplify handling the head swap — it points to the start of the list.

    • For each pair, reconnect pointers so their order flips: first ↔ second → rest of list.

---
Why this code Works:
    • Data structure: singly linked list.

    • Technique: pointer manipulation using a dummy node.
        - `prev` tracks the node before the current pair.
        - Swap two nodes by updating `.next` pointers:
            prev → second → first → next pair.
        - Move `prev` and `head` forward by two nodes for the next swap.

    • Efficiency: O(N) time — each node visited once; O(1) space — swaps done in place.

    • Intuition: Think of walking through the list and flipping every two adjacent cards while keeping the rest intact.

---
TLDR:
    • Use a dummy node and pointer updates to swap every two nodes without losing connections.

---
Quick Example Walkthrough:

Input: [1 → 2 → 3 → 4]

    Step 0: dummy → 1 → 2 → 3 → 4  
        prev = dummy, head = 1

    Step 1: Swap (1, 2)
        first_node = 1
        second_node = 2

        prev.next = 2  
        1.next = 3  
        2.next = 1  

        List: dummy → 2 → 1 → 3 → 4  
        Move prev = 1, head = 3


    Step 2: Swap (3, 4)
        first_node = 3
        second_node = 4

        prev.next = 4  
        3.next = None  
        4.next = 3  

        List: dummy → 2 → 1 → 4 → 3  
        Move prev = 3, head = None

Final Output: [2, 1, 4, 3] ✅



---
Quick Example Walkthrough:

Input: [1 → 2 → 3]

    Step 0: dummy → 1 → 2 → 3  
        prev = dummy, head = 1

    Step 1: Swap (1, 2)
        first_node = 1
        second_node = 2

        prev.next = 2  
        1.next = 3  
        2.next = 1  

        List: dummy → 2 → 1 → 3  
        Move prev = 1, head = 3

    Step 2: Stop (no pair left)
        head.next = None  
        Loop ends.

Final Output: [2, 1, 3] ✅




---
Q: Why do we return dummy.next? (Example-based explanation)
  • Imagine the input list: [1 → 2 → 3 → 4]
  • We add a dummy node before it: [-1 → 1 → 2 → 3 → 4]

  • After swapping pairs:
      dummy → 2 → 1 → 4 → 3

  • The dummy's next pointer now points to the true new head (2).
  • If we returned dummy, we'd include the fake -1 node.

  • Returning dummy.next skips the dummy and returns the real swapped list:
      ✅ [2 → 1 → 4 → 3]



---
Q: Why do we use `while head and head.next:` instead of `while head:`?
    • Each swap needs a pair of nodes — the current node (`head`) and the next one (`head.next`).
    
    • If we only check `while head:`, the last single node (when list length is 
    odd) would try to swap with `None` → causes an error.
    
    • `while head and head.next:` safely stops when fewer than 2 nodes remain.

    • This ensures all valid pairs are swapped without breaking the list.

"""


# –––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def swapPairs(head):
    dummy = ListNode(-1)      # Create dummy node pointing to head
    dummy.next = head         # Link dummy to head
    prev = dummy         # Initialize prev at dummy

    while head and head.next:    # Continue while at least two nodes remain

        # Nodes to be swapped
        first_node = head        # First node to swap
        second_node = head.next  # Second node to swap

        # Swapping
        prev.next = second_node  # Link prev to second
        first_node.next = second_node.next  # Link first to node after second
        second_node.next = first_node  # Link second to first

        # Reinitializing the head and prev for next swap
        prev = first_node  # Update prev to first for next iteration
        head = first_node.next  # Move head to next pair

    return dummy.next         # Return head of modified list








# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Approach 2: Recursive Approach
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


# Helper: Convert linked list to list for printing
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# --------------------------------------------
# EXAMPLE: head = [1, 2, 3, 4]
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b; b.next = c; c.next = d

result = Solution().swapPairs(a)
print("Output:", to_list(result))  # [2, 1, 4, 3]