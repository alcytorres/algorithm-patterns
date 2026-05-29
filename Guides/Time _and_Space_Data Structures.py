


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Python Data Structures — Time & Space Cheat Sheet (LeetCode / Entry Level)


"""
================================================================================
PART 1 — QUICK REFERENCE (scan this in interviews)
================================================================================

Legend:  Avg = average case  |  Worst = worst case  |  Space = worst-case space
         — = not typical / N/A for that structure

────────────────────────────────────────────────────────────────────────────────
LIST (dynamic array) — Python: []
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Access by index | O(1)        | O(1)         | —
Search (in x)   | O(N)        | O(N)         | —
Insert (append) | O(1)*       | O(N)         | O(N)†
Insert (index)  | O(N)        | O(N)         | O(N)†
Delete (pop)    | O(1)        | O(1)         | —
Delete (index)  | O(N)        | O(N)         | —

* Amortized O(1) for append. Worst O(N) when array must resize.
† O(N) extra space only if you create a new list; in-place uses O(1) extra.

────────────────────────────────────────────────────────────────────────────────
DICT (hash map) — Python: {}
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Access / Get    | O(1)        | O(N)         | O(N)
Search (in x)   | O(1)        | O(N)         | O(N)
Insert / Set    | O(1)        | O(N)         | O(N)
Delete          | O(1)        | O(N)         | O(N)

────────────────────────────────────────────────────────────────────────────────
SET (hash set) — Python: set()
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Search (in x)   | O(1)        | O(N)         | O(N)
Insert (add)    | O(1)        | O(N)         | O(N)
Delete (remove) | O(1)        | O(N)         | O(N)
Access by index | —           | —            | —

────────────────────────────────────────────────────────────────────────────────
DEQUE (double-ended queue) — Python: collections.deque
────────────────────────────────────────────────────────────────────────────────
Operation           | Time (Avg)  | Time (Worst) | Space (Worst)
--------------------|-------------|--------------|---------------
Access (ends)       | O(1)        | O(1)         | O(N)
Search (in x)       | O(N)        | O(N)         | O(N)
Insert (append/     | O(1)        | O(1)         | O(N)
  appendleft)       |             |              |
Delete (pop/        | O(1)        | O(1)         | —
  popleft)          |             |              |
Access by index     | O(N)        | O(N)         | —

────────────────────────────────────────────────────────────────────────────────
HEAP (min-heap) — Python: heapq on a list
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Peek (min)      | O(1)        | O(1)         | O(N)
Insert (heappush)| O(log N)   | O(log N)     | O(N)
Delete min      | O(log N)    | O(log N)    | —
Search (in x)   | O(N)        | O(N)         | O(N)
Build heap      | O(N)        | O(N)         | O(N)

────────────────────────────────────────────────────────────────────────────────
STACK — Python: list used as stack (append / pop)
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Push (append)   | O(1)*       | O(N)         | O(N)
Pop (pop)       | O(1)        | O(1)         | —
Peek (top)      | O(1)        | O(1)         | —
Search          | O(N)        | O(N)         | O(N)

────────────────────────────────────────────────────────────────────────────────
QUEUE — Python: collections.deque (append + popleft)
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Enqueue         | O(1)        | O(1)         | O(N)
Dequeue         | O(1)        | O(1)         | —
Peek (front)    | O(1)        | O(1)         | —
Search          | O(N)        | O(N)         | O(N)

────────────────────────────────────────────────────────────────────────────────
STRING — Python: str (immutable)
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Access by index | O(1)        | O(1)         | —
Search (in s)   | O(N)        | O(N)         | —
Concat (+)      | O(N)        | O(N)         | O(N)
Slice           | O(K)        | O(K)         | O(K)

────────────────────────────────────────────────────────────────────────────────
SINGLY LINKED LIST — LeetCode ListNode (conceptual)
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Access (i-th)   | O(N)        | O(N)         | O(N)
Search          | O(N)        | O(N)         | O(N)
Insert (head)   | O(1)        | O(1)         | O(1) extra
Insert (tail)   | O(N)        | O(N)         | O(1) extra
Insert (middle) | O(N)        | O(N)         | O(1) extra
Delete (head)   | O(1)        | O(1)         | O(1) extra
Delete (middle) | O(N)        | O(N)         | O(1) extra

────────────────────────────────────────────────────────────────────────────────
BINARY SEARCH TREE (balanced avg / skewed worst)
────────────────────────────────────────────────────────────────────────────────
Operation       | Time (Avg)  | Time (Worst) | Space (Worst)
----------------|-------------|--------------|---------------
Search          | O(log N)    | O(N)         | O(N)
Insert          | O(log N)    | O(N)         | O(N)
Delete          | O(log N)    | O(N)         | O(N)
Access min/max  | O(log N)    | O(N)         | —

================================================================================
AT-A-GLANCE — "Which is O(1) lookup?"
================================================================================
Structure   | Search by value | Search by index/key
------------|-----------------|--------------------
List        | O(N)            | O(1) by index
Dict / Set  | O(1) avg        | Dict: O(1) by key
Deque       | O(N)            | O(N) by index (avoid)
Heap        | O(N)            | O(1) peek min only
Linked List | O(N)            | O(N) by position
BST         | O(log N) avg    | —


================================================================================
PART 2 — WHY (short explanations)
================================================================================

LIST (dynamic array)
  Access O(1):     Items sit in contiguous memory — index i = start + i × size.
  Search O(N):     No hash/index by value — must scan left to right.
  Insert append O(1)*: Usually room at end; occasionally resize → O(N).
  Insert/delete middle O(N): Must shift all elements after the index.

DICT & SET (hash table)
  Search/Insert/Delete O(1) avg: hash(value) → jump to bucket → check.
  Worst O(N):      All keys hash to same bucket (rare in practice).
  Space O(N):      Stores N key-value pairs (dict) or N values (set).
  No index access: Sets have no order; dicts use keys, not numeric index.

DEQUE (doubly linked list of blocks internally)
  Insert/delete at ends O(1): Just move front/rear pointers.
  Search O(N):     No hash — must walk through elements.
  Don't use [i] on deque — that's O(N); use popleft/append instead.

HEAP (binary heap in a list)
  Peek min O(1):   Min is always at index 0.
  Insert/delete O(log N): Bubble up or down through tree height ≈ log N.
  Search O(N):     Not a hash structure — must scan the array.
  heapq is min-heap only; no O(1) max (use negated values trick).

STACK (list as stack)
  Push/pop O(1):   Always at the end — same as list append/pop.
  Never pop(0) on a list — that's O(N); use deque for queue behavior.

QUEUE (deque)
  Enqueue O(1):    append() at rear.
  Dequeue O(1):    popleft() at front — list.pop(0) is O(N), avoid it.

STRING (immutable)
  Access O(1):     Like an array of characters.
  Concat O(N):     Must create a brand-new string each time (+ operator).
  Tip: use list of chars + "".join() for many builds → O(N) total.

SINGLY LINKED LIST
  Access O(N):     No index — start at head, walk i steps.
  Insert/delete at known node O(1): Just rewire next pointer.
  Insert/delete at position O(N): Must walk to that position first.
  Space O(N):      One node per element (value + next pointer).

BINARY SEARCH TREE
  Search O(log N) avg: Halve the search space each level (balanced tree).
  Worst O(N):      Skewed tree (all nodes on one side) → becomes a linked list.
  Python has no built-in BST — use dict for O(1) lookup or bisect for sorted list.

---
Interview tips:
  • "in list" → O(N).  "in set" / "in dict" → O(1) avg.
  • Need fast lookup? → dict or set.
  • Need fast ends insert/delete? → deque.
  • Need always-min / always-max? → heapq.
  • Need index access? → list.
  • Worst O(N) for hash structures is collision edge case — still say O(1) avg in interviews.

"""