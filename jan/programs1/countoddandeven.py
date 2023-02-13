def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst =[20,25,36,47,58,79,65,44,23,21,12]
even,odd = count(lst)
print(even,odd)