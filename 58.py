# def is_prime(number):
#     divs = [i for i in range(1, number + 1) if number % i == 0]
#     return True if len(divs) == 2 else False
#
#
# print(is_prime(45))
# print(is_prime(17))

def is_prime(number):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    print(True) if len(divs) == 2 else print(False)


is_prime(45)
is_prime(17)
