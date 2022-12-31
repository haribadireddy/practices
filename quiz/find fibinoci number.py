def fib(n: int) -> int:
    a = 0
    b = 1
    c = 1
    # print(a)
    # print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


# print(fib(int(input("enter the number:"))))


def fib_recursion(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    result = fib_recursion(n - 1) + fib_recursion(n - 2)
    return result


# if n==3:f(2)+f(1)=1+0=1
# if n==4:f(3)+f(2)=1+0+1=2
# if n==5::f(4)+f(3)=f(3)+f(2) +1=1+1+1=3
print(fib_recursion(8))
