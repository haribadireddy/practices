def count(str):
    greater=0
    smaller=0
    for i in str:
        if len(i)<=4:
            smaller+=1
        else:
            greater+=1
    return greater,smaller
str=["hari","pavan","sai","krishna","hokesh"]
greater,smaller = count(str)
print(greater,smaller)
