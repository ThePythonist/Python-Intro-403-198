# numbers = []
# for i in range(10):
#     numbers.append(i)
# print(numbers)
# =============================================
# numbers = [i for i in range(10)]
# print(numbers)
# =============================================
# numbers = [i ** 2 for i in range(10)]
# print(numbers)
# =============================================
# numbers = ["OK" for i in range(10)]
# print(numbers)
# =============================================
numbers = [i for i in range(10) if i % 2 == 1]
print(numbers)
