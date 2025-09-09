# 2260. Minimum Consecutive Cards to Pick Up

# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

# Example:
    # Input: cards = [3, 4, 2, 3, 4, 7]
    # Output: 4

    # Explanation: We can pick up the cards [3, 4, 2, 3] which contain a matching pair of cards with value 3. Note that picking up the cards [4, 2, 3, 4] is also optimal.

# Solution: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/solutions/


def minimumCardPickup(cards):
    last = {}
    best = float('inf')

    for i, v in enumerate(cards):
        if v in last:
            best = min(best, i - last[v] + 1)
        last[v] = i

    return best if best < float('inf') else -1

cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))
# Output: 4









# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Solutions

def minimumCardPickup(cards):
    minPick = float('inf')
    seen = {}

    for i, n in enumerate(cards):
        if n in seen:
            if i - seen[n] + 1 < minPick:
                minPick = i - seen[n] + 1
        seen[n] = i

    if minPick == float('inf'):
        return -1
    
    return minPick

cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))
# Output: 4

# Time – O(N) as we iterate over the input only once
# Space – O(N) at worst case we will be storing all the numbers in the input to our index hashmap. (in case of all distinct numbers in input array)

# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/solutions/1996393/python3-beginner-friendly-explained/




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––

from math import inf  

def minimumCardPickup(self):
    d = {}
    l = 0
    mi = inf
    for r in range(len(cards)):
        if cards[r] in d:
            if mi > r - d[cards[r]] + 1:
                mi = r - d[cards[r]] +1
        d[cards[r]] = r
    if mi < inf:
        return mi
    return -1


cards = [3, 4, 2, 3, 4, 7]
print(minimumCardPickup(cards))
# Output: 4

# Time complexity:O(N)
# Space complexity:O(N)

# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/solutions/7054707/easy-solution-without-enum-in-single-loop-beats-90/