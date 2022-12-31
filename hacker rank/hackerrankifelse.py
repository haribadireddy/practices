n= int(input("enter the number: "))
if n%2==1:
    print("weird")
elif n%2==0 and 5>=n>=2:
    print("not weird")
elif n%2==0 and 20>=n>=6:
    print("weird")
else:
    print("not weird")
