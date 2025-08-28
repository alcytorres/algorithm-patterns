# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import defaultdict

def maxNumberOfBalloons(text):
    # Step 1: Count characters in text
    counts = defaultdict(int)
    
    for c in text:
        counts[c] += 1
    
    # Step 2: Find how many "balloon"s we can make
    return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])


text = "nlaebolko"
print(maxNumberOfBalloons(text))
# Output: 1

# counts = {'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1}
