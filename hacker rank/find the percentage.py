n=int(input("enter the no of students: "))
students={}
for i in range(n):
    name=input("enter the name:")
    for j in range(3):
        marks=input("enter the marks")
        students[name]=marks

print(students)



