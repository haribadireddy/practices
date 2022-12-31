from typing import List


def get_top_two(lst: List) -> tuple[int, int]:
    max1 = -1000
    max2 = -1000
    for i in lst:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i

    return max1, max2


def runner_up(n: int) -> int:
    lst = []
    for i in range(n):
        s = int(input("enter the score: "))
        lst.append(s)
    print(lst)
    winner, runner = get_top_two(lst)
    return runner


a = int(input("enter the number: "))
print(runner_up(a))

