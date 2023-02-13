def Tuple(lst: list[tuple[str, float]]):
    lst = []
    for i in range(int(input("enter the no of students: "))):
        name = input("enter the name: ")
        score = input("enter the score: ")
        t = name, score
        lst.append(t)
    t1=lst[0]
    print(t1[1])
    return lst[0][1]


print(Tuple(li))
