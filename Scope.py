balance = 0  # global
print(balance)


def variz(x):
    global balance  # permission for updating variables
    print("dar hale variz ...")
    balance += x  # turning it into local


variz(500)
print(balance)
