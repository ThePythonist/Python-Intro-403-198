import datetime

# Current Date and Time

# x = datetime.datetime.now()
# print(x)
# # print(type(x))
# x = str(x)
# print(x[:4])

# =========================================================================

# Delta

# x = datetime.datetime(2020, 5, 17, 23, 0)
# y = datetime.datetime(1991, 1, 16,23, 30)
# print(x - y)

# =========================================================================

# Attributes

# year = datetime.datetime.now().year
# month = datetime.datetime.now().month
# minute = datetime.datetime.now().minute
# day = datetime.datetime.now().day
# hour = datetime.datetime.now().hour
# second = datetime.datetime.now().second
#
# print(f"{hour}:{minute}")

# =========================================================================

# Strftime

now = datetime.datetime.now()
print(now.strftime("%B"))
