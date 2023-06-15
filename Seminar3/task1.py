my_list = [1, 1, 1, 2, 2, 3, 4, 4, 7, 7, 7, 5, 6]

COUNT = 1

for val in my_list:
    if my_list.count(val) > COUNT:
        for _ in range(COUNT):
            my_list.remove(val)
print(my_list)
