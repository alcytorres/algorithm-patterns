# ===============================
# file_2.py
# ===============================
# Source: https://www.youtube.com/watch?v=KZpYtNtGxSU

# How to test:
#   1. Run: python3 file_2.py  → with CORRECT code you see ONLY: 30
#   2. Comment out the CORRECT section in file_1, uncomment the WRONG section
#   3. Run: python3 file_2.py  → now you see: pass AND 30 (test code leaked!)

from file_1 import add


print(add(10, 20))  # 30
