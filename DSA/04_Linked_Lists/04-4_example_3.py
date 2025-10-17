# FIND THE KTH NODE FROM THE END OF A LINKED LIST

# Example 3: Given the head of a linked list and an integer k, return the kth node from the end.

# For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.


# FIND THE KTH NODE FROM THE END OF A LINKED LIST
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# --------------------------------------------
# ✅ EXAMPLE 1: Linked list: 1 → 2 → 3 → 4 → 5
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
k = 2
node = find_node(a, k)
print(node.val)
# Output: 4


"""
Time: O(N)
  - Let N = number of nodes in the linked list.
  - Step 1: Move the fast pointer k steps ahead → O(k).
  - Step 2: Move both slow and fast pointers together until fast reaches the end → O(N - k).
  - Each node is visited at most once.
  - Overall: O(N).

Space: O(1)
  - Only two pointers (slow, fast) and a loop counter are used.
  - No additional data structures are required.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Two-pointer traversal ensures only one full pass through the list.

Space: O(1)
  - Constant space for two pointers.


  
---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5], k = 2

Step 1: Advance fast pointer k steps
i   | fast.val
----|---------
0   | 2
1   | 3

Step 2: Move slow and fast pointers until fast reaches end
slow.val | fast.val | fast exists
---------|----------|------------
2        | 3        | True
3        | 4        | True
4        | 5        | True
4        | None     | False

Final: 4 (slow.val)


---
Overview for Each Iteration
Input: head = [1, 2, 3, 4, 5], k = 3

Step 1: Advance fast pointer k steps
i   | fast.val
----|---------
0   | 2
1   | 3
2   | 4

Step 2: Move slow and fast pointers until fast reaches end
slow.val | fast.val | fast exists
---------|----------|------------
2        | 5        | True
3        | None     | False

Final: 3 (slow.val)






---
📘 Explanation: for _ in range(k)

- `range(k)` → creates a sequence of numbers from 0 up to (but not including) k.
  Example: if k = 2 → range(k) = [0, 1]

- The loop `for _ in range(k):` → repeats the next line(s) k times.

- The underscore `_` means “I don't care about this variable.”
  It's a common Python convention when the loop variable isn't used.

In this problem's context:
    for _ in range(k):
        fast = fast.next

- It moves the `fast` pointer forward k times.
- Purpose: to position `fast` k nodes ahead of `slow`
  so when `fast` reaches the end, `slow` will be at the kth node from the end.



"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def find_node(head, k):
    slow = head               # Slow pointer starts at head
    fast = head               # Fast pointer starts at head
    
    for _ in range(k):        # Move fast k steps ahead
        fast = fast.next      # Advance fast pointer

    while fast:               # Move both until fast reaches end
        slow = slow.next      # Advance slow pointer
        fast = fast.next      # Advance fast pointer
    return slow               # Slow is at kth node from end