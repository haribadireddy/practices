import array as ar
vals=ar.array("i",[3,4,7,8,1,2,6])
newarr = ar.array(vals.typecode, (a for a in vals))
for i in newarr:
    print(i)