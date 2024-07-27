# 1 Tuples

# t = (10, 20, 30, 50, 40)
# print(t)
# print(type(t))
# print(t[0])
# print(t[12])  # error !
# print(t[2:12])  # okay !

# mahdodiati dar nou dadeh va tedad dadeh nadarim !

# items = ("arian", 4.5, "peyman", 5.5, "saeed", 6)
# names = ("arian", "peyman", "saeed")
# names[0] = "amir" # tuples ha immutable hastand
# print(names)

# names = ("ali", "saeed", "mina", "ali", "mina", "hamid")  # tekrari ghabol mikonad
# print(names)

# t1 = (100, 200, 300)
# t2 = (-50, 10, 50)
# print(t2 + t1)  # jam pazir hastan va tartib ra rayat mikonan

# cities = ("tehran", "yazd", "shiraz", "zahedan")
# print(cities*2) # okay
# print(cities - "yazd") # error !
# print(t2 - t1)  # error !

# t = (1, 2, 1, 3, 4, 1, 5, 1)
# print(t.count(1))
# print(t.index(5))

# ------------------------------------------------------------------------------------------

# 2 Sets

# s = {10, 20, 30, 40, 10, 10}
# print(s)  # tartib pazir nist - tekrari ghabol nemikonad
# print(type(s))

# countries = {"usa", "germany", "iran", "spain"}
# print(countries[-1]) # indexing nadarad
# countries[0] = "italy"

# s1 = {100, 200}
# s2 = {300, 400}
# print(s1 + s2)
# print(s1 * 4)

# s1 = {"digikala", "irancell", "torob", "snapp"}
# s2 = {"bank mellat", "mofid", "asan pardakht", "divar"}

# s1.add("divar")
# print(s1)

# s1.remove("torob")
# print(s1)

# print(s1.union(s2))

# fruits = {"apple", "banana", "cherry"}
# x = fruits.pop()
# print(x)

# ------------------------------------------------------------------------------------------

# 3 Lists

# items = [10, 20, 30, 10, 40, 50, 10]
# print(items)  # tartib darad - tekrari ham darad
# print(type(items))
# print(items[0])  # indexing darad

# items[-1] = 60
# print(items)  # list mutable hast
# del items[0]
# print(items)

# lst1 = [10, 20, 30]
# lst2 = [40, 50, 60]
# print(lst2 + lst1)
# print(lst1*5)

# movies = ["manhattan", "zodiac", "annie hall", "inception"]

# movies.append("interstellar")
# print(movies)

# movies.insert(2, "interstellar")
# print(movies)

# movies = [1, 2, 5, 4, 3]
# movies.sort()
# print(movies)

# movies.reverse()
# print(movies)

# print(movies[::-1])

# ------------------------------------------------------------------------------------------

# 4 Dictionaries

# d = {"name": "aria", "city": "tehran", "age": 30}
# print(d)
# print(type(d))
# print(len(d))

# print(d["age"]) # index adadi nadarad - kilidi darad

# d1 = {"name": "aria", "city": "tehran", "age": 30}
# d2 = {"name": "aria", "city": "tehran", "age": 30}
# print(d1+d2)

# d["age"] = 32
# print(d)

# d = {"name": "aria", "city": "tehran", "age": 30, "city": "shiraz"}
# print(d)

# d1 = {"name": "aria", "weight": 60, "age": 60}

# d1.setdefault("job", "developer")
# print(d1)

# d2 = {"email": "aria@gmail.com", "country": "russia", "age": 40}
# d1.update(d2)  # update meghdar mojod ra update mikonad
# print(d1)

# d1.setdefault("age", 20) # update nemikone
# print(d1)

# d1 = {"club": "manchester united", "country": "england", "league": "premier league"}
# print(d1.keys())
# print(d1.values())
# print(d1.items())

info = {
    "club": "barcelona",
    "players": [{"yamal": 16}, {"pedri": 20}, {"de jong": 27}, {"roberto": 34}],
    "country": "spain",
    "league": "la liga",
    "rival": "real madrid",
    "manager": "hans flick"
}

print(info["players"][0])
print(info["players"][-1])
