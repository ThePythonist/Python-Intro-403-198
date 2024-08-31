n = int(input("How many numbers do you want to enter : "))
numbers = []

for i in range(n):
    x = int(input("Enter any number : "))
    numbers.append(x)

print(max(numbers))
