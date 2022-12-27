import array as ar
arr=ar.array("i",[])
n= int(input("enter the length of the array "))
for i in range(n):
     x=int(input("enter the next value: "))
     arr.append(x)
print(arr)