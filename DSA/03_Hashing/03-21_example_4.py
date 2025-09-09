# 2352. Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


# Example:
    # Input: grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    # Output: 1

    # Explanation: There is 1 equal row and column pair:
    # - (Row 2, Column 1): [2, 7, 7]

# Solution: https://leetcode.com/problems/equal-row-and-column-pairs/solutions/3519973/equal-row-and-column-pairs/






# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown





# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 


def equalPairs(grid):
    count = 0
    n = len(grid)
    
    # Check each row r against each column c.
    for r in range(n):
        for c in range(n):
            match = True
            
            # Iterate over row r and column c.
            for i in range(n):
                if grid[r][i] != grid[i][c]:
                    match = False
                    break
                    
            # If row r equals column c, increment count by 1.
            count += int(match)
                
    return count

grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(equalPairs(grid))
# Output: 1
