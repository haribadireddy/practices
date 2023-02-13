def fact(n):
   a=1

   for i in range(2,n+1):
      c=a*i
      a=c
   print(a)
fact(6)
