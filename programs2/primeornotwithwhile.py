n=int(input("enter the number: "))
i=2
while i<=n-1:
    if n%i==0:
        print(n, "is not a prime number")
        break
    i += 1
else:
    print(n , "is a prime number")

