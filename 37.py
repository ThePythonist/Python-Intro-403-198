# numbers = [-8, -5, -10, -7, -21, -20, -15]
# # maximum = 0 # doesn't work for negative numbers
# # maximum = numbers[0]
# maximum = -(float("inf"))  # manfi bi nahayat
#
# for i in numbers:
#     if i > maximum:
#         maximum = i
#         # print("maximum changed to", i)
#     else:
#         # print("maximum is still", maximum)
#         pass
#
# print("Maximum :", maximum)

# =====================================================================

# numbers = [8, 5, 10, 7, 21, 20, 15]
# maximum = sorted(numbers)[-1]
# print("Maximum :", maximum)

# =====================================================================

numbers = [8, 5, 10, 7, 21, 20, 15]
print(max(numbers))
print(min(numbers))
