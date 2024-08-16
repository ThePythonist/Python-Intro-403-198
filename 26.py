numbers = [128, 256, 320, 480]
n = int(input("Enter any number : "))

# if n % 2 == 0 and 99 < n < 1000:
#     numbers.append(n)

if n % 2 == 0 and str(n)[0] == "-" and len(str(n)) == 4:
    numbers.append(n)
elif n % 2 == 0 and str(n)[0] != "-" and len(str(n)) == 3:
    numbers.append(n)

print(numbers)
