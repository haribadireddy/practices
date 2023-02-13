def armstrong_number(z):
    for i in range(a):

        num = i
        result = 0
        n = len(str(i))
        while i != 0:
            digit = i % 10
            result += digit ** n
            i = i // 10
        if num == result:
            print(num)


a = int(input("enter the range of numbers: "))
armstrong_number(a)
