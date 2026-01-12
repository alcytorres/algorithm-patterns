# DNA Complements 
# IBM Interview: March 7, 2025
"""
Let's solve this DNA complement problem in Python. We need to write the dnaComplement function that takes a DNA string s, reverses it, and replaces each symbol with its complement (A ↔ T, C ↔ G).

Problem Breakdown
Input: A string s containing DNA symbols (A, T, C, G).

Task:
    Reverse the string.
    Replace each symbol with its complement:
    A ↔ T
    C ↔ G

Output: The reverse complement string.

Constraints:
    1 ≤ length of s ≤ 1000
    s only contains A, T, C, G.

Solution Approach
  Define a mapping for the complements (e.g., A → T, T → A, C → G, G → C).
  Reverse the string.
  Replace each character with its complement using the mapping.
  Return the resulting string.

DNA Complements: https://grok.com/chat/c8f1646c-c9c8-4d11-8a91-c7a5762d72c4
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'dnaComplement' function below.

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


# DNA Complement (Reverse + Map Complements)
def dnaComplement(s):
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    result = ""
    for char in s[::-1]:          
        result += complements[char] 
    
    return result

print(dnaComplement("ATGC"))       # → "GCAT"
print(dnaComplement("AAA"))        # → "TTT"
print(dnaComplement("G"))          # → "C"
print(dnaComplement("ACCGGGTTT"))  # → "AAACCCGGT"


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def dnaComplement(s):
    # Dictionary mapping each base to its complement
    complements = {
        'A': 'T',    # Adenine pairs with Thymine
        'T': 'A',    # Thymine pairs with Adenine
        'C': 'G',    # Cytosine pairs with Guanine
        'G': 'C'     # Guanine pairs with Cytosine
    }
    
    result = ""      # Build the reverse complement here, one letter at a time
    
    # Iterate through the string in reverse order
    for char in s[::-1]:     # s[::-1] gives reversed string
        # Look up complement and append it
        result += complements[char]  # Dictionary lookup is O(1)
    
    return result        # Return the completed string


"""
Time: O(N)
  - Let N = length of the DNA string s.
  - Reversing the string using slicing (s[::-1]) takes O(N).
  - Looping through the reversed string processes each character once → O(N).
  - Dictionary lookups for complements are O(1) per character.
  - Overall: O(N).

Space: O(N)
  - The result string stores N characters.
  - The complement dictionary has constant size (4 entries) → O(1).
  - Overall: O(N).

  
---
Interview Answer: Worst Case

Time: O(N)
  - Reverse the string and map each character once.

Space: O(N)
  - Output string requires linear space.


  
---
Most IMPORTANT thing to Understand:
    • DNA bases pair in fixed ways: A ↔ T and C ↔ G.

    • The problem asks for the reverse of the string AND the complement at the same time.

    • If you process the string from right to left and swap each base, you get the answer directly.

---
Why this code Works:
    • Data structure: a dictionary maps each DNA base to its complement in O(1) time.

    • Technique: reverse traversal + lookup.
        • s[::-1] reverses the DNA string.
        • Each reversed character is replaced with its complement.

    • Efficiency: we avoid extra passes.
        • No separate reverse step and no nested loops.
        • Each character is handled exactly once → O(N).

    • Intuition: read the DNA strand backwards and flip each base as you go.

---
TLDR:
    • Reverse the DNA string and replace each base with its complement using a lookup table.

---
Quick Example Walkthrough:

    Input:
        s = "ATGC"

    Step 1: Reverse the string
        s[::-1] → "CGTA"

    Step 2: Replace each character with its complement
        'C' → 'G'
        'G' → 'C'
        'T' → 'A'
        'A' → 'T'

    Step 3: Build result as we go
        "G" → "GC" → "GCA" → "GCAT"

    Final Answer:
        "GCAT"

        

---
Q: Why is the space complexity O(N)?

  • We create a reversed copy of the input string (s[::-1]), which stores N characters.

  • We build a new result string that also stores N characters.

  • Although the complement dictionary is constant size (O(1)), the output grows with input size.

  • Extra memory scales with N → O(N) space.
"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Simpler Version
def dnaComplement(s):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # One-liner version (still very readable for beginners)
    return ''.join(complements[char] for char in reversed(s))

print(dnaComplement("ATGC"))       # "GCAT"



# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def dnaComplement(s):
    # Fixed mapping: A↔T, C↔G (standard DNA base pairing)
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Most Pythonic & readable one-liner version:
    #   1. reversed(s)    → iterate characters from end to start
    #   2. complements[char] → look up complement (O(1))
    #   3. ''.join(...)   → efficiently build the final string
    return ''.join(complements[char] for char in reversed(s))

"""
Time: O(N)
  - Let N = length of the string s.
  - reversed(s) iterates through the string once → O(N).
  - For each character:
      • Dictionary lookup for complement → O(1).
      • Generator feeds into join.
  - ''.join(...) builds the final string in O(N).
  - Overall: O(N).

Space: O(N)
  - The output string stores N characters.
  - The complements dictionary is constant size (4 entries) → O(1).
  - Generator uses constant extra space.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - One pass to reverse and map each character.

Space: O(N)
  - Output string requires linear space.
"""
