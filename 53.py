def digit_summation(number):
    number = str(number)
    # summation = 0
    #
    # for i in number:
    #     summation += int(i)
    #
    # return summation
    digits = [int(i) for i in number]
    return sum(digits)


print(digit_summation(45351))
