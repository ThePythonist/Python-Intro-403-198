# entry = input("Type something : ")
# print("-"*50)
#
# while entry != "exit":
#     entry = input("Type something : ")
#     print("-"*50)

# ====================================================

# flag = 1
#
# while flag:
#     entry = input("Type something : ")
#     print("-" * 50)
#     if entry == "exit":
#         flag = 0
# else:  # 1 bar ejra mishe
#     print("Flag has turned into False")

# ====================================================

while True:
    entry = input("Type something : ")
    print("-" * 50)
    if entry == "exit":
        break # else ejra nemishavad
else:  # 1 bar ejra mishe
    print("Flag has turned into False")
