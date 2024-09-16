def is_binary(number):
    for i in number:
        if i not in {"0", "1"}:
            return False
    return True


binaries = list(filter(is_binary, ["512", "10100001", "10", "24", "10101101", ]))
print(binaries)
