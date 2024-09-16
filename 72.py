def find_longest1(text):
    text = text.split()
    lengths = [len(i) for i in text]
    maxlen = max(lengths)
    for i in text:
        if len(i) == maxlen:
            print(i)


def find_longest2(text):
    text = text.split()
    print(max(text, key=len))


def find_longest3(text):
    text = text.split()
    print(sorted(text, key=len)[-1])


find_longest3("python is a good programming language")
