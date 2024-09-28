import time

f = open("words.txt", "r").readlines()

# f = list(reversed(f))
# print(f)

# f.reverse()
# print(f)
# ----------------------------------------------------

t1 = time.time()
f = f[::-1]
output = "".join(f)
open("reversed_words.txt", "w").write(output)
t2 = time.time()
print(t2 - t1)

# ----------------------------------------------------

# t1 = time.time()
# output = open("reversed_words.txt", "w")
# f = f[::-1]
# for i in f:
#     output.writelines(i)
# t2 = time.time()
# print(t2-t1)
