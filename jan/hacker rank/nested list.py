#def topper(lst:list[tuple[str,float]])
def second_min(lst:list[tuple[str,float]]):
    lowest = 1000
    second_lowest = 1000
    for i in lst:
        if i < lowest:
            lowest = i
    for j in lst:
        if lowest < j < second_lowest:
            second_lowest = j
    return lowest, second_lowest

def find_max(lst):
    max=-1000
    max_tuple=None
    for t in lst:
        if t[1]>max:
            max=t[1]
            max_tuple=t
    return max_tuple


def school_rank(n):
    lst = []

    for i in range(n):
        name = str(input("enter the name: "))
        marks = float(input("enter the marks: "))
        t = (name, marks)
        lst.append(t)
        # lst2.append(marks)
    # print(lst1,lst2)
    #lowest, second_lowest = second_min(lst)
    max=find_max(lst)
    return max[0]


n = int(input("enter the no of students: "))
print(school_rank(n))
