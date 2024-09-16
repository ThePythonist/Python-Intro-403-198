a = int(input("Enter a : "))
b = int(input("Enter b : "))

print((lambda x, y: "equal" if x == y else x if x > y else y)(a, b))
