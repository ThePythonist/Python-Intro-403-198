f = open("words.txt").readlines()
revlist = []
for i in f:
    revlist.append(i[::-1])

open("reversed_words.txt", "w").writelines(revlist)
