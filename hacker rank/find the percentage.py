n = int(input())
students = {}
for i in range(n):
    line = input().split(" ")
    name = line[0]
    marks = list(map(float, line[1:4]))
    students[name] = marks
query_name = input()
print(students)

print(students[query_name])
add = sum(students[query_name])
result = add / len(students[query_name])
print("%.2f" % result)

print(students)

"""n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
add=sum(student_marks[query_name])
result=add/len(student_marks[query_name])
print("%.2f" % result)"""
