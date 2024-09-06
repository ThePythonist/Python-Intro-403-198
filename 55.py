def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    print(divisors)
    if sum(divisors) == number:
        return True
    else:
        return False


print(is_perfect(28))
