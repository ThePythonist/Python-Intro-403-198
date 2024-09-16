items = [10, True, 11, "guitar", 12.5, "piano", 6, 9.42]
print(list(filter(lambda x: type(x) in [int, float], items)))
