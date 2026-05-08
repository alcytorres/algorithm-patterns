# 71. Simplify Path
"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:
    A single period '.' represents the current directory.
    A double period '..' represents the previous/parent directory.
    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:
    The path must start with a single slash '/'.
    Directories within the path must be separated by exactly one slash '/'.
    The path must not end with a slash '/', unless it is the root directory.
    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
    Return the simplified canonical path.

Example 1:
    Output: "/a/b/f"
    Input: path = "/a/b///c/.././d/../f/"
    Explanation:
    Extra slashes are treated as one.
    "." means current directory (ignored).
    ".." moves up one level.
    Simplified path: "/a/b/f"

Example 2:
    Input: path = "/home/"
    Output: "/home"
    Explanation:
    The trailing slash should be removed.

Example 2:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation:
    Multiple consecutive slashes are replaced by a single one.

Example 3:
    Input: path = "/../"
    Output: "/"
    Explanation:
    Going one level up from the root directory is not possible.

Example 4:
    Input: path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"
    Explanation:
    A double period ".." refers to the directory up a level (the parent directory).

TLDR:
Given a Unix-style file path string
Simplify it to its canonical form by:
  • Removing redundant slashes (`// → /`)
  • Ignoring current directory markers (`.`)
  • Going up one directory for (`..`)
  • Keeping valid folder names (like `...`)
Return the final simplified absolute path starting with `/`

Solution: https://leetcode.com/problems/simplify-path/description/
"""

def simplifyPath(path):
    stack = []

    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)


path = "/a/b///c/.././d/../f/"
print(simplifyPath(path))  # /a/b/f

path = "/home//foo/"
print(simplifyPath(path))  # /home/foo

path = "/../"
print(simplifyPath(path))  # /

path = path = "/home/user/Documents/../Pictures"
print(simplifyPath(path))  # /home/user/Pictures



"""
Time: O(N)
  - Let N = length of the path string.
  - Splitting the path by '/' takes O(N).
  - Iterating through all parts:
      • Each part is processed once.
      • Stack operations (append, pop) are O(1).
  - Joining stack elements into the final string takes O(N).
  - Overall: O(N).

Space: O(N)
  - Stack stores valid directory names (worst case: every segment is valid).
  - The final string also takes O(N) space when joined.
  - A few loop variables (part, path components) use O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Each directory name is processed once.

Space: O(N)
  - Stack holds directory names to form the simplified path.



---
Most IMPORTANT thing to Understand:
    • The path must be simplified by resolving ".", "..", and redundant slashes.

    • A stack is used to keep track of valid directories — like walking through folders step-by-step.

    • Each ".." means “go up one folder,” so we pop from the stack if possible.

---
Why this code Works:
    • Data structure: stack stores the directory path being built.

    • Technique:
        - Split the path by '/' into parts.
        - Skip "" (extra slashes) and "." (current directory).
        - On "..", pop the last valid directory if it exists.
        - Otherwise, push the directory name onto the stack.

    • Efficiency: O(N) time and O(N) space — each path segment is processed once.

    • Intuition: Imagine navigating a file explorer — when you go into a folder, add it to the path; when you click “up one level,” remove the last folder.

---
TLDR:
    • Split the path and use a stack to simulate moving through directories — push folders, pop for "..", skip "." and empty parts.

---
Quick Example Walkthroughs:

Example 1: path = "/a/b///c/.././d/../f/"
----------------------------------------
    Split → ['', 'a', 'b', '', '', 'c', '..', '.', 'd', '..', 'f', '']

    Stack = []

    ''   → skip
    'a'  → push → ['a']
    'b'  → push → ['a','b']
    ''   → skip
    ''   → skip
    'c'  → push → ['a','b','c']
    '..' → pop  → ['a','b']
    '.'  → skip
    'd'  → push → ['a','b','d']
    '..' → pop  → ['a','b']
    'f'  → push → ['a','b','f']
    ''   → skip

    Final: "/" + "a/b/f" → "/a/b/f"
    Output: "/a/b/f" ✅


Example 2: path = "/home//docs/"
--------------------------------
    Split → ['', 'home', '', 'docs', '']
    Stack = []

    'home' → push ['home']
    '' → skip
    'docs' → push ['home', 'docs']

    Final: "/" + "home/docs" → "/home/docs"
    Output: "/home/docs" ✅


Example 3: path = "/../"
--------------------------------
    Split → ['', '..', '']
    Stack = []

    '..' → try to go up, but stack empty → skip

    Final: "/" + "" → "/"
    Output: "/" ✅


Example 4: path = "/home/user/Documents/../Pictures"
--------------------------------
    Split → ['', 'home', 'user', 'Documents', '..', 'Pictures']
    Stack = []

    'home' → ['home']
    'user' → ['home','user']
    'Documents' → ['home','user','Documents']
    '..' → pop → ['home','user']
    'Pictures' → ['home','user','Pictures']

    Final: "/" + "home/user/Pictures"
    Output: "/home/user/Pictures" ✅




---
Q: What does `continue` do in this solution?

  • `continue` tells Python to SKIP the rest of the current loop
  and move on to the next iteration.

  • In this code, it's used when `part` is either:
    - an empty string '' (from multiple slashes like "//"), or
    - a single dot '.' (which means "current directory" in Unix paths)

- When either of those appears, we don't need to do anything — 
  we simply skip and go to the next `part`.

Example:
---------
    path = "/home//./foo/"
    split → ['','home','','.','foo','']
    → parts '' and '.' trigger `continue` → skipped
    → stack ends up as ['home','foo']

✅ Prevents adding useless or invalid entries to the path.




---
Q: How do extra slashes (// or ///) get removed?

A: Two steps:

1. path.split('/') → automatically turns multiple slashes into EMPTY strings ('')
   Example:
   "/a/b///c/" → split gives: ['', 'a', 'b', '', '', 'c', '']

   → All those '' come from extra slashes!

2. This line IGNORES the empty strings:
   if part == '' or part == '.':
       continue    → skips them completely!

So yes:
   • split('/') creates '' for extra slashes
   • continue skips every '' → they disappear!

Result: "/a/b///c/.././" → becomes clean "/a/b"


"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def simplifyPath(path):
    stack = []       # Stack to track valid directories

    for part in path.split('/'):      # Split path by '/' into components
        if part == '' or part == '.': # Skip empty parts or current dir
            continue
        if part == '..':            # If go up one directory
            if stack:               # Only pop if not at root
                stack.pop()
        else:                       # Valid directory name
            stack.append(part)      # Add to path

    return '/' + '/'.join(stack)      # Join with '/' and add leading '/'





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground

# STRING METHOD: 
.split()
# What it does: Splits string into list based on delimiter.
# Why use it: Parses strings into tokens efficiently.
# How it works: Default delimiter is whitespace; optional maxsplit.
# When to use: Tokenizing inputs in word or array problems.
# Time/Space: O(n) time (n = string length), O(n) space for list.

# Syntax:
string.split(separator)  # Returns list; 'separator' optional (defaults to whitespace)

# Basic Example 1 (Default Whitespace):
s = "a b  c"
print(s.split())  # Output: ['a', 'b', 'c']

# Basic Example 2 (Custom Delimiter):
s = "1,2,3"
print(s.split(','))  # Output: ['1', '2', '3']

# Basic Example 3: Splitting a path (LeetCode-relevant)
path = "/a//b/c/"
print(path.split('/'))
# ['', 'a', '', 'b', 'c', '']  ← empty strings come from extra slashes

# Basic Example 4 (No Delimiter):
s = "abc"
print(s.split())  # Output: ['abc']

# DSA Example (Word Parsing):
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

"""
📘 split() Mini Cheat Sheet

split()                → smart whitespace split
   • collapses spaces
   • trims ends
   • no empty strings

split(delimiter)       → literal split
   • every delimiter counts
   • keeps empty strings
   • no trimming/collapsing

Examples:
" a  b ".split()       → ['a','b']
"/a//b/".split('/')    → ['','a','','b','']

---
Character Walkthrough: s = "/a//b/c/" 
  s.split('/') → ['', 'a', '', 'b', 'c', '']

    /  starts a new piece → ''  
    a  added to piece → 'a'
    /  slash ends piece → 'a' saved
    /  slash again → empty piece '' saved
    b  added → 'b'
    /  ends piece → 'b' saved
    c  added → 'c'
    /  ends piece → 'c' saved
    (end) trailing slash → '' saved

    Final: ['', 'a', '', 'b', 'c', '']

"""


# ––––––––––––––––––––––––––––––––––––––––––––––
"""
Tutorial: .split() + .join() in LeetCode

  - .split() turns string into list of parts
  - .join() turns list back into string with separator
  
  - Use together to clean, reorder, or rebuild strings
"""

# Example 1: Reverse Words
def reverse_words(s):
    words = s.split()           # → ['sky', 'is', 'blue']
    words.reverse()             # → ['blue', 'is', 'sky']
    return " ".join(words)      # → "blue is sky"

print(reverse_words("sky is blue"))


# Example 2: Remove Extra Spaces
def clean_spaces(s):
    words = s.split()           # → ['hello', 'world'] (removes extra spaces)
    return " ".join(words)      # → "hello world"

print(clean_spaces("  hello   world  "))


# Example 3: Build Path from string
def build_path(s):
    parts = s.split("/")           # → ['', 'home', 'user', 'docs']
    parts = [p for p in parts if p]  # remove empty
    return "/" + "/".join(parts)

print(build_path("/home/user/docs/"))  # "/home/user/docs"


# Example 3: Build Path from string (no list comprehension)
def build_path(s):
    parts = s.split("/")           # ['', 'home', 'user', 'docs']
    stack = []
    for p in parts:
        if p:                      # skip empty strings
            stack.append(p)
    return "/" + "/".join(stack)

print(build_path("/home/user/docs/"))  # "/home/user/docs"


# ––––––––––––––––––––––––––––––––––––––––––––––
"""
📘 Tutorial: When to Use `continue` in LeetCode

  • `continue` skips the *rest of the loop* and jumps to the next item.

  • Use it when you want to ignore certain cases early and keep your logic clean.

  • Great for filtering: skip blanks, skip invalid input, skip no-op values.
"""

# Example 1: Skip negative numbers
nums = [-1, 2, -3, 4]
result = []
for n in nums:
    if n < 0:
        continue      # skip negatives
    result.append(n)
print(result)  # Output: [2, 4]


# Example 2: Skip empty strings
words = ["hi", "", "code", ""]
clean = []
for w in words:
    if w == "":
        continue      # skip blanks
    clean.append(w)
print(clean)  # Output: ["hi", "code"]


# Example 3: Skip '.' and '' in Simplify Path
def simplifyPath(path):
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue    # skip meaningless parts
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)

print(simplifyPath("/a/./b//c/../"))  # Output: "/a/b"












# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Approach: Using Stacks

def simplifyPath(path):
    # Initialize a stack
    stack = []

    # Split the input string on "/" as the delimiter
    # and process each portion one by one
    for portion in path.split("/"):

        # If the current component is a "..", then
        # we pop an entry from the stack if it's non-empty
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == "." or not portion:
            # A no-op for a "." or an empty string
            continue
        else:
            # Finally, a legitimate directory name, so we add it
            # to our stack
            stack.append(portion)

    # Stich together all the directory names together
    final_str = "/" + "/".join(stack)
    return final_str


path = "/home/"
print(simplifyPath(path))  # /home