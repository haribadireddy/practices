l=[]
n=int(input())
for i in range(1,n+1):
        name=input()
        l.append(name)

s=set(l)
print(len(s))