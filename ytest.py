class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

# Display a doubly linked list as a string (e.g., '3 <-> 1 <-> 7'). O(n)
def display(head):
    if not head:
        return "Empty List"
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    return " <-> ".join(elements)

# Inserts a node at the beginning of a doubly linked list. O(1)
def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    new_node.next = head
    head.prev = new_node
    return new_node, tail

# Inserts a node at the end of a doubly linked list. O(1)
def insert_at_end(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node


# Example Usage

# Creates single node with value 1 (head and tail are same).
head = tail = DoublyNode(1)

# Display initial list state
print("Initial list:", display(head))  # Output: 1
# Insert 3 at the beginning: 3 <-> 1
head, tail = insert_at_beginning(head, tail, 3)
print("After inserting 3 at beginning:", display(head))  # Output: 3 <-> 1
# Insert 7 at the end: 3 <-> 1 <-> 7
head, tail = insert_at_end(head, tail, 7)
print("After inserting 7 at end:", display(head))  # Output: 3 <-> 1 <-> 7



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# # Get List Length
def get_length(head):
    count = 0          # Initialize counter
    curr = head        # Start at head
    while curr:        # Traverse until None
        count += 1     # Increment for each node
        curr = curr.next  # Move to next node
    return count       # Return total nodes

# Test get_length
print("List length:", get_length(head))  # Output: 3 (for 3 <-> 1 <-> 7)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Check if Value Exists
def has_value(head, value):
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
    return False

# Test has_value
print("Has value 1:", has_value(head, 1))  # Output: True
print("Has value 5:", has_value(head, 5))  # Output: False