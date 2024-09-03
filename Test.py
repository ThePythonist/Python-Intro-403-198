items = [10, 40, 30, 20]
print(sum(items))


# ===================================================
def mysum(seq):
    summation = 0

    for i in seq:
        summation += i

    return summation


print(mysum([10, 30, 20, 40]))
