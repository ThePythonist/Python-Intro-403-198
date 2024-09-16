courses = {
    "mabani computer": (20, 3),
    "zaban omomi": (17, 2),
    "andishe eslami": (6, 2),
    "tarbiat badani": (16, 1),
    "madar manteghi": (19, 3)
}


def pass_or_fail(courses):
    for k, v in courses.items():
        if v[0] >= 10:
            print(k, ": passed")
        else:
            print(k, ": failed")


def grade(courses):
    scores = []
    units = []

    for k, v in courses.items():
        scores.append(v[0] * v[1])
        units.append(v[1])

    print("Grade", end=' : ')
    print(sum(scores) / sum(units))


# pass_or_fail(courses)
grade(courses)
