# Overview of all Methods

# ============================================================
# METHODS and BUILT-IN FUNCTIONS GUIDE
# ============================================================
# STRING METHODS
# LIST METHODS
# DICTIONARY METHODS
# SET METHODS
# BUILT-IN FUNCTIONS
# SPECIAL METHODS

"""
Rule of thumb:
• If it returns None → usually mutates the object
• If it returns something else → usually creates a new one (no mutation)
"""


### STRING METHODS      
# Do NOT mutate the original
.split()
.join()
ord()
chr()
.lower()
.upper()
.replace()
.isdigit()
.isnumeric()
.isalpha()
.format()

### LIST METHODS
# DO mutate the set
.append()
.pop()
.sort()
.reverse()
.extend()
.remove()
.insert()

### DICTIONARY METHODS   
# Do NOT mutate the dictionary
.get()
.items()
.keys()
.values()

### SET METHODS            
# DO mutate the set
.add()
.remove()

### BUILT-IN FUNCTIONS
# Do NOT mutate the dictionary
len()
range()
print()
sorted()
reversed()
enumerate()
sum()
max()
str()
int()
float()
list()
tuple()
dict()
set()
iter()
next()
zip()
any()
type()
input()
isinstance()


# MUTABLE CONTAINER CONSTRUCTORS & METHODS
# DO mutate the set
defaultdict(int)
defaultdict(list)
Counter()

deque()
.append() (deque method)
.appendleft() (deque method)
.pop() (deque method)
.popleft() (deque method)


### SPECIAL METHODS
# Do NOT mutate the dictionary
__init__()
__str__()




"""
MUTATION CHEAT-SHEET
Which operations mutate the original object in place?

STRING METHODS
──────────────
→ NEVER mutate (strings are immutable)
All string methods return a new string.

LIST METHODS
────────────
→ YES, mutate in place
Most mutating methods return None (except .pop() returns the element)

DICTIONARY METHODS
──────────────────
→ NO for read/view methods
.get()  .keys()  .values()  .items()

→ YES for mutating methods (not shown here)

SET METHODS
───────────
→ YES for typical in-place methods

BUILT-IN FUNCTIONS
──────────────────
→ NO mutation
Almost all return new value / object / view

MUTABLE CONTAINER CLASSES & THEIR METHODS
─────────────────────────────────────────
defaultdict(int/list)  Counter()  deque()
→ YES — these objects are mutable
Their typical methods mutate in place

SPECIAL / DUNDER METHODS (your examples)
────────────────────────────────────────
__init__()   → NO (only during object creation)
__str__()    → NO (returns representation, no change)


Quick rules of thumb:
  • Method returns None + changes the object → usually mutates in place
  • Returns new object / value / view / bool → does NOT mutate
  • Strings are immutable → no method ever mutates them
  
"""