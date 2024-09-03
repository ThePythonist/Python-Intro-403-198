numbers = []

for i in range(3):
    num = input("Entry : ")

    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        # print("Entry was not a number")
        pass

print(numbers)
