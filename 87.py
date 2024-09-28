# f = open("words.txt").read().split("\n")
# numbers = []
#
# for i in f:
#     try:
#         i = float(i)
#         if str(i)[-2:] == ".0":
#             numbers.append(int(i))
#         else:
#             numbers.append(i)
#     except ValueError:
#         pass
#
# print(numbers)

# ============================================================

f = open("words.txt").read().split("\n")
numbers = []

for i in f:
    if i.isdigit():
        numbers.append(i)

print(numbers)
