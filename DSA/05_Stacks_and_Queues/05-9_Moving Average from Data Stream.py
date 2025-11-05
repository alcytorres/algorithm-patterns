# 346. Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
 
# Solution: https://leetcode.com/problems/moving-average-from-data-stream/description/

# Example 1:
    # Input
    # ["MovingAverage", "next", "next", "next", "next"]
    # [[3], [1], [10], [3], [5]]
    # Output
    # [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# Approach 1: Array or List

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)


# Create the MovingAverage object with a window size of 3
movingAverage = MovingAverage(3)

# Call next() with the example inputs
print(movingAverage.next(1))   # → 1.0       = (1) / 1
print(movingAverage.next(10))  # → 5.5       = (1 + 10) / 2
print(movingAverage.next(3))   # → 4.66667   = (1 + 10 + 3) / 3
print(movingAverage.next(5))   # → 6.0       = (10 + 3 + 5) / 3

# Input = ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
















# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 2: Double-ended Queue

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)
    

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach 3: Circular Queue with Array
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)