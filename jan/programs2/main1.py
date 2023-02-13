lst=[12,23,25,13,26,17,24]
s=len(lst)

a=lst[0]
b=lst[s-1]
a=b
lst[s-1]=lst[0]

print(lst)