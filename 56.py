def has_duplicate1(word):
    characters = []

    for i in word:
        if i in characters:
            return True
        else:
            characters.append(i)

    return False


def has_duplicate2(word):
    if len(set(word)) == len(word):
        return False
    else:
        return True


print(has_duplicate2("mohammad"))
