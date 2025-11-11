# 71. Simplify Path

# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:
    # A single period '.' represents the current directory.
    # A double period '..' represents the previous/parent directory.
    # Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    # Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

# The simplified canonical path should follow these rules:
    # The path must start with a single slash '/'.
    # Directories within the path must be separated by exactly one slash '/'.
    # The path must not end with a slash '/', unless it is the root directory.
    # The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
    # Return the simplified canonical path.

# Solution: https://leetcode.com/problems/simplify-path/description/

# Example 1:
    # Input: path = "/home/"
    # Output: "/home"
    # Explanation:
    # The trailing slash should be removed.

# Example 2:
    # Input: path = "/home//foo/"
    # Output: "/home/foo"
    # Explanation:
    # Multiple consecutive slashes are replaced by a single one.

# Example 3:
    # Input: path = "/home/user/Documents/../Pictures"
    # Output: "/home/user/Pictures"
    # Explanation:
    # A double period ".." refers to the directory up a level (the parent directory).

# Example 4:
    # Input: path = "/../"
    # Output: "/"
    # Explanation:
    # Going one level up from the root directory is not possible.

# Example 5:
    # Input: path = "/.../a/../b/c/../d/./"
    # Output: "/.../b/d"
    # Explanation:
    # "..." is a valid name for a directory in this problem.


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

path = "/home/"
print(simplifyPath(path))  # /home

path = "/home//foo/"
print(simplifyPath(path))  # /home/foo

path = "/../"
print(simplifyPath(path))  # /

path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))  #  "/.../b/d"



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
Overview for Each Iteration
Input: path = "/home/"

Step: Split and process path
part | part == '' or '.' | part == '..' | stack (before) | Action         | stack (after)
-----|-------------------|--------------|----------------|----------------|---------------
     | True              | False        | []             | continue       | []
home | False             | False        | []             | append         | ['home']
     | True              | False        | ['home']       | continue       | ['home']
Final: '/' + 'home' → "/home"




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

Example 1: path = "/home/"
--------------------------------
    Split → ['', 'home', '']
    Stack = []
    'home' → push ['home']
    Final: "/" + "home" → "/home"
    Output: "/home" ✅


Example 2: path = "/home//foo/"
--------------------------------
    Split → ['', 'home', '', 'foo', '']
    Stack = []
    'home' → push ['home']
    '' → skip
    'foo' → push ['home', 'foo']
    Final: "/" + "home/foo" → "/home/foo"
    Output: "/home/foo" ✅


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


Example 5: path = "/.../a/../b/c/../d/./"
--------------------------------
    Split → ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.', '']
    Stack = []
    '...' → ['...']
    'a' → ['...', 'a']
    '..' → pop 'a' → ['...']
    'b' → ['...', 'b']
    'c' → ['...', 'b', 'c']
    '..' → pop 'c' → ['...', 'b']
    'd' → ['...', 'b', 'd']
    '.' → skip
    Final: "/" + ".../b/d" → "/.../b/d"
    Output: "/.../b/d" ✅


Example 6: path = "/a/b///c/.././d/../f/"
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



    


Q: What does `continue` do in this solution?
--------------------------------------------

- ✅ `continue` tells Python to **skip the rest of the current loop** 
  and move on to the next iteration.

- In this code, it's used when `part` is either:
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

"""





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def simplifyPath(path):
    stack = []                        # Stack to track valid directories

    for part in path.split('/'):      # Split path by '/' into components
        if part == '' or part == '.': # Skip empty parts or current dir
            continue
        if part == '..':              # If go up one directory
            if stack:                 # Only pop if not at root
                stack.pop()
        else:                         # Valid directory name
            stack.append(part)        # Add to path

    return '/' + '/'.join(stack)      # Join with '/' and add leading '/'







# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Playground


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








# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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