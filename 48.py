info = {
    "cityname": "tehran",
    "country": "iran",
    "population": 8694000,
    "temp": 33,
    "area": 730,
    "code": "021"
}

key = input("Search for key : ")

# if key in info:
#     print(info[key])
# else:
#     print(key, "Not Found")

try :
    print(info[key])
except KeyError:
    print(key, "Not Found")
