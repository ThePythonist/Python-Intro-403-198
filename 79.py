def find1(file):
    file = file.readlines()
    file = sorted(file, key=len)
    longest = file[-1]
    print(longest)
    print(len(longest))


# f = open("words.txt", "r")
# find1(f)


def find2(file):
    file = file.readlines()
    longest = max(file, key=len)
    print(longest)
    print(len(longest))


# f = open("words.txt", "r")
# find2(f)


def find3(file):
    file = file.readlines()
    longest = max(file, key=len)
    maxlen = len(longest)

    for i in file:
        if len(i) == maxlen:
            print(i)


f = open("words.txt", "r")
find3(f)
