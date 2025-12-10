# 933. Number of Recent Calls

"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:
    # RecentCounter() Initializes the counter with zero recent requests.
    # int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Solution: https://leetcode.com/problems/number-of-recent-calls/description/

Example 1:
    # Input: ["RecentCounter", "ping", "ping", "ping", "ping"]
    # [[], [1], [100], [3001], [3002]]
    # Output: [null, 1, 2, 3, 3]

    # Explanation
    # RecentCounter recentCounter = new RecentCounter();
    # recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
    # recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
    # recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
    # recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Constraints:
    # 1 <= t <= 109
    # Each test case will call ping with strictly increasing values of t.
    # At most 104 calls will be made to ping.


---
TLDR:
  • Every time you call ping(t), a new request happens at time t.
  • Your job: return how many requests happened in the last 3000 milliseconds.

How to do it:
    1) Remove timestamps older than t - 3000  
    2) Add t  
    3) The number of timestamps you have left is the answer

That's the whole problem.


---
TLDR YOU SHOULD MEMORIZE
  • The current time (like 3002) can be huge.
  • We only care about keeping timestamps within 3000 milliseconds of that time.

Meaning:
  • Keep timestamps ≥ t - 3000
  • Throw away timestamps < t - 3000


---  
SUPER SIMPLE VERSION OF THE QUESTION

You are building a counter that tracks how many “pings” (requests) happened recently.

Every time you call ping(t), it means:
    "A ping just happened at time t."

Your job:
    When ping(t) is called, return how many pings happened in the last 3000 milliseconds,
    INCLUDING the new ping at time t.

In other words:
    Count all pings where their time is between t - 3000 and t.

Important:
    • Times always increase (each t is bigger than the previous one).
    • Only pings inside the last 3000ms matter — older ones do NOT count.

Example:
    ping(1)     → only ping is at time 1                   → return 1
    ping(100)   → pings at times 1 and 100                 → return 2
    ping(3001)  → pings at 1, 100, 3001 → all in window   → return 3
    ping(3002)  → ping at 1 is now too old → remove it     → return 3

Goal:
    Build a class RecentCounter with a ping(t) function that does this.



---
Think of it like this
You have a timeline of pings.
When a new ping comes in:
    1. Remove all pings older than t - 3000.
    2. Add the new ping.
    3. Count what's left.

"""

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)

obj = RecentCounter()
print(obj.ping(1))     # 1
print(obj.ping(100))   # 2
print(obj.ping(3001))  # 3
print(obj.ping(3002))  # 3


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
Time: O(1) amortized
  - Let N be the total number of pings made so far.
  - Each ping(t):
      • Removes outdated timestamps from the front of the deque.
      • Each timestamp is added once and removed once over the whole program.
      • So all pops across all calls sum to O(N), giving O(1) amortized per call.
  - Appending t and returning queue length are O(1).
  - Overall per operation: O(1) amortized.

Space: O(N)
  - The deque stores only timestamps within the past 3000 ms.
  - In the worst case (dense pings), up to all recent pings may remain in the deque.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(1) amortized
  - Add new ping and drop old ones; each timestamp is pushed and popped once.

Space: O(N)
  - Queue holds recent timestamps within the 3000-ms window.




---
Most IMPORTANT thing to Understand:
    • Every ping(t) wants the number of requests in the last 3000 ms → the window [t-3000, t].

    • Old timestamps outside this window must be removed.

    • A queue works perfectly because timestamps arrive in increasing order — the oldest is always at the front.

---
Why this code Works:
    • Queue stores all recent timestamps.

    • For each ping(t):
        - Remove timestamps < t - 3000 (they're too old).
        - Append the new time t.
        - The queue now contains ONLY valid times → its length is the answer.

    • Efficiency:
        - Each timestamp is added once and removed once → O(1) amortized.
        - No scanning through the whole history each time.

    • Intuition: Think of a sliding 3000-ms window that moves forward with each ping — the queue holds exactly what's inside that window.

---
TLDR:
    • Maintain a queue of timestamps and drop anything older than 3000 ms — the queue size is the answer.

---
Quick Example Walkthrough:

    Calls:
        ping(1)
        ping(100)
        ping(3001)
        ping(3002)

    1) ping(1)
    Window = [1-3000, 1] = [-2999, 1]
    Queue before: []
    Remove: none
    Add 1  → [1]
    Return: 1

    2) ping(100)
    Window = [100-3000, 100] = [-2900, 100]
    Queue before: [1]
    Remove: none (1 ≥ -2900)
    Add 100 → [1, 100]
    Return: 2

    3) ping(3001)
    Window = [3001-3000, 3001] = [1, 3001]
    Queue before: [1, 100]
    Remove: none (1 ≥ 1)
    Add 3001 → [1, 100, 3001]
    Return: 3

    4) ping(3002)
    Window = [3002-3000, 3002] = [2, 3002]
    Queue before: [1, 100, 3001]
    Remove: 1 (because 1 < 2 → outside window)
    Add 3002 → [100, 3001, 3002]
    Return: 3

    Final outputs: [1, 2, 3, 3]


    


---
Q: What is the best way to build a queue in python?

    • from collections import deque

    • deque = the fast, correct way to do a queue.
    • Always use it when you need FIFO (First In, First Out).

    

---
Q: IMPORTANT: Do pings carry over between print statements?
  • YES — and this is the entire point of the problem.

  • Each call to ping(t) updates the same queue inside the same RecentCounter object.

That's why:
  • ping(1) → queue is [1]
  • ping(100) → queue is [1, 100]
  • ping(3001) → queue is [1, 100, 3001]
  • ping(3002) → queue becomes [100, 3001, 3002]

  

---
Q: Why a QUEUE, not a STACK?

Key behavior:
    • Oldest pings should be removed first (those that fall out of the left side of the window).
    • Newest pings should stay as long as they are inside the window.

That is:
    • First In → First Out  (FIFO)  → a QUEUE

A stack is:
    • Last In → First Out   (LIFO)  → would remove the newest ping first (wrong).

So we use:
    from collections import deque
    and call:
        append(t)   → enqueue (add to back)
        popleft()   → dequeue (remove from front)


        


Q; Why does it not fail with print(obj.ping(3001))?  3001 is more than 3000?
"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import deque  # Import deque for efficient append/pop from both ends
class RecentCounter:
    def __init__(self):
        self.queue = deque()      # Initialize empty deque to store ping timestamps

    def ping(self, t):
        while self.queue and self.queue[0] < t - 3000:  # While queue is not empty and oldest ping is too old
            self.queue.popleft()  # Remove the oldest ping (outside 3000ms window)
        
        self.queue.append(t)      # Add the current ping time to the end of queue
        return len(self.queue)    # Return total number of pings in last 3000ms

obj = RecentCounter()  # Create new counter; queue = []

print(obj.ping(1))     
# → t=1: queue = [1] → only 1 ping in [1-3000,1] → returns 1

print(obj.ping(100))
# → t=100: queue = [1, 100] → both in [100-3000,100] → returns 2

print(obj.ping(3001))
# → t=3001: 
#   - 1 < 3001-3000 → remove 1
#   - queue = [100, 3001] → both in [1,3001] → returns 3

print(obj.ping(3002))
# → t=3002:
#   - 100 ≥ 3002-3000 → keep 100
#   - queue = [100, 3001, 3002] → all in [2,3002] → returns 3










"""
ASCII Timeline + Animation for 933. Number of Recent Calls

Goal:
    VISUALLY understand what RecentCounter is doing
    and why we use a QUEUE with a 3000ms time window.

We'll walk through this example:

    obj = RecentCounter()
    print(obj.ping(1))     # 1
    print(obj.ping(100))   # 2
    print(obj.ping(3001))  # 3
    print(obj.ping(3002))  # 3

Each call:
    • ping(t) means: "a request happened at time t"
    • We keep only pings in [t - 3000, t]
    • We remove old pings, add t, then return how many are left


===========================================================
PART 1: Concept – The 3000 ms Sliding Window
===========================================================

Think of pings as dots on a timeline.

For each ping(t):
    1. Move current time to t
    2. Valid time range is [t - 3000, t]
    3. Remove any pings < t - 3000 (too old)
    4. Add the new ping t
    5. Count the pings that remain


===========================================================
PART 2: Step-by-Step "Animation" with Queue Contents
===========================================================

We maintain:
    queue = a FIFO list of ping times (oldest at front)


1) ping(1)
-----------

t = 1
Window = [1 - 3000, 1] = [-2999, 1]

Before:
    queue = []

No pings to remove (queue empty)

Add t = 1:
    queue = [1]

Count:
    len(queue) = 1

Printed output:
    1


2) ping(100)
-------------

t = 100
Window = [100 - 3000, 100] = [-2900, 100]

Before:
    queue = [1]

Check oldest ping: 1
    Is 1 < -2900?  → No, so we keep it

Add t = 100:
    queue = [1, 100]

Count:
    len(queue) = 2

Printed output:
    2


3) ping(3001)
--------------

t = 3001
Window = [3001 - 3000, 3001] = [1, 3001]

Before:
    queue = [1, 100]

Check oldest ping: 1
    Is 1 < 1?  → No, equal to 1, so keep

Check next: 100
    Is 100 < 1? → No, keep

Add t = 3001:
    queue = [1, 100, 3001]

Count:
    len(queue) = 3

Printed output:
    3


4) ping(3002)
--------------

t = 3002
Window = [3002 - 3000, 3002] = [2, 3002]

Before:
    queue = [1, 100, 3001]

Check oldest ping: 1
    Is 1 < 2? → Yes → too old → REMOVE it

Now:
    queue = [100, 3001]

Check new oldest: 100
    Is 100 < 2? → No → keep it

3001 is also ≥ 2 → keep it

Add t = 3002:
    queue = [100, 3001, 3002]

Count:
    len(queue) = 3

Printed output:
    3


Final outputs in order:
    [1, 2, 3, 3]


===========================================================
PART 3: ASCII Moving Timeline Animation
===========================================================

Legend:
    • ● = a ping (request)
    • Numbers under dots = time values
    • Window [L, R] = allowed time range for pings at that step
    • Anything left of L is "too old" and gets removed


1) ping(1)
-----------

Time: t = 1
Window: [1 - 3000, 1] = [-2999 .. 1]

No existing pings.

After adding ping at t = 1:

    ... -2999                          1
           |--------------------------|
                                       ●
                                      (1)

queue = [1]
Output = 1


2) ping(100)
-------------

Time: t = 100
Window: [100 - 3000, 100] = [-2900 .. 100]

Existing pings:
    ●1

Is 1 in the window [-2900, 100]?  → Yes → keep it.

Add ping at t = 100:

    ... -2900                       1                100
           |------------------------|-----------------|
                                     ●                ●
                                    (1)              (100)

queue = [1, 100]
Output = 2


3) ping(3001)
--------------

Time: t = 3001
Window: [3001 - 3000, 3001] = [1 .. 3001]

Existing pings:
    ●1, ●100

Is 1 in [1, 3001]?  → Yes (on the left edge)
Is 100 in [1, 3001]? → Yes

Add ping at t = 3001:

         1             100                      3001
         |-------------|------------------------|
         ●             ●                        ●
        (1)           (100)                   (3001)

queue = [1, 100, 3001]
Output = 3


4) ping(3002)
--------------

Time: t = 3002
Window: [3002 - 3000, 3002] = [2 .. 3002]

Existing pings:
    ●1, ●100, ●3001

Check oldest first:

    Is 1 < 2?  → Yes → too old → REMOVE 1

Now pings:
    ●100, ●3001

Both 100 and 3001 are inside [2, 3002].

Add ping at t = 3002:

         2           100        3001       3002
         |-----------|-----------|----------|
                     ●           ●          ●
                    (100)      (3001)     (3002)

(1 was to the left of 2, so it "fell out" of the window and got removed.)

queue = [100, 3001, 3002]
Output = 3


"""
















"""
Quick Example Walkthrough:

Calls:
    ping(1)
    ping(100)
    ping(3001)
    ping(3002)

1) ping(1)
    Valid times: from -2999 to 1
    Queue before: []
    Old pings to remove: none
    Add 1 → queue = [1]
    Return: 1

2) ping(100)
    Valid times: from -2900 to 100
    Queue before: [1]
    1 is still in this range → keep it
    Add 100 → queue = [1, 100]
    Return: 2

3) ping(3001)
    Valid times: from 1 to 3001
    Queue before: [1, 100]
    1 and 100 are still in this range → keep both
    Add 3001 → queue = [1, 100, 3001]
    Return: 3

4) ping(3002)
    Valid times: from 2 to 3002
    Queue before: [1, 100, 3001]
    1 is now too old (less than 2) → remove it
    100 and 3001 are still in range → keep them
    Add 3002 → queue = [100, 3001, 3002]
    Return: 3

Final outputs: [1, 2, 3, 3]
"""

























"""
🔥 VISUAL TIMELINE ANIMATION — How RecentCounter REALLY Works
   Goal: Understand WHY ping(3002) returns 3 (not 1) when earlier pings exist.

RULE:
    FOR EACH ping(t):
        only keep timestamps inside [t - 3000, t]

Meaning:
    t = 3002 → window = [3002 - 3000, 3002] = [2, 3002]
    Anything < 2 is too old and gets removed.

Let's animate each call.
"""

# -------------------------------
# CALL 1: ping(1)
# -------------------------------

# Starting window: [-2999, 1]
# (We have no pings yet)

# Add 1
# Timeline:
#   [1]

# Count = 1
print("ping(1)  → window [-2999, 1]    → [1]                     → returns 1")

# -------------------------------
# CALL 2: ping(100)
# -------------------------------

# New window: [-2900, 100]
# Pings we have: [1]

# Is 1 inside [-2900, 100]? Yes → keep it.

# Add 100
# Timeline:
#   [1] ---- [100]

# Count = 2
print("ping(100) → window [-2900, 100]  → [1, 100]               → returns 2")

# -------------------------------
# CALL 3: ping(3001)
# -------------------------------

# New window: [1, 3001]
# Pings: [1, 100]

# 1 ≥ 1 → keep
# 100 ≥ 1 → keep

# Add 3001
# Timeline:
#   [1] ---- [100] ------------------------- [3001]

# Count = 3
print("ping(3001) → window [1, 3001]     → [1, 100, 3001]         → returns 3")

# -------------------------------
# CALL 4: ping(3002)
# -------------------------------

# New window: [2, 3002]
# Pings: [1, 100, 3001]

# Check each:
#   1 < 2 → REMOVE (too old)
#   100 ≥ 2 → keep
#   3001 ≥ 2 → keep

# Add 3002
# Timeline:
#         [100] ------------------ [3001] ---- [3002]

# Count = 3
print("ping(3002) → window [2, 3002]     → [100, 3001, 3002]      → returns 3")

"""
FINAL OUTPUTS: [1, 2, 3, 3]

KEY INSIGHT:
    • Even though 3002 is bigger than 3000,
      that DOESN'T MATTER.

    • What matters is:
          “Is each old ping at least 3000 ms behind t?”

      i.e. keep pings >= (t - 3000)

    • x is valid WHEN x is within 3000 ms BEFORE t.
"""











# Task: Count the number of pings in the last 3000 ms (inclusive range [t-3000, t]).
# Example: pings at t = 1, 100, 3001, 3002 → Output: [1, 2, 3, 3]
# Why: Practices deque (double-ended queue) for efficient sliding window time-based counting.

from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize an empty deque to store ping timestamps
        # Why? Deque allows O(1) append (right) and popleft (left)
        self.queue = deque()  # queue = []

    def ping(self, t):  # Example: t = 1, then 100, then 3001, then 3002
        # --- Step 1: Remove pings older than t - 3000 ---
        # Why? Only keep pings in the inclusive range [t-3000, t]
        while self.queue and self.queue[0] < t - 3000:  # queue[0] is the oldest ping
            self.queue.popleft()  # Remove outdated ping

        # --- Example: ping(1) ---
        # t = 1, t - 3000 = -2999
        # queue = [], no elements to remove
        # while condition: False → skip

        # --- Example: ping(100) ---
        # t = 100, t - 3000 = -2900
        # queue = [1], 1 >= -2900 → keep
        # while condition: False → skip

        # --- Example: ping(3001) ---
        # t = 3001, t - 3000 = 1
        # queue = [1, 100], 1 >= 1 → keep, 100 >= 1 → keep
        # while condition: False → skip

        # --- Example: ping(3002) ---
        # t = 3002, t - 3000 = 2
        # queue = [1, 100, 3001], 1 < 2 → remove
        # popleft() → queue = [100, 3001]
        # 100 >= 2 → keep
        # while condition: False → exit

        # --- Step 2: Add the current ping ---
        # Why? This is a new request at time t
        self.queue.append(t)  # Add t to the end of the queue

        # --- Example: ping(1) ---
        # queue.append(1) → queue = [1]

        # --- Example: ping(100) ---
        # queue.append(100) → queue = [1, 100]

        # --- Example: ping(3001) ---
        # queue.append(3001) → queue = [1, 100, 3001]

        # --- Example: ping(3002) ---
        # queue.append(3002) → queue = [100, 3001, 3002]

        # --- Step 3: Return the count of recent pings ---
        # Why? len(queue) = number of pings in [t-3000, t]
        return len(self.queue)

        # --- Example Outputs ---
        # ping(1):     len([1]) = 1
        # ping(100):   len([1, 100]) = 2
        # ping(3001):  len([1, 100, 3001]) = 3
        # ping(3002):  len([100, 3001, 3002]) = 3


# Test the class
obj = RecentCounter()
print(obj.ping(1))     # 1 → [1]
print(obj.ping(100))   # 2 → [1, 100]
print(obj.ping(3001))  # 3 → [1, 100, 3001]
print(obj.ping(3002))  # 3 → [100, 3001, 3002]

