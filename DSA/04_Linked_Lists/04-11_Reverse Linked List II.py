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
    if left == right: 
        return head

    dummy = ListNode(0, head)
    prev = dummy

    # 1) move prev to node BEFORE 'left'
    for _ in range(left - 1):
        prev = prev.next

    # 2) reverse by repeatedly moving the node after 'curr' to the front
    curr = prev.next
    for _ in range(right - left):
        nxt = curr.next           # node to relocate
        curr.next = nxt.next      # detach nxt
        nxt.next = prev.next      # put nxt at front of the sublist
        prev.next = nxt           # reconnect front

    return dummy.next



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
# Grok Solution
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
# Approach 1: Recursion
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




# --------------------------------------------
# Approach 2: Iterative Link Reversal.
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head