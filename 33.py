items = ["IT", 10, [], 5.5, "Financial", 20, True, 7.75]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int,float]:
        numbers.append(i)

print(numbers)
