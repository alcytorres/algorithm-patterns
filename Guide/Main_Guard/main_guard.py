# ===============================
# GUIDE: What is if __name__ == '__main__'?
# ===============================
# Source: https://www.youtube.com/watch?v=KZpYtNtGxSU

"""
Every Python file has a hidden variable called __name__.
You never create it — Python creates it for you automatically.

Python sets __name__ based on HOW the file is used:
    • You RUN the file directly       → __name__ = '__main__'
    • You IMPORT it from another file  → __name__ = the file's name (e.g. 'file_1')

So this line:
    if __name__ == '__main__':

means: "Only run this code if I'm the file being executed directly."
"""


# ===============================
# The example (two real files you can test)
# ===============================

"""
file_1.py:
    def add(a, b):
        return a + b

    if __name__ == '__main__':
        if add(1, 2) == 3:
            print("pass")
        else:
            print("fail")


file_2.py:
    from file_1 import add
    print(add(10, 20))
"""


# ===============================
# Scenario 1: Run file_1.py directly
# ===============================

"""
You type:  python3 file_1.py

What happens:
    1. Python sets file_1's __name__ = '__main__'  (because you ran it directly)
    2. The add() function is defined
    3. if '__main__' == '__main__':  → True  → test code RUNS
    4. add(1, 2) returns 3, which equals 3 → prints "pass"

Output:
    pass
"""


# ===============================
# Scenario 2: Run file_2.py (which imports file_1)
# ===============================

"""
You type:  python3 file_2.py

What happens:
    1. Python starts running file_2.py
    2. It hits: from file_1 import add
       → Python loads file_1.py to get the add function
       → But this time, it sets file_1's __name__ = 'file_1' (NOT '__main__')
    3. Inside file_1: if 'file_1' == '__main__':  → False  → test code is SKIPPED
    4. Back in file_2: print(add(10, 20)) runs → prints 30

Output:
    30

No "pass" or "fail" — the test code in file_1 was skipped!
"""


# ===============================
# Why does this matter?
# ===============================

"""
The problem WITHOUT if __name__ == '__main__':
    When you import a file, Python runs ALL the code in it.
    So any test code or print statements run during the import.
    That's messy — you only wanted the function, not the tests.

The fix WITH if __name__ == '__main__':
    Test code only runs when YOU run the file directly.
    When someone imports it, they just get the functions — no unwanted output.
"""


# ===============================
# Mental model
# ===============================

"""
    if __name__ == '__main__':  →  "Run this only if I'm the main script."

    Run directly   → __name__ is '__main__' → code inside RUNS
    Imported       → __name__ is the file name → code inside is SKIPPED
"""



# ===============================
# Try it yourself: Compare CORRECT vs WRONG
# ===============================

"""
CORRECT (current state — test code is inside the guard):
    python3 file_1.py  → pass       (test runs because you ran it directly)
    python3 file_2.py  → 30         (test is skipped — only the add result)

WRONG (test code is outside the guard):
    1. In file_1.py, comment out the CORRECT section
    2. Uncomment the WRONG section
    3. python3 file_1.py  → pass     (same as before)
    4. python3 file_2.py  → pass     (test code leaked during import!)
                          → 30

    That "pass" leaking into file_2's output is the problem.
    There was no guard to stop it from running during import.




---
Q: Why does running file_2.py print "pass" AND 30 when there's no guard?
   
   All file_2 does is print(add(10, 20)) — so where does "pass" come from?

A: Because import doesn't just grab the function — it runs the entire file.

  • When Python sees from file_1 import add, it opens file_1.py and executes it top to bottom. If the test code is sitting out in the open (no guard), Python runs it during the import. That's where pass comes from.

 • Then after the import is done, print(add(10, 20)) runs and prints 30.

  • So you get both: pass from the import, then 30 from your code. You only wanted 30.



---
Q: But I only imported add, not the whole file. Why does Python run all of file_1?

A: Python has to execute the entire file to find add. There's no way to grab one function without running everything else.

  • from file_1 import add and import file_1 both run the whole file.

  • The from ... import part only controls what name you get access to — not what code runs.

"""