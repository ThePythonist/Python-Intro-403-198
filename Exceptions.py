import builtins

explist = [
    i for i in dir(builtins) if
    isinstance(getattr(builtins, i), type)
    and issubclass(getattr(builtins, i), BaseException)
]

for exc in explist:
    print(exc)
