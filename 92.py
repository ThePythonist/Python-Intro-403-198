import random


# def generate_password(length):
#     password = []
#     for i in range(length):
#         password.append(str(random.randint(0, 9)))
#
#     print("".join(password))
#
#
# generate_password(6)

def generate_password(length):
    password = ""
    for i in range(length):
        password += str(random.randint(0, 9))

    print(password)


generate_password(8)
