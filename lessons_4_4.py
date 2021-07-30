numbers_list = [2, 3, 3, 7, 23, 1, 44, 44, 3, 2, 7, 4, 11]
result = [x for x in numbers_list if numbers_list.count(x) == 1]
print(result)
