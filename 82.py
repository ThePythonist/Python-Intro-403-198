# lines = open("words.txt").read()
# print(lines.split("\n"))

# -----------------------------------------------

# lines = open("words.txt").read()
# print(lines.replace("\n", "-"))

# -----------------------------------------------

lines = open("words.txt").readlines()
newwords = []
for i in lines:
    newwords.append(i[:-1])

print(newwords)
