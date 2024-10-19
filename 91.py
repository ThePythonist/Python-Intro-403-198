import datetime


def show_gregorian_age(birth):
    thisyear = int(str(datetime.datetime.now())[:4])
    age = thisyear - birth
    print(age)


show_gregorian_age(1991)
