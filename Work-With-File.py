# f = open("cars.txt")
# print(f.read()) # string
# print(f.tell())  # mogheiat cursor
# f.seek(5)  # taghir mogheiat cursor
# print(f.read())

# ------------------------------------------

# f = open("cars.txt")

# print(f.readline()) # string
# print(f.readline())
# print(f.readline())

# for i in range(10):
#     print(f.readline())

# ------------------------------------------

# f = open("cars.txt")
#
# print(f.readlines())  # list

# ------------------------------------------

# f = open("cars.txt", "w")
# print(f.write("bmw"))

# ------------------------------------------

# f = open("cars.txt", "a+")
# f.seek(0)
# print(f.read())
# f.write("\ntoyota")

# ------------------------------------------

open("jadid.txt", "w").write("hello")
