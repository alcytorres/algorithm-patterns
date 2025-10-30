# 92. Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1
    # Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
    # Output: [1, 4, 3, 2, 5]

# Example 2:
    # Input: head = [5], left = 1, right = 1
    # Output: [5]

# Solution: https://leetcode.com/problems/reverse-linked-list-ii/description/

# --------------------------------------------
# 1) One-pass “head-insertion” (anchor at left-1) — simplest + fastest to write
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    # 1) Move prev to the node BEFORE position 'left'
    for _ in range(left - 1):
        prev = prev.next
    curr = prev.next

    # 2) Reverse by repeatedly moving curr.next to the FRONT of the sublist
    for _ in range(right - left):
        temp = curr.next          # node to relocate
        curr.next = temp.next     # detach temp
        temp.next = prev.next     # put temp at front of the sublist
        prev.next = temp          # reconnect front

    return dummy.next


# Helper to convert linked list to Python list for easy printing
def to_list(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


# --------------------------------------------
# EXAMPLE 1: head = [1, 2, 3, 4, 5], left = 2, right = 4
a = ListNode(1); b = ListNode(2); c = ListNode(3)
d = ListNode(4); e = ListNode(5)

a.next = b; b.next = c; c.next = d; d.next = e

result = reverseBetween(a, 2, 4)
print("Output 1:", to_list(result))   # [1, 4, 3, 2, 5]


# --------------------------------------------
# EXAMPLE 2: head = [5], left = 1, right = 1
a = ListNode(5)

result = reverseBetween(a, 1, 1)
print("Output 2:", to_list(result))   # [5]


# --------------------------------------------
# EXAMPLE 3: head = [10, 20, 30, 40, 50], left = 2, right = 4
a = ListNode(10); b = ListNode(20); c = ListNode(30)
d = ListNode(40); e = ListNode(50)

a.next = b; b.next = c; c.next = d; d.next = e

result = reverseBetween(a, 2, 4)
print("Output 2:", to_list(result))   # [10, 40, 30, 20, 50]





"""
Time: O(N)
  - Let N = number of nodes in the linked list.
  - Step 1: Move the 'prev' pointer to the node before 'left' → O(left).
  - Step 2: Reverse the sublist between 'left' and 'right' using local pointer changes → O(right - left).
  - Both steps are linear total, in the worst case.
  - Overall: O(N).

Space: O(1)
  - Uses only a few pointers (dummy, prev, curr, temp).
  - Reversal is done in place, without extra data structures.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single traversal reverses sublist within one pass.

Space: O(1)
  - Constant space for pointer manipulation.


  
---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5], left = 2, right = 4

Step 1: Move prev to node before 'left' (left-1 = 1)
i   | prev.val
----|---------
0   | 1

Step 2: Reverse sublist from position 2 to 4
i   | curr.val | temp.val | curr.nxt.val | temp.next.val | prev.nxt.val  | Action                                    
----|----------|----------|--------------|---------------|---------------|--------------------------------------
0   | 2        | 3        | 3            | 4             | 2             | curr.next=4, temp.next=2, prev.next=3 
1   | 2        | 4        | 4            | 5             | 3             | curr.next=5, temp.next=3, prev.next=4 


Linked List
-------------------
[1 → 3 → 2 → 4 → 5]
[1 → 4 → 3 → 2 → 5]


Final: [1, 4, 3, 2, 5]
  

---
Overview for Each Iteration
Input: head = [5], left = 1, right = 1

Step 1: Check if left == right
left = 1, right = 1, return head unchanged

Final: [5]



---
Most IMPORTANT thing to Understand:
    • We reverse only the segment [left, right] in-place; everything else stays as-is.

    • A dummy node lets us uniformly handle cases where left = 1.

    • We park a pointer (prev) at the node before 'left' and then repeatedly pull the next node after 'curr' to the front of the sublist.

---
Why this code Works:
    • Data structure: singly linked list; we manipulate only .next pointers.

    • Technique (head insertion inside the window): keep 'curr' at the start of the sublist and, for (right - left) times, take curr.next out and insert it right after 'prev'.

    • Correctness: nodes between left..right are rotated to the front one by one, producing the exact reversal while preserving outside links.

    • Efficiency: O(n) time (single pass) and O(1) extra space (constant pointers).

---
TLDR:
    • Move to left-1, then repeatedly take the node after 'curr' and insert it right after 'prev' until the [left, right] segment is reversed.

---
Quick Example Walkthrough:
    head = [1, 2, 3, 4, 5], left = 2, right = 4

    Setup
        dummy → 1 → 2 → 3 → 4 → 5
        prev = node(1)   (node before left)
        curr = prev.next = node(2)

    We will do `(right - left) = 2` head-insertions.


    Iteration 1 (bring 3 to front of sublist):
        temp = curr.next = 3
        
        Rewire:
        curr.next = temp.next   → 2.next = 4
        temp.next = prev.next   → 3.next = 2
        prev.next = temp        → 1.next = 3

        List now: 1 → 3 → 2 → 4 → 5
        (`prev` still at 1, `curr` still at 2)
        

    Iteration 2 (bring 4 to front of sublist):
        temp = curr.next = 4
        
        Rewire:
        curr.next = temp.next   → 2.next = 5
        temp.next = prev.next   → 4.next = 3
        prev.next = temp        → 1.next = 4

        List now: 1 → 4 → 3 → 2 → 5
        (sublist [2..4] is reversed)

    
Return dummy.next → 1 → 4 → 3 → 2 → 5
Final Output: [1, 4, 3, 2, 5] ✅



---
Q: Why this works?
  • prev marks the node before the reversal starts.

  • curr stays fixed at the start of the sublist.

  • Each loop takes curr.next (temp) and moves it right after prev, effectively pulling nodes to the front one by one.



---
Why do we need 'for _ in range(right - left):'?

  • It tells us how many pointer swaps are needed to reverse the chosen section.
  
  • Each loop takes one node from after 'curr' and moves it to the front of the sublist.
  
  • To fully reverse N nodes, you need N-1 moves — that's what (right - left) represents.
  
  Example: left=2, right=4 means 3 nodes (2,3,4); we need 2 moves:
    1st move: 3 → front  → [1,3,2,4,5]
    2nd move: 4 → front  → [1,4,3,2,5]


---
Q: Why do we pass 2 and 4 instead of b and d?

    • The function uses positions, not node variables.

    • left=2 and right=4 mean "reverse nodes at positions 2 through 4."

    • You can't pass b or d because those are node objects, not positions.

    
---
Q: Why was it confusing with [1, 2, 3, 4, 5]?

    • The numbers looked like both values and positions.

    • Using values like [10, 20, 30, 40, 50] makes it clear they're just positions, not node values.


"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def reverseBetween(head, left, right):
    # 0) Early exit — empty list or no-op range
    if not head or left == right:  # If empty list or no reversal needed
        return head                # Return original head
    
    # 1) Setup — add dummy before head; start prev at dummy
    dummy = ListNode(-1)    # Create dummy node pointing to head
    dummy.next = head       # Link dummy to head
    prev = dummy            # Start prev at dummy

    # 2) Move prev to the node BEFORE position 'left'
    for _ in range(left - 1):   # Move prev to node before left position
        prev = prev.next
    curr = prev.next            # Start curr at left position

    # 3) Reverse by repeatedly moving curr.next to the FRONT of the sublist
    for _ in range(right - left):   # Reverse sublist right-left times
        temp = curr.next       # Store next node to relocate
        curr.next = temp.next  # Detach temp
        temp.next = prev.next  # Insert temp at front of sublist
        prev.next = temp       # Reconnect prev to new front

    # 4) Return the real head (skip dummy)
    return dummy.next               # Return head of modified list







# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Reverse nodes in a singly linked list from position left to right and return the modified list.
# Example: head = [1, 2, 3, 4, 5], left = 2, right = 4 → Output = [1, 4, 3, 2, 5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):  # Example: head = 1->2->3->4->5, left = 2, right = 4

    # 0️⃣ Early exit — empty list or no-op range
    # Check if list is empty or left equals right
    # Why? No reversal is needed if list is empty or range is a single node
    if not head or left == right:  # head exists, left = 2, right = 4, 2 == 4 is false, proceed
        return head  # skip

    # 1️⃣ Setup — add dummy before head; start prev at dummy
    # Create a dummy node pointing to head
    # Why? Simplifies handling edge cases, like reversing from the head
    dummy = ListNode(-1)  # dummy = -1->None
    dummy.next = head     # dummy = -1->1->2->3->4->5
    prev = dummy          # prev points to dummy (-1)

    # 2️⃣ Move prev to the node BEFORE position 'left'
    # Move prev left-1 steps to reach the node before position left
    # Why? We need to connect prev to the reversed sublist
    for _ in range(left - 1):  # left = 2, range(2-1) = [0], 1 iteration
        prev = prev.next       # prev = dummy.next = 1
    # After loop: prev points to node 1
    curr = prev.next           # curr points to node 2 (position left = 2)
    # After setup: prev = 1, curr = 2, list = -1->1->2->3->4->5

    # 3️⃣ Reverse by repeatedly moving curr.next to the FRONT of the sublist
    # Reverse right-left times to cover the sublist
    # Why? We move nodes one by one to the front of the sublist to reverse it
    for _ in range(right - left):  # right = 4, left = 2, range(4-2) = [0, 1], 2 iterations
        # --- Iteration 1 ---
        # Store the next node to relocate
        temp = curr.next      # curr = 2, temp = 3
        # Detach temp from the list
        curr.next = temp.next # curr.next = 3.next = 4, list = -1->1->2->4->5
        # Insert temp at the front of the sublist (after prev)
        temp.next = prev.next # temp = 3, prev.next = 2, 3.next = 2
        prev.next = temp      # prev.next = 3, list = -1->1->3->2->4->5
        # After Iteration 1: prev = 1, curr = 2, list = -1->1->3->2->4->5

        # --- Iteration 2 ---
        if _ == 1:
            temp = curr.next      # curr = 2, temp = 4
            curr.next = temp.next # curr.next = 4.next = 5, list = -1->1->3->2->5
            temp.next = prev.next # temp = 4, prev.next = 3, 4.next = 3
            prev.next = temp      # prev.next = 4, list = -1->1->4->3->2->5
        # After Iteration 2: prev = 1, curr = 2, list = -1->1->4->3->2->5

    # 4️⃣ Return the real head (skip dummy)
    # Why? The list is modified, and we return the head after the dummy
    return dummy.next  # dummy.next = 1->4->3->2->5


# Helper to convert linked list to Python list for easy printing
def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# Test the function
a = ListNode(1); b = ListNode(2); c = ListNode(3)
d = ListNode(4); e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

result = reverseBetween(a, 2, 4)
print(to_list(result))  # Output: [1, 4, 3, 2, 5]









# --------------------------------------------
# 2) Two-phase with a standard in-place reversal loop — most explicit/teachable
def reverseBetween(head, left, right):
    if left == right:
        return head

    dummy = ListNode(0, head)
    left_prev = dummy

    # 1) find left_prev (node before left) and left_node (at left)
    for _ in range(left - 1):
        left_prev = left_prev.next
    left_node = left_prev.next

    # 2) reverse from left to right using standard prev/curr loop
    prev = None
    curr = left_node
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # 3) reconnect: left_prev -> (reversed head 'prev'), and tail -> curr
    left_prev.next = prev
    left_node.next = curr

    return dummy.next





# --------------------------------------------
# 3) Grok: Two-phase with a standard in-place reversal loop 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head
    
    # Reach node at position left
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    
    # Reverse sublist from left to right
    curr = prev.next
    for _ in range(right - left):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next




# --------------------------------------------
# 4) Approach: Recursion
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head