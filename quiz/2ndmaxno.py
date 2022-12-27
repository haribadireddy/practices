def second_max(lst):
    max1 = lst[0]
    max2 = lst[0]
    for i in lst:
        if i > max1:
            max1 = i
    for j in lst:
        if max1 > j > max2:
            max2 = j
    return max1, max2


lst1 = [1, 3, 4, 6, 2, 70, 90, 90, 77, 65, 54, 103]
print(second_max(lst1))
print(second_max([20, 40, 2, 30, 1, 40]))
