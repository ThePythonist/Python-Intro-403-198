scores = {
    "mabani computer": 20,
    "zaban omomi": 17,
    "andishe eslami": 6,
    "sakhteman dadeha": 16
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": passed")
    else:
        print(k, ": failed")

length = 0
summation = 0
for i in scores.values():
    length += 1
    summation += i

print("Grade :", summation / length)

# grade = sum(scores.values()) / len(scores)
# print("Grade :", grade)
