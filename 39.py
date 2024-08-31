pythons = ["aria", "kiana", "yasna", "kiarash"]
icdls = ["yasna", "taha", "mohammad", "aria"]
commons = []

for i in pythons:
    if i in icdls:
        commons.append(i)

print(commons)

# ====================================================

# for i in pythons:
#     if i == i in icdls:
#         commons.append(i)
#
# print(commons)

# ====================================================

# for i in pythons:
#     for j in icdls:
#         if i == j:  # martabe ejrayi : i * j
#             commons.append(j)
#
# print(commons)
