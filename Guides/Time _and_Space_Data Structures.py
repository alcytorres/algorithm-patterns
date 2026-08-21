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
HIDDEN COSTS — one-liners that LOOK O(1) but are not
================================================================================
These are the lines that make a "linear looking" loop secretly quadratic.
If any of these sits inside a loop, the loop is NOT O(N).

Line of code            | Real cost   | Why
------------------------|-------------|--------------------------------------
x in some_list          | O(N)        | scans element by element
some_list.remove(x)     | O(N)        | finds it, then shifts everything after
some_list.index(x)      | O(N)        | scans element by element
some_list.pop(0)        | O(N)        | shifts every remaining element left
some_list.insert(0, x)  | O(N)        | shifts every element right
s = c + s   (in a loop) | O(N)        | strings are immutable → new string
s[i:j]      (slice)     | O(K)        | copies K characters
sorted(x) / x.sort()    | O(N log N)  | full sort
max/min/sum(collection) | O(N)        | one full pass
list(x) / x.copy()      | O(N)        | copies N elements
del some_list[i]        | O(N)        | shifts everything after i

Safe inside a loop (truly O(1)):
    x in some_set / some_dict     → hash lookup
    some_dict[k] / count[c] += 1  → hash lookup
    some_list[i]                  → index math
    some_list.append(x)           → amortized O(1)
    some_list.pop()               → from the END only
    left += 1, right -= 1         → integer math

The check: for each line in the loop body, ask "does this line touch every
element?" If yes, multiply its cost by the number of iterations.

  loop iterations × work inside one iteration = total time

Example: `for c in t:` with `c not in available` and `available.remove(c)` inside
  → O(N) iterations × (O(N) + O(N)) = O(N²), even though nothing looks nested.

================================================================================
PART 2 — CONSTRAINTS → WHAT COMPLEXITY IS ALLOWED
================================================================================
Read n from Constraints. Compare n² to ~10 million. That one check
tells you whether nested loops are legal.

The budget (Python / LeetCode):
  ~10 million operations (10⁷) is a safe personal budget.
  Interviewers often say 10⁸. Same idea, slightly looser.
  If your algorithm does more than that at worst-case n, it will TLE.

The 10-second check:
  1. Look at the largest n.
  2. Square it (or picture n × n).
  3. Is that bigger than 10 million?
       YES → nested loops (O(n²)) are out. Need O(n) or O(n log n).
       NO  → O(n²) is allowed. Don't panic-optimize past it.

────────────────────────────────────────────────────────────────────────────────
n (max)        | n²                    | Allowed time          | Typical tell
---------------|-----------------------|-----------------------|----------------
≤ 20           | tiny                  | O(2^n) ok             | subsets / backtracking
≤ 100          | 10,000                | O(n³) sometimes       | rare at entry-level
≤ 3,000        | 9 million (9×10⁶)     | O(n²) allowed         | 3Sum-style (n=3000)
≤ 10⁴          | 100 million (10⁸)     | O(n²) too slow        | need O(n log n) or O(n)
≤ 10⁵          | 10 billion (10¹⁰)     | O(n) or O(n log n)    | most array problems
≤ 10⁶          | huge                  | O(n)                  | n log n may TLE in Python
≥ 10⁹          | impossible            | O(log n) or O(1)      | binary search / math
────────────────────────────────────────────────────────────────────────────────

Worked in one line:
  n = 10⁵ → (10⁵)² = 10 billion. Nested loops die. Sort + scan (O(n log n))
             is ~100,000 × 17 ≈ 1.7 million — well under 10 million. Allowed.
  n = 3000 → 3000² = 9 million. Nested two-pointer (O(n²)) is allowed.

Space (even simpler):
  O(N) extra  → almost always fine (a dict, a result list).
  O(N²) extra → only if n is small (a few hundred).
  O(1) extra  → only chase this when the problem asks, or when they
                already sorted the input for you (that's a hint).



================================================================================
PART 3 — WHY (short explanations)
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
  • First: look at n (PART 2). If n² > 10 million, nested loops are out.
  • A loop is only O(N) if EVERY line inside it is O(1) — check Hidden Costs above.
  • "in list" → O(N).  "in set" / "in dict" → O(1) avg.
  • Need fast lookup? → dict or set.
  • Need fast ends insert/delete? → deque.
  • Need always-min / always-max? → heapq.
  • Need index access? → list.
  • Worst O(N) for hash structures is collision edge case — still say O(1) avg in interviews.

"""