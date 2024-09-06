def custom_sort(items):
    # items = sorted(items)
    # print(items[::-1])
    print(sorted(items, reverse=True))


custom_sort([6, 3, 2, 1, 4, 5])

# --------------- Whats happening ---------------

# def custom_sorted(items, reverse=False):
#     if reverse == False:
#         return sorted(items)
#     elif reverse == True:
#         return sorted(items)[::-1]
