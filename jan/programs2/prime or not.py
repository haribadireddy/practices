from math import sqrt
num = int(input("enter the no: "))
checktill=int(sqrt((num)))+1
for i in range(2,checktill):
    if num%i==0:
        print(num , "is not a prime")
        break
else:
        print(num , "is a prime")