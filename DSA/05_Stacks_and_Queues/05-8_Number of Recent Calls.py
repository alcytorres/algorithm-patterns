# 933. Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:
    # RecentCounter() Initializes the counter with zero recent requests.
    # int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Solution: https://leetcode.com/problems/number-of-recent-calls/description/

# Example 1:
    # Input: ["RecentCounter", "ping", "ping", "ping", "ping"]
    # [[], [1], [100], [3001], [3002]]
    # Output: [null, 1, 2, 3, 3]

    # Explanation
    # RecentCounter recentCounter = new RecentCounter();
    # recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
    # recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
    # recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
    # recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

"""
TLDR: Number of Recent Calls
    • You need to count how many requests happened in the last 3000 milliseconds.
    • Each time you call ping(t), a new request happens at time t.
    • You only keep the pings that happened within [t - 3000, t].
    • Return how many pings are still inside that 3000 ms window.

Think of it like this
You have a timeline of pings.
When a new ping comes in:
    1. Remove all pings older than t - 3000.
    2. Add the new ping.
    3. Count what's left.
"""

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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



"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import deque  # Import deque for efficient append/pop from both ends
class RecentCounter:
    def __init__(self):
        self.queue = deque()      # Initialize empty deque to store ping timestamps

    def ping(self, t):
        while self.queue and self.queue[0] < t - 3000:  # While queue not empty and oldest ping is too old
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

