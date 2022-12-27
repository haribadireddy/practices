lst=[1,3,4,6,2,70,90,77,65,54,103]
max1=lst[0]
max2=lst[0]
for i in lst:
    if i>max1:
        max1=i
for i in lst:
    if max1>i>max2:
        max2=i

print(max1)
print(max2)