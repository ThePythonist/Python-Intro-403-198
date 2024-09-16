def even_or_odd(number):
    if number % 2 == 0:
        print("Entry is even")
    else:
        print("Entry is odd")


def is_number(entry):
    if type(entry) in [int, float]:
        even_or_odd(entry)
    else:
        print("Entry is not a number")


is_number("ali")
is_number(3)
