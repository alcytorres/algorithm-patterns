# 2225 Find Players With Zero or One Losses

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:
    # answer[0] is a list of all players that have not lost any matches.
    # answer[1] is a list of all players that have lost exactly one match.

# The values in the two lists should be returned in increasing order.

# Note:
    # You should only consider the players that have played at least one match.
    # The testcases will be generated such that no two matches will have the same outcome.

# Example
    # Input: matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
    # Output: [[1, 2, 10], [4, 5, 7, 8]]

# Explanation:
    # Players 1, 2, and 10 have not lost any matches.
    # Players 4, 5, 7, and 8 each have lost one match.
    # Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1, 2, 10] and answer[1] = [4,5,7,8].

# Solution: https://leetcode.com/problems/find-players-with-zero-or-one-losses/solutions/2655744/find-players-with-zero-or-one-losses/


from collections import defaultdict

def findWinners(matches):
    losses = defaultdict(int)   # player -> number of losses
    seen   = set()              # players that appeared in at least one match

    # Record all players (winners and losers) and count each loss
    for winner, loser in matches:
        seen.add(winner)
        seen.add(loser)
        losses[loser] += 1

    # zero-loss players: in seen but not in losses
    zero_loss = [p for p in seen if losses[p] == 0]
    # one-loss players: exactly one loss
    one_loss  = [p for p in seen if losses[p] == 1]

    return [sorted(zero_loss), sorted(one_loss)]


matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
print(findWinners(matches))
# Output: [[1, 2, 10], [4, 5, 7, 8]] → Players 1, 2, and 10 never lost a match, while players 4, 5, 7, 8 each lost exactly once.

# seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 2, 4: 1, 1: 0, 2: 0, 10: 0}

"""
Time: O(N + P log P)
  - Let N = number of matches, P = number of unique players.
  - Process all matches once to update dict + set → O(N).
  - Scan players to build zero_loss and one_loss → O(P).
  - Sort both lists → O(P log P).
  - Overall: O(N + P log P).
  - Since P ≤ 2N, worst case is O(N log N).

Space: O(P) ≈ O(N)
  - Dict 'losses' stores up to P players.
  - Set 'seen' stores up to P players.
  - Output lists (zero_loss, one_loss) store up to P players.
  - Overall: O(P).
  - Since P ≤ 2N, worst case O(P) = O(N).

Interview Answer

Time: O(N log N)
  - Process matches in O(N).
  - Sorting dominates → O(N log N).

Space: O(N)
  - Dictionary and set track up to N players.
  - Extra space is linear.



Overview for Each Iteration
Input: matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
Step 1: Record players and count losses
Match   | winner | loser | seen                            | losses
--------|--------|-------|---------------------------------|-------------------------------------
[1, 3]  | 1      | 3     | {1, 3}                          | {3:1}
[2, 3]  | 2      | 3     | {1, 2, 3}                       | {3:2}
[3, 6]  | 3      | 6     | {1, 2, 3, 6}                    | {3:2, 6:1}
[5, 6]  | 5      | 6     | {1, 2, 3, 5, 6}                 | {3:2, 6:2}
[5, 7]  | 5      | 7     | {1, 2, 3, 5, 6, 7}              | {3:2, 6:2, 7:1}
[4, 5]  | 4      | 5     | {1, 2, 3, 4, 5, 6, 7}           | {3:2, 6:2, 7:1, 5:1}
[4, 8]  | 4      | 8     | {1, 2, 3, 4, 5, 6, 7, 8}        | {3:2, 6:2, 7:1, 5:1, 8:1}
[4, 9]  | 4      | 9     | {1, 2, 3, 4, 5, 6, 7, 8, 9}     | {3:2, 6:2, 7:1, 5:1, 8:1, 9:1}
[10, 4] | 10     | 4     | {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} | {3:2, 6:2, 7:1, 5:1, 8:1, 9:1, 4:1}
[10, 9] | 10     | 9     | {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} | {3:2, 6:2, 7:1, 5:1, 8:1, 9:2, 4:1}

Step 2: Identify zero-loss and one-loss players
p  | losses[p] | zero_loss  | one_loss
---|-----------|------------|-------------
1  | 0         | [1]        | []
2  | 0         | [1, 2]     | []
3  | 2         | [1, 2]     | []
4  | 1         | [1, 2]     | [4]
5  | 1         | [1, 2]     | [4, 5]
6  | 2         | [1, 2]     | [4, 5]
7  | 1         | [1, 2]     | [4, 5, 7]
8  | 1         | [1, 2]     | [4, 5, 7, 8]
9  | 2         | [1, 2]     | [4, 5, 7, 8]
10 | 0         | [1, 2, 10] | [4, 5, 7, 8]
Final: [sorted([1, 2, 10]), sorted([4, 5, 7, 8])] = [[1, 2, 10], [4, 5, 7, 8]]

zero_loss = [1, 2, 10]   # Players in seen with losses[p] == 0
one_loss  = [4, 5, 7, 8] # Players in seen with losses[p] == 1




Simple Overview for Each Iteration
i | Match   | Seen (New) | Losses (New/Updated)
--|---------|------------|---------------------
- | -       | {}         | {}
0 | [1, 3]  | {1, 3}     | {3:1}
1 | [2, 3]  | {2}        | {3:2}
2 | [3, 6]  | {6}        | {6:1}
3 | [5, 6]  | {5}        | {6:2}
4 | [5, 7]  | {7}        | {7:1}
5 | [4, 5]  | {4}        | {5:1}
6 | [4, 8]  | {8}        | {8:1}
7 | [4, 9]  | {9}        | {9:1}
8 | [10, 4] | {10}       | {4:1}
9 | [10, 9] | {}         | {9:2}

Final: [[1, 2, 10], [4, 5, 7, 8]]




Most IMPORTANT thing to Understand:
    • The problem is about counting how many times each player loses.

    • If a player has 0 losses → they belong in the first list (never lost).

    • If a player has exactly 1 loss → they belong in the second list (lost once).
    
    • We only care about players who actually appeared in at least one match.

Why this code Works:
    • Hash map (losses): tracks how many losses each player has.

    • Set (seen): records every player that appears, winner or loser, so nobody is missed.

    • After processing all matches:
        • Players with losses[p] == 0 → never lost → go in zero_loss.
        • Players with losses[p] == 1 → lost once → go in one_loss.

    • Sorting at the end puts the lists in the required increasing order.

    • Efficiency: We process matches in a single pass (O(n)) and then scan players (O(m)),avoiding any brute force comparisons.

    • Intuition: Think of it like keeping a scoreboard:
        • Every time a player loses, we add +1 to their “loss count.”
        • At the end, read the scoreboard:
            • players with 0 losses → group 1,
            • players with 1 loss → group 2.

TLDR:
    • This solution works because we count each player's losses in a hash map, then group players with 0 and 1 losses directly.

Quick Example Walkthrough:
    Input: matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]

    Step 1: Tally losses
        • Player 3, 6, 9 each lose twice
        • Players 4, 5, 7, 8 each lose once
        • Players 1, 2, 10 never lose

    Step 2: Build results
        • zero_loss = [1, 2, 10]
        • one_loss  = [4, 5, 7, 8]

    Final Answer: [[1, 2, 10], [4, 5, 7, 8]]

"""


# –––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import defaultdict

def findWinners(matches):
    losses = defaultdict(int)  # Track number of losses per player
    seen = set()               # Track all players in matches

    for winner, loser in matches:  # Iterate over each match
        seen.add(winner)      # Add winner to seen players
        seen.add(loser)       # Add loser to seen players
        losses[loser] += 1    # Increment losses for loser

    zero_loss = [p for p in seen if losses[p] == 0]  # Players with no losses
    one_loss = [p for p in seen if losses[p] == 1]   # Players with one loss

    return [sorted(zero_loss), sorted(one_loss)]     # Return sorted lists


# –––––––––––––––––––––––––––––––––––––––––––––––––
# Same Solution with Standard For Loop
    # The Solution up top uses Basic list comprehension
    # I like this solution

from collections import defaultdict

def findWinners(matches):
    losses = defaultdict(int)   # player -> number of losses
    seen   = set()              # players that appeared in at least one match

    for winner, loser in matches:
        seen.add(winner)
        seen.add(loser)
        losses[loser] += 1

    # zero-loss players: in seen but not in losses
    zero_loss = []
    for p in seen:
        if losses[p] == 0:
            zero_loss.append(p) 

    # one-loss players: exactly one loss
    one_loss = []
    for p in seen:
        if losses[p] == 1:
            one_loss.append(p)

    return [sorted(zero_loss), sorted(one_loss)]


matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
print(findWinners(matches))
# Output: [[1, 2, 10], [4, 5, 7, 8]]



# –––––––––––––––––––––––––––––––––––––––––––––––––
# Basic list comprehension
l = [x for x in range(5)]
print(l)  # Outputs: [0, 1, 2, 3, 4]

# Standard For Loop
l = []
for x in range(5):
    l.append(x)
print(l)  # Outputs: [0, 1, 2, 3, 4]


# –––––––––––––––––––––––––––––––––––––––––––––––––
# Playground

# Simple code to play with
seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 2, 4: 1, 1: 0, 2: 0, 10: 0}

zero_loss = [p for p in seen if losses[p] == 0]
print(zero_loss)  # Output: [1, 2, 10]

one_loss = [p for p in seen if losses[p] == 1]
print(one_loss)  # Output: [4, 5, 7, 8]





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def findWinners_bruteforce(matches):
    # Collect all players (naively, avoiding dicts)
    players = []
    for w, l in matches:
        if w not in players:
            players.append(w)
        if l not in players:
            players.append(l)

    zero_loss = []
    one_loss = []

    # For each player, count losses by scanning all matches
    for p in players:
        loss_count = 0
        for w, l in matches:
            if l == p:
                loss_count += 1
        if loss_count == 0:
            zero_loss.append(p)
        elif loss_count == 1:
            one_loss.append(p)

    zero_loss.sort()
    one_loss.sort()
    return [zero_loss, one_loss]


matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
print(findWinners_bruteforce(matches))
# Output: [[1, 2, 10], [4, 5, 7, 8]]

"""
Time: O(m^2)
  - Build unique player list with 'in' checks on a Python list: up to ~2m insert checks, each O(m) → O(m^2).
  - For each player (≤ 2m), scan all matches (m) to count losses → O(m^2).
  - Overall: O(m^2) time.

Space: O(p)  (p = number of distinct players, ≤ 2m)
  - Store the players list and the two result lists.
  - Overall: O(p) additional space.


Overview for Each Iteration
Input: matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
Step 1: Collect all players
w  | l  | players
---|----|--------------------------------
-  | -  | []
1  | 3  | [1, 3]
2  | 3  | [1, 3, 2]
3  | 6  | [1, 3, 2, 6]
5  | 6  | [1, 3, 2, 6, 5]
5  | 7  | [1, 3, 2, 6, 5, 7]
4  | 5  | [1, 3, 2, 6, 5, 7, 4]
4  | 8  | [1, 3, 2, 6, 5, 7, 4, 8]
4  | 9  | [1, 3, 2, 6, 5, 7, 4, 8, 9]
10 | 4  | [1, 3, 2, 6, 5, 7, 4, 8, 9, 10]
10 | 9  | [1, 3, 2, 6, 5, 7, 4, 8, 9, 10]

Step 2: Count losses for each player
p  | loss_count | w  | l  | Action              | zero_loss | one_loss
---|------------|----|----|---------------------|-----------|-------------
1  | 0          | *  | *  | Add to zero_loss    | [1]       | []
3  | 0          | 1  | 3  | loss_count+=1       | [1]       | []
   | 1          | 2  | 3  | loss_count+=1       | [1]       | []
   | 2          | *  | *  | Skip (loss_count=2) | [1]       | []
2  | 0          | *  | *  | Add to zero_loss    | [1, 2]    | []
6  | 0          | 3  | 6  | loss_count+=1       | [1, 2]    | []
   | 1          | 5  | 6  | loss_count+=1       | [1, 2]    | []
   | 2          | *  | *  | Skip (loss_count=2) | [1, 2]    | []
5  | 0          | 4  | 5  | loss_count+=1       | [1, 2]    | []
   | 1          | *  | *  | Add to one_loss     | [1, 2]    | [5]
7  | 0          | 5  | 7  | loss_count+=1       | [1, 2]    | [5]
   | 1          | *  | *  | Add to one_loss     | [1, 2]    | [5, 7]
4  | 0          | 10 | 4  | loss_count+=1       | [1, 2]    | [5, 7]
   | 1          | *  | *  | Add to one_loss     | [1, 2]    | [5, 7, 4]
8  | 0          | 4  | 8  | loss_count+=1       | [1, 2]    | [5, 7, 4]
   | 1          | *  | *  | Add to one_loss     | [1, 2]    | [5, 7, 4, 8]
9  | 0          | 4  | 9  | loss_count+=1       | [1, 2]    | [5, 7, 4, 8]
   | 1          | 10 | 9  | loss_count+=1       | [1, 2]    | [5, 7, 4, 8]
   | 2          | *  | *  | Skip (loss_count=2) | [1, 2]    | [5, 7, 4, 8]
10 | 0          | *  | *  | Add to zero_loss    | [1, 2, 10]| [5, 7, 4, 8]

Step 3: Sort results
zero_loss = sorted([1, 2, 10]) = [1, 2, 10]
one_loss = sorted([5, 7, 4, 8]) = [4, 5, 7, 8]
Final: [[1, 2, 10], [4, 5, 7, 8]]

"""




# –––––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown 

# Task: Given matches[i] = [winner, loser], return [players with 0 losses, players with 1 loss] in sorted order.
# Example: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]] → Output = [[1,2,10],[4,5,7,8]]
# Why: Practices hash map and set usage to track losses and players efficiently.

from collections import defaultdict

def findWinners(matches):  # Example: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

    # 1️⃣ Initialize data structures
    # Initialize a defaultdict to track number of losses per player
    # Why? We need to count how many times each player loses
    losses = defaultdict(int)  # losses = {}

    # Initialize a set to track players who played at least one match
    # Why? We only consider players who appear in matches
    seen = set()  # seen = {}

    # 2️⃣ Process matches
    # Iterate through each match to update losses and seen players
    # Why? We need to record winners and losers and count losses
    for winner, loser in matches:  # Iterate over pairs [1,3], [2,3], ..., [10,9]
        # --- Match 1: winner = 1, loser = 3 ---
        seen.add(winner)  # seen = {1}
        seen.add(loser)   # seen = {1, 3}
        losses[loser] += 1  # losses = {3: 1}
        # After Match 1: seen = {1, 3}, losses = {3: 1}

        # --- Match 2: winner = 2, loser = 3 ---
        if winner == 2 and loser == 3:
            seen.add(winner)  # seen = {1, 3, 2}
            seen.add(loser)   # seen = {1, 3, 2} (3 already in set)
            losses[loser] += 1  # losses = {3: 2}
            # After Match 2: seen = {1, 2, 3}, losses = {3: 2}

        # --- Match 3: winner = 3, loser = 6 ---
        if winner == 3 and loser == 6:
            seen.add(winner)  # seen = {1, 2, 3}
            seen.add(loser)   # seen = {1, 2, 3, 6}
            losses[loser] += 1  # losses = {3: 2, 6: 1}
            # After Match 3: seen = {1, 2, 3, 6}, losses = {3: 2, 6: 1}

        # --- Match 4: winner = 5, loser = 6 ---
        if winner == 5 and loser == 6:
            seen.add(winner)  # seen = {1, 2, 3, 6, 5}
            seen.add(loser)   # seen = {1, 2, 3, 6, 5}
            losses[loser] += 1  # losses = {3: 2, 6: 2}
            # After Match 4: seen = {1, 2, 3, 5, 6}, losses = {3: 2, 6: 2}

        # --- Match 5: winner = 5, loser = 7 ---
        if winner == 5 and loser == 7:
            seen.add(winner)  # seen = {1, 2, 3, 5, 6}
            seen.add(loser)   # seen = {1, 2, 3, 5, 6, 7}
            losses[loser] += 1  # losses = {3: 2, 6: 2, 7: 1}
            # After Match 5: seen = {1, 2, 3, 5, 6, 7}, losses = {3: 2, 6: 2, 7: 1}

        # --- Match 6: winner = 4, loser = 5 ---
        if winner == 4 and loser == 5:
            seen.add(winner)  # seen = {1, 2, 3, 5, 6, 7, 4}
            seen.add(loser)   # seen = {1, 2, 3, 5, 6, 7, 4}
            losses[loser] += 1  # losses = {3: 2, 6: 2, 7: 1, 5: 1}
            # After Match 6: seen = {1, 2, 3, 4, 5, 6, 7}, losses = {3: 2, 6: 2, 7: 1, 5: 1}

        # --- Match 7: winner = 4, loser = 8 ---
        if winner == 4 and loser == 8:
            seen.add(winner)  # seen = {1, 2, 3, 4, 5, 6, 7}
            seen.add(loser)   # seen = {1, 2, 3, 4, 5, 6, 7, 8}
            losses[loser] += 1  # losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1}
            # After Match 7: seen = {1, 2, 3, 4, 5, 6, 7, 8}, losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1}

        # --- Match 8: winner = 4, loser = 9 ---
        if winner == 4 and loser == 9:
            seen.add(winner)  # seen = {1, 2, 3, 4, 5, 6, 7, 8}
            seen.add(loser)   # seen = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            losses[loser] += 1  # losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 1}
            # After Match 8: seen = {1, 2, 3, 4, 5, 6, 7, 8, 9}, losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 1}

        # --- Match 9: winner = 10, loser = 4 ---
        if winner == 10 and loser == 4:
            seen.add(winner)  # seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            seen.add(loser)   # seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            losses[loser] += 1  # losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 1, 4: 1}
            # After Match 9: seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 1, 4: 1}

        # --- Match 10: winner = 10, loser = 9 ---
        if winner == 10 and loser == 9:
            seen.add(winner)  # seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            seen.add(loser)   # seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
            losses[loser] += 1  # losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 2, 4: 1}
            # After Match 10: seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, losses = {3: 2, 6: 2, 7: 1, 5: 1, 8: 1, 9: 2, 4: 1}

    # 3️⃣ Identify players with zero or one loss
    # Zero-loss players: in seen but not in losses (never lost)
    # Why? Players who only won have no entry in losses
    zero_loss = [p for p in seen if losses[p] == 0]  # Check each player in seen
    # Players 1, 2, 10: losses[1] = 0, losses[2] = 0, losses[10] = 0
    # zero_loss = [1, 2, 10]

    # One-loss players: exactly one loss in losses
    # Why? We need players with exactly one loss
    one_loss = [p for p in seen if losses[p] == 1]  # Check each player in seen
    # Players 3, 4, 5, 6, 7, 8, 9: losses[3] = 2, losses[4] = 1, losses[5] = 1, losses[6] = 2, losses[7] = 1, losses[8] = 1, losses[9] = 2
    # one_loss = [4, 5, 7, 8]

    # 4️⃣ Return sorted lists
    # Sort both lists and return as [zero_loss, one_loss]
    # Why? The problem requires results in increasing order
    return [sorted(zero_loss), sorted(one_loss)]  # return [sorted([1, 2, 10]), sorted([4, 5, 7, 8])] = [[1, 2, 10], [4, 5, 7, 8]]


matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]
print(findWinners(matches))  
# Output: [[1, 2, 10], [4, 5, 7, 8]]