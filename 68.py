number = int(input("Enter any number : "))
divs = [i for i in range(1, number) if number % i == 0]
print((lambda x: True if x == sum(divs) else False)(number))
