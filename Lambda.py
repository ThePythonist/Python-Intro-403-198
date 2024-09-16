# def ahvalporsi(name):
#     return "Hello" + " " + name
#
#
# print(ahvalporsi("nima"))

# ahvalporsi = lambda name: "Hello" + " " + name
# print(ahvalporsi("nima"))


# # --------------------------------------------------------------------


# def power(x, y):
#     return x ** y
#
#
# print(power(4, 3))

# power = lambda x, y: x ** y
# print(power(2, 3))


# # --------------------------------------------------------------------
#
#
# def f(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(f(4))

# f = lambda x: True if x % 2 == 0 else False
# print(f(13))


# # --------------------------------------------------------------------
# print((syntax lambda)(vorodi ha))

# print((lambda x, y: x * y)(5, 4))

# # --------------------------------------------------------------------

if (lambda x: True if x % 2 == 0 else False)(11):
    print("Yes")
else:
    print("No")
