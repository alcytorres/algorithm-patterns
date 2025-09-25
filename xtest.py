

# Hash Set 

def numJewelsInStones(J, S):
    Jset = set(J)
    count = 0

    for s in S:
        if s in Jset:
            count += 1
    
    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
# Output 3

# Jset = {'a', 'A'}



