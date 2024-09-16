lines = open("words.txt").readlines()
c = 0
for i in lines:
    if c == 100:
        break
    if i[:3] == "sub":
        print(i)
        c += 1
