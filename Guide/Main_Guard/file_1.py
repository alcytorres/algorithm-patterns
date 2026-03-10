# ===============================
# file_1.py
# ===============================
# Source: https://www.youtube.com/watch?v=KZpYtNtGxSU


# ===============================
# CORRECT: test code inside the guard
# ===============================
def add(a, b):
    return a + b


if __name__ == '__main__':
    if add(1, 2) == 3:
        print("pass")
    else:
        print("fail")


# ===============================
# WRONG: test code WITHOUT the guard (uncomment to compare)
# ===============================
# def add(a, b):
#     return a + b
#
# if add(1, 2) == 3:
#     print("pass")
# else:
#     print("fail")
