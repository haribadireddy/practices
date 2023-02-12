students=[]
scores=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
min1 = scores[0]
min2 = scores[0]
for i in scores:
        if i < min1:
                min1=i
for j in scores:
        if min1<j<min2:
                min2=j
lowest = [p[0] for p in students if p[1] == min2]
for p in sorted(lowest):
        print(p)




