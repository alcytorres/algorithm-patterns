"""
============================
Simple LINKED LIST — RECAP
============================
"""

class ListNode:
    def __init__(self, val):
        self.val = val      # store this node’s value
        self.next = None    # start unlinked; will later point to next node

# Build nodes
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

"""
🧩 Overview — Node Creation
-----------------------------------------
| Step | Code Line          | Node(s) Affected | val | next (points to) | 
|------|--------------------|------------------|-----|------------------|
| 1    | one = ListNode(1)  | one              | 1   | None             | 
| 2    | two = ListNode(2)  | two              | 2   | None             |
| 3    | three = ListNode(3)| three            | 3   | None             |

Summary:
    Step 1: Created node one with value 1; not linked yet 
    Step 2: Created node two with value 2; not linked yet 
    Step 3: Created node three with value 3; not linked yet 


📦 Visual Diagram (mental picture)
----------------------------------
[1]    [2]    [3]
 ↓      ↓      ↓
None   None   None

💡 Explanation:
    • Three separate nodes created (one, two, three).
    • Each has a value (1, 2, 3) 
    • None are linked yet since their .next pointer still point to None.

    • [1], [2], and [3] are independent boxes, not connected yet - just isolated boxes.

"""



"""
============================
FULL LINKED LIST — RECAP GUIDE
============================

🧠 Big picture: What's going on here?
------------------------------------
A linked list is a chain of boxes (nodes).
Each node stores:
  • a value (data)
  • a link (pointer) to the next node

Instead of being side by side like an array, nodes can live anywhere in memory and just point to the next one.
"""

class ListNode:
    def __init__(self, val):
        self.val = val      # store this node’s value
        self.next = None    # start unlinked; will later point to next node

# Build nodes
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

# Link them together
one.next = two
two.next = three

# Mark the start of the list
head = one

print(head.val)            # 1
print(head.next.val)       # 2
print(head.next.next.val)  # 3


"""
🧩 Overview — Node Creation & Pointer Linking
-----------------------------------------
| Step | Code Line          | Node(s) Affected | val | next (points to) | 
|------|--------------------|------------------|-----|------------------|
| 1    | one = ListNode(1)  | one              | 1   | None             | 
| 2    | two = ListNode(2)  | two              | 2   | None             |
| 3    | three = ListNode(3)| three            | 3   | None             |
| 4    | one.next = two     | one              | 1   | two              | 
| 5    | two.next = three   | two              | 2   | three            | 
| 6    | head = one         | head pointer     | -   | one              | 

Summary:
    Step 1: Created node one with value 1; not linked yet 
    Step 2: Created node two with value 2; not linked yet 
    Step 3: Created node three with value 3; not linked yet 
    Step 4: Linked node one to node two 
    Step 5: Linked node two to node three
    Step 6: head points to the first node (one)

    * Note the last node (three) still points to None

✅ Final chain: head → [1] → [2] → [3] → None


Summary:
    • Each node stores a value (val) and a pointer (next).
    • We create nodes first, then connect them by updating .next.
    • head is just a reference to the start of the chain.
"""


"""
📦 Visual Diagram (mental picture)
----------------------------------
head
 ↓
[1] → [2] → [3] → None

- head points to the first node.
- each .next points to the next node in the chain.
- the last node points to None (end).
"""

print(head.val)            # 1
print(head.next.val)       # 2
print(head.next.next.val)  # 3


"""
🔁 Why this pattern exists
--------------------------
Arrays store elements contiguously in memory.
Linked lists use pointers so elements can live anywhere.

Trade-offs:
  • Fast insertion/deletion (just relink pointers)
  • Slower lookup (must walk node by node)


💡 Memory Hook
--------------
“Each node is like a box that says:
    'Here's my value, and here's where the next box lives.'”


Recent Q&A Highlights
---------------------
Q: Why does this work?
   one.next = two
   two.next = three
   head = one

A: `next` is not a keyword — it's just an attribute.
    • You're storing a reference to another object,
    • literally linking them together.
    • head = one simply marks where the chain begins.

Q: Is this only used in linked lists?
    • A: No — similar idea appears in trees (left/right), graphs (neighbors), or object chains (next_page).

Q: Do you need 'head'?
    • A: Not strictly here, but yes in real use.
    • It's a best practice to keep a reference
    • to the first node so you don't lose the list.
"""


# ----------------------------------------------
"""
============================
MECHANICS OF A LINKED LIST
============================

🧠 Big Picture
--------------
A linked list is made of nodes connected by pointers (.next).
To use or modify one, you move these pointers carefully.

Understanding how pointers and assignments work
is key to manipulating linked lists correctly.
"""


# ----------------------------
# 📘 Assignment (=)
# ----------------------------
"""
When you assign one variable to another, both point
to the same node in memory.

Example:
    ptr = head        # ptr now points to the same node as head
    head = head.next  # move head forward one node
    head = None       # head is now empty

💡 Key idea:
    'ptr' still points to the original head.
    Variables only change if you reassign them (ptr = something).
"""

# Visualization:
# Before:
#   head → [1] → [2] → [3]

# After `head = head.next`:
#   ptr → [1] → [2] → [3]
#   head → [2] → [3]

# After `head = None`:
#   ptr → [1] → [2] → [3]
#   head → None


"""
In C/C++, you have to manually use pointers — you see symbols like `*` and `&` to control memory directly.

In Python, you don't see those — but it still works like pointers behind the scenes.

When you assign one variable to another (like `ptr = head`),
both now refer to the same object in memory — just like pointers would.

💡 Think of it like this:
    • Python automatically handles the “pointer stuff” for you — every object variable is really just a reference to something in memory.

"""


# ----------------------------
# 🔗 Chaining .next
# ----------------------------
"""
Each '.next' means “go one step forward.”

Given 1 → 2 → 3:
  head           → node 1
  head.next      → node 2
  head.next.next → node 3

So when you write head.next.next,
you're really saying: “go to node 2's next (which is node 3).”

💡 Rule of thumb:
    • Everything before the final .next refers to the node whose .next you're accessing.
"""


# ----------------------------
# 🔁 Traversal (Iterating)
# ----------------------------
"""
To walk through the list (visit each node):
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    # Traversal (Iterating)
    def get_sum(head):
        ans = 0
        while head:
            ans += head.val
            head = head.next  # move forward one node
        return ans

# Build nodes
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
# Link them together
one.next = two
two.next = three
# Mark the start of the list
head = one

result = ListNode.get_sum(head)
print(result)  # Output: 6

"""
🧩 Overview — Traversal (Iterating)
------------------------------
Input: head → [1 → 2 → 3]

| Step | head.val  | ans (running total) | head (after move) |
|------|-----------|---------------------|-------------------|
| -    | -         | 0                   | 1 → 2 → 3         |
| 1    | 1         | 1 (0+1)             | 2 → 3             |
| 2    | 2         | 3 (1+2)             | 3                 |
| 3    | 3         | 6 (3+3)             | None              |


Summary:
    • Start with head at first node (value 1)
    • Add each node's value to ans
    • Stop when head becomes None

✅ Final: ans = 6


💡 Explanation:
    • The loop `while head:` runs as long as head isn't None.
    • Each iteration visits one node, adds its value, then moves forward.
    • `head = head.next` means "step to the next node."
    • When head becomes None, loop ends and returns ans. This happens at the last node since its .next is None.


    • Think of `head = head.next` as “move to the next train car.”

    

Truthy vs Falsy in Loops
    • In Python, 'while head:' keeps looping as long as head is truthy.
    • When head becomes None (which is falsy), the loop stops.

    • Falsy values include: None, False, 0, '', [], {}, set().
    • Everything else is truthy.

"""


# ----------------------------
# 🔂 Recursive Traversal
# ----------------------------
"""
You can also do the same thing recursively:
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    # Recursive Traversal
    def get_sum_recursive(head):
        if not head:
            return 0
        return head.val + ListNode.get_sum_recursive(head.next)

# Build nodes
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
# Link them together
one.next = two
two.next = three
# Mark the start of the list
head = one

result = ListNode.get_sum(head)
print(result)  # Output: 6


"""
🧩 Overview — Recursive Traversal
| Step | head.val  | What happens                        | Returned to caller            
|------|-----------|-------------------------------------|-------------------|
| 1    | 1         | return 1 + get_sum_recursive([2])   | waits              
| 2    | 2         | return 2 + get_sum_recursive([3])   | waits              
| 3    | 3         | return 3 + get_sum_recursive(None)  | waits              
| 4    | None      | if not head → return 0              | 0                  
| 5    | 3         | 3 + 0 = 3                           | 3                  
| 6    | 2         | 2 + 3 = 5                           | 5                  
| 7    | 1         | 1 + 5 = 6                           | 6                  

Explanation
    Step 1: Calls itself for the rest of the list     
    Step 2: Calls itself again for the next node      
    Step 3: Calls one more time with None (end)        
    Step 4: Base case: no node → return 0             
    Step 5: Adds own value + result from next (0)     
    Step 6: Adds own value + result from next (3)    
    Step 7: Adds own value + result from next (5)   

✅ Final: ans = 6

Summary:
    • Each call handles one node.
    • Adds current node's value + sum of the rest.
    • When head is None, returns 0 (base case).
    • Results bubble back up: 3 → 5 → 6


Q: Why do we add 0 to 3 in step 5? 
    • The 0 comes from the base case (no nodes left).
    • It's the return value of ListNode.get_sum(head.next) when head.next is None.



🧩 Step-by-Step Walkthrough — Recursion in get_sum_recursive
------------------------------------------------------------
We're using recursion to add up the values of this linked list:
[1] → [2] → [3] → None

Goal: Understand what happens in memory as Python runs this code.

"""

# Step 1 – First call (head = [1])
"""
• head is not None → skip 'if not head'
• Return line runs:  return 1 + get_sum_recursive(head.next)
• head.next points to [2]
• So Python must call get_sum_recursive([2]) to find that value.
⚙️ This first call is now “paused” — waiting for the next one to finish.
"""

# Step 2 – Second call (head = [2])
"""
• head is not None
• Return line:  return 2 + get_sum_recursive(head.next)
• head.next points to [3]
• So it calls get_sum_recursive([3])
⚙️ This call also pauses until it knows what get_sum_recursive([3]) returns.
"""

# Step 3 – Third call (head = [3])
"""
• head is not None
• Return line:  return 3 + get_sum_recursive(head.next)
• head.next is None
• So it calls get_sum_recursive(None)
⚙️ This one also pauses, waiting for that last call.
"""

# Step 4 – Fourth call (head = None)
"""
• if not head → True
• So we return 0
✅ This is the BASE CASE — it stops the recursion.
Now Python finally has a number to send back up.
"""

# Step 5 – Return back to third call (head = 3)
"""
• The “waiting” call from Step 3 gets the 0
• It now finishes:  return 3 + 0 = 3
• Sends 3 back up to Step 2
"""

# Step 6 – Return back to second call (head = 2)
"""
• The “waiting” call from Step 2 gets 3
• It now finishes:  return 2 + 3 = 5
• Sends 5 back up to Step 1
"""

# Step 7 – Return back to first call (head = 1)
"""
• The “waiting” call from Step 1 gets 5
• It now finishes:  return 1 + 5 = 6
✅ Final result: 6
"""

"""
💡 Mental Picture
-----------------
Going down:
    (1 waits for 2)
    (2 waits for 3)
    (3 waits for None)

Coming back up:
    3 + 0 = 3
    2 + 3 = 5
    1 + 5 = 6

✅ Final Answer: 6


🧠 Understanding Recursion (Like You're 10)
------------------------------------------
We have boxes (nodes) in a line:
[1] → [2] → [3] → None

Each box knows:
  - its number (val)
  - the next box (next)


How it works:
-------------
    1. If there are no boxes left (head = None) → return 0
    2. Otherwise → take my value + the sum of everything after me.


"""


# ----------------------------
# 🧩 TL;DR CHEAT SHEET
# ----------------------------
"""
- Assignment (=):
  Moves or copies references — doesn't duplicate nodes.
  ptr = head → both point to the same node.

- .next:
  Jumps one node forward. head.next.next = “2 steps forward.”

- Traversal:
  Use a loop or recursion to move through all nodes.

- Stop condition:
  When node.next is None → end of list.

- Analogy:
  Each node is a train car. .next is the coupler.
  Moving head = head.next means stepping into the next car.
"""


"""
💡 Summary (memorize this)
    • .next stores a reference to the next node.

    • head = head.next means “move my pointer one step forward.”

    • That's how you traverse a linked list — follow each .next until it's None.

When .next is None, it means there's no more node — end of the list.

"""


# FINAL SUMMARY

# ----------------------------
# 🔁 Traversal (Iterating)
# ----------------------------
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    
    return ans

result = get_sum(head)
print(result)  # Output: 6

# ----------------------------
# 🔂 Recursive Traversal
# ----------------------------
def get_sum(head):
    if not head:
        return 0
    
    return head.val + get_sum(head.next)

result = get_sum(head)
print(result)  # Output: 6




"""
============================
TYPES OF LINKED LISTS
============================

🧩 Singly Linked List — The Standard Type
-----------------------------------------
This is the type we've been working with so far.

Each node has:
  • a value (val)
  • a pointer to the next node (.next)

That means we can only move FORWARD through the list.
There are no links pointing backward.
"""

class ListNode:
    def __init__(self, val):
        self.val  = val
        self.next = None

"""
📦 Visual Diagram (mental picture)
----------------------------------
head
 ↓
[1] → [2] → [3] → None

- Each node points only to the next node.
- No “previous” link exists.
- Traversal moves one way → forward only.
"""

# ----------------------------------------------
# Singly Linked List: Insert & Delete a node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Delete the node right after prev_node
def delete_node(prev_node):
    prev_node.next = prev_node.next.next

# Example: Insert 99 after 1 in list [1 → 2 → 3] → [1 → 99 → 2 → 3]
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

# Link them: a → b → c
a.next = b
b.next = c

# Create a new node
x = ListNode(99)

# --------------------------------------------
# Insert x after a (so list becomes: 1 → 99 → 2 → 3)
add_node(a, x)

# Print the full list to verify
print("Forward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next
# Output: 1  99  2  3

# --------------------------------------------
# Delete node after 'a' (this removes node 99)
delete_node(a)

# Print the list after deletion
print("Forward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next
# Output: 1  2  3


# ----------------------------
# ➕ Inserting a Node
# ----------------------------
"""
Let's say you want to insert a new node so it becomes the element at position i.

You need a pointer to the node currently at position (i - 1).
  • We'll call it prev_node.

Steps:
  1️⃣ Point the new node's .next to the node after prev_node.
  2️⃣ Then make prev_node's .next point to the new node.
"""

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

"""
📊 Example:
Original chain:  [1] → [2] → [3] → None

Insert [99] after [1]:
  node_to_add = [99]
  prev_node = [1]

After:
  [1] → [99] → [2] → [3] → None

🧠 Time Complexity:
  • O(1) if you already have prev_node
  • O(n) if you must iterate from head to find it
"""


# ----------------------------
# ➖ Deleting a Node
# ----------------------------
"""
To delete the node at position i, you also need a pointer to the node at position (i - 1).

Steps:
  1️⃣ Skip the unwanted node by changing pointers.
  2️⃣ prev_node.next should now point to prev_node.next.next
"""

# Delete the node right after prev_node
def delete_node(prev_node):
    prev_node.next = prev_node.next.next

"""
📊 Example:
Original chain:  [1] → [99] → [2] → [3] → None

Delete [99]:
  prev_node = [1]

After:
  [1] → [2] → [3] → None

💡 What happened:
  • prev_node.next (which was [99]) got replaced by [99].next (which is [2])
  • Node [99] is no longer connected → effectively removed

🧠 Time Complexity:
  • O(1) if you already have prev_node
  • O(n) if you must iterate from head to reach it


✅ Recap — Singly Linked List
-----------------------------
- Each node only points forward (via .next).
- You can traverse only in one direction.
- Insertion and deletion are O(1) **if** you already know where to do it.
- Otherwise, finding the spot to insert/delete is O(n).

💡 Memory Hook:
  • “Each node says: 'Here's my value — and here's who comes next.’”


  

============================
DOUBLY LINKED LIST — RECAP
============================

🧠 Big Picture
--------------
Like a singly list, but each node has:
  • val
  • next  → who comes after me
  • prev  → who comes before me

This lets you iterate in BOTH directions.
"""

class ListNode:
    def __init__(self, val):
        self.val  = val
        self.next = None
        self.prev = None

"""
📦 Visual Diagram (mental picture)
----------------------------------
head                         tail
 ↓                            ↓
[1] ⇄ [2] ⇄ [3] ⇄ [4] ⇄ None

- Each node points forward (.next) and backward (.prev).
- You can move left or right across the chain.
"""


# ----------------------------------------------
# Doubly linked list: Insert & Delete a node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node


# Example setup: 1 ⇄ 2 ⇄ 3
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

# Link them together
a.next = b
b.prev = a
b.next = c
c.prev = b

# --------------------------------------------
# ✅ Insert a new node (99) BEFORE node c
x = ListNode(99)
add_node(c, x)
# List becomes: 1 ⇄ 2 ⇄ 99 ⇄ 3

# Print the list forward
print("Forward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next


# --------------------------------------------
# ✅ Delete node b (value = 2)
delete_node(b)
# List becomes: 1 ⇄ 99 ⇄ 3

# Print the list forward
print("\nForward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next  # 1 ⇄ 99 ⇄ 3

# Print the list backward
print("Backward:")
curr = c
while curr:
    print(curr.val)
    curr = curr.prev  # 3 ⇄ 99 ⇄ 1


# ----------------------------
# ➕ Inserting BEFORE a node at position i
# ----------------------------
"""
You only need a reference to the node AT position i (call it 'node').
  • We'll insert 'node_to_add' BEFORE it.

Steps (update 4 pointers total):
  1) prev_node = node.prev
  2) node_to_add.next = node
  3) node_to_add.prev = prev_node
  4) prev_node.next = node_to_add
  5) node.prev = node_to_add
"""

def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

"""
📊 Example:
Original:  [1] ⇄ [2] ⇄ [3]
Insert [99] before [3] (node = [3]):

After:     [1] ⇄ [2] ⇄ [99] ⇄ [3]

🧠 Why we don't need (i - 1):
- In a singly list, you needed the previous node.
- Here, you can get it with node.prev.
- Same O(1) insert once you have 'node'.
"""


# ----------------------------
# ➖ Deleting the node at position i
# ----------------------------
"""
Given a reference to the node AT i (call it 'node'), unlink it.

Steps (update 2 neighbor pointers + conceptually drop 'node'):
  1) prev_node = node.prev
  2) next_node = node.next
  3) prev_node.next = next_node
  4) next_node.prev = prev_node
"""

def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

"""
📊 Example:
Original:  [1] ⇄ [2] ⇄ [99] ⇄ [3]
Delete [2] (node = [2]):

After:     [1] ⇄ [99] ⇄ [3]

💡 What happened:
- We “bridged around” [2] by connecting its neighbors.
- [2] has no incoming links now → effectively removed.
"""


# ----------------------------
# 🔁 Traversal (both ways)
# ----------------------------

# Forward:
curr = a
while curr:
    print(curr.val)
    curr = curr.next  # 1 ⇄ 99 ⇄ 3

# Backward:
curr = c
while curr:
    print(curr.val)
    curr = curr.prev  # 3 ⇄ 99 ⇄ 1


# ----------------------------
# ⚠️ Edge Cases (important)
# ----------------------------
"""
- Inserting at the HEAD:
    • prev_node is None — set new_node.prev = None and update head.
- Inserting at the TAIL:
    • node is None if appending after tail — handle separately.
- Deleting the HEAD:
    • After removal, new head.prev must be None.
- Deleting the TAIL:
    • After removal, new tail.next must be None.

Rule of thumb: In DLL ops, you usually touch FOUR pointers.
  • Miss one → bugs.
"""


# ----------------------------
# ⏱️ Complexity
# ----------------------------
"""
- Once you have 'node' (position i):
    • Insert/delete: O(1)
- If you must find position i first:
    • O(n) traversal from head or tail

Tip: DLLs are great when you frequently insert/remove in the middle and need to move in both directions.


💡 Memory Hook
--------------
“Each node knows its neighbor on BOTH sides:
  • 'Here's who's next, and here's who came before.’”
"""












# ----------------------------------------------
# Linked lists with sentinel nodes
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head



# ----------------------------------------------
# Dummy pointers
# Simple singly linked list node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_sum(head):
    ans = 0
    dummy = head
    while dummy:
        ans += dummy.val
        dummy = dummy.next
    
    # same as before, but we still have a pointer at the head
    return ans

# Example: create a linked list 1 → 2 → 3
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

# Print total sum
result = get_sum(a)
print(result)  # Output: 6









