# items = []
#
# for i in range(5):
#     x = int(input("Enter any number : "))
#     if 0 < x < 11:
#         items.append(x)
#
# print(items)
# ------------------------------------------------
# items = []
#
# while len(items) != 5:
#     x = int(input("Enter any number : "))
#     if 0 < x < 11:
#         items.append(x)
#
# print(items)
# ------------------------------------------------
items = []
c = 0

while True:
    if c == 5:
        break

    x = int(input("Enter any number : "))
    if 0 < x < 11:
        items.append(x)
        c += 1

print(items)
