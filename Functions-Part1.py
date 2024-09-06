# def checknumber(x):
#     if type(x) in [int, float]:
#         # print("Okay continue")
#         return "Number"
#     else:
#         # print("Not okay")
#         return "Not Number"
#
#
# checknumber(11)

# if checknumber("11") == "Number":
#     print("Yes")
# else:
#     print("No")


# ==============================================================

def checknumber(x):
    if x % 2 == 0:
        # print("Even")
        return "Even"
    else:
        # print("Odd")
        return "Odd"


# print(checknumber(14))
# checknumber(int(input("Enter n : ")))

# if checknumber(8) == "Even":
#     print("Pasokh zoj ast")

# numbers = [11, 4, 2, 3, 5, 12, 16]
#
# for i in numbers:
#     print(checknumber(i))

# print(checknumber(12))

# ==============================================================

# def gozinesh(x):
#     if x % 2 == 0:
#         print(x)
#
#
# numbers = [11, 4, 2, 3, 5, 12, 16]
# for i in numbers:
#     gozinesh(i)


# ==============================================================

def login(username, password):
    if username == "admin" and password == "admin":
        print("Successfully logged in")
        return True
    else:
        print("Incorrect username or password")
        return False

#
# status = login("admin", "admin")
#
# if status == True:
#     print("Dashboard")

# ==============================================================

# items = [10, 40, 30, 20]
# print(sum(items))

# ==============================================================

# def mysum(seq):
#     summation = 0
#
#     for i in seq:
#         summation += i
#
#     return summation
#
#
# print(mysum([10, 30, 20, 40]))
