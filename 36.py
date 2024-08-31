numbers = []

for i in range(5):
    x = int(input("Enter any number : "))
    numbers.append(x)

# numbers.sort() # works only for lists
print(sorted(numbers))  # works for any sequence
