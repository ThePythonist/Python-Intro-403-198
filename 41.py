# items = ["python", "js", "java", "python", "c#", "js"]
#
# for i in items:
#     if items.count(i) != 1:
#         items.remove(i)
#
# print(items)

# ----------------------------------------------------------

items = ["python", "js", "java", "python", "c#", "js"]
unique = []

for i in items:
    if i not in unique:
        unique.append(i)

print(unique)
