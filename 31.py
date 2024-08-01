counter = 1
a, b = 0, 1

while counter <= 100:
    # fibonacci series
    print(a)
    c = a+b
    a = b
    b = c
    counter += 1
