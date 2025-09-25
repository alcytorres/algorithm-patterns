from collections import Counter

def numJewelsInStones(J, S):
    letters = Counter(S)
    curr = 0

    for c in J:
        curr += letters[c]
    return curr


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3

# Counter({'b': 4, 'A': 2, 'a': 1})
