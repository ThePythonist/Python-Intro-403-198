items = ["IT", 10, [], 5.5, "Financial", 20, True, 7.75]
numbers = []

for i in items:
    if type(i) == str:
        numbers.append(i)

print(numbers)
