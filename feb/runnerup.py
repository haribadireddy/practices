n=int(input())
arr=map(int,input().split())
max1 = -1000
max2 = -1000
for i in arr:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i

print(max2)