lines = open("words.txt").readlines()
c = 0
for i in lines:
    # if i[-4:] == "ing\n":
    if i[-4:-1] == "ing":
        print(i)
