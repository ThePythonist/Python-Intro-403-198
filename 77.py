lines = open("words.txt").readlines()

for i in lines:
    if len(i) == 6:
        print(i)
