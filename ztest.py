# # print(type(True))

# # if False:
# #     print(1)
# #     print(3)

# # print(10)


grocery_list = ["apple", "grape", "banana", "orange"]

# for i in range(len(grocery_list)):
#     print(grocery_list[i])

# print(range(5))
# print(range(len(grocery_list)))


# for i, item in enumerate(grocery_list):
    # print(i, item)

# j = len(grocery_list) - 1
# while j >= 0:
#     print(grocery_list[j])
#     j -= 1
# print('end')

z = 42

def our_print(s):
    print(z)
    print(s + " hello")

print(our_print("Hi"))

s = 87

# By default a function returns 'None' which is nothing 

def our_print(s):
    print(z)
    print(s + " hello")
    return None  # Here is what it looks like behind the scenes 

print(our_print("Hi"))


