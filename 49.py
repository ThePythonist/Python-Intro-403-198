ages = {
    "taha": 30,
    "meysam": 32,
    "sama": 32,
    "kia": 24,
    "mina": 30
}

maxage = max(ages.values())

# for i in ages:
#     if ages[i] == maxage:
#         print(i)
#         # break

# for i in ages.items():
#     if i[1] == maxage:
#         print(i[0])

for k, v in ages.items():
    if v == maxage:
        print(k)
