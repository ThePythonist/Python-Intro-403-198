def make_dict1(word):
    chars = {}
    index = 0
    for i in word:
        chars.setdefault(index, i)
        index += 1

    print(chars)


# make_dict1("engineer")

def make_dict2(word):
    chars = {}
    for i in range(len(word)):
        chars.setdefault(i, word[i])

    print(chars)


make_dict2("ali")