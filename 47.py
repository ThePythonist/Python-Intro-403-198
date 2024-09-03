numbers = []

while True:
    num = input("Entry : ")
    if num == "exit":
        break

    try:
        num = float(num)
        if num == int(num):
            numbers.append(int(num))
        else:
            numbers.append(num)
    except ValueError:
        pass

print(numbers)
