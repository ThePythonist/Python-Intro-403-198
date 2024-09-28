# f = open("words.txt").read().split("\n")
# selection = []
#
# for i in f:
#     if not i.isdigit():
#         for j in i:
#             if j.isdigit():
#                 selection.append(i)
#                 break
#
# print(selection)

# =====================================================

f = open("words.txt").read().split("\n")
selection = []

for i in f:
    if i.isdigit():
        continue

    for j in i:
        if j.isdigit():
            selection.append(i)
            break

print(selection)
