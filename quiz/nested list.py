students = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    scores.append(score)
min1 = scores[0]
min2 = scores[0]
for i in scores:
    if i < min1:
        min1 = i

for j in scores:
    if min1 < j < min2:
        min2 = j
second_lowest = []
for s in students:
    if s[1] == min2:
        second_lowest.append(s[0])
# lowest = [p[0] for p in students if p[1] == min2]
for p in sorted(second_lowest):
    print(p)
