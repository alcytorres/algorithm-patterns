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

# ––––––––––––––––––––––––––––––––––––––––––––––– 
# Approach 1: Swap Nodes in Pairs (Dummy Node Version)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # Dummy node acts as the prevNode for the head node
    # of the list and hence stores pointer to the head node.
    dummy = ListNode(-1)
    dummy.next = head

    prev_node = dummy

    while head and head.next:

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Reinitializing the head and prev_node for next swap
        prev_node = first_node
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
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
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
