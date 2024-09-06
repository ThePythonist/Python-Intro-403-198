def is_binary(number):
    for i in number:
        if i not in ["0", "1"]:
            return False

    return True


numbers = ["01101", "24", "15", "100", "111"]

for i in numbers:
    print(i, ":", is_binary(i))
