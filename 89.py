n = int(input("How many files ? "))
frmt = input("Which type of file ? ")

# for i in range(n):
#     open(f"file{i}.{frmt}", "w")

for i in range(n):
    x = open(f"file{i}.{frmt}", "x")