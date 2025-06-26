# l = [x for x in range(5)]
# print(l)

# l = [x**2 for x in range(5)]
# print(l)

l = [x for x in range(5) if (x%2) == 0]
print(l)

l = [x if (x%2) == 0 else 5 for x in range(5)]
print(l)

l = [x if (x%2) == 0 else 5 for x in [4, 1, 6, 12]]
print(l)  # [4, 5, 6, 12]