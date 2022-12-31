def second_max(lst):
    max1 = lst[0]
    max2 = lst[0]
    for i in lst:
        if i < max1:
            max1 = i
    for j in lst:
        if max1 < j < max2:
            max2 = j
    return max1, max2

lst1 = [36,54,28,21,12,88,11,43,76]
print(second_max(lst1))