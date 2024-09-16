# def func(number):
#     divs = [i for i in range(1, number + 1) if number % i == 0]
#     return divs


numbers = [15, 21, 10, 8]
print(list(map(lambda number: [i for i in range(1, number + 1) if number % i == 0], numbers)))
