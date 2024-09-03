numbers = []

for i in range(5):
    num = input("Entry : ")

    try:
        num = float(num)
        # if str(num)[-2:] == ".0":
        if num == int(num):
            numbers.append(int(num))
        else:
            numbers.append(num)
    except ValueError:
        pass

print(numbers)
