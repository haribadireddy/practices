def fact(n: int) -> int:
    a = 1

    for i in range(2, n + 1):
        c = a * i
        a = c
    return a


# print(fact(6))

def factorial_r(n):
    if n == 0:
        return 1
    result = n * factorial_r(n - 1)
    return result


# f(1)=1*f(0)=1*1=1
# f(2)=2*f(1)=2*1=2
# f(3)=3*f(2)=3*2=6
print(factorial_r(5))
