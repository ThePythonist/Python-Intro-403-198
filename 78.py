def func(file):
    five_letters = []

    for line in file:
        if len(line) == 6:
            five_letters.append(line)

    open("five_letters.txt", "w").writelines(five_letters)


f = open("words.txt").readlines()
func(f)
