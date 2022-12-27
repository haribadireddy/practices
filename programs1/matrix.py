from numpy import *
arr1=array([
    [1,2,3],
    [6,4,5],
    [1,6,7]

           ])
arr2=array([
    [1,2,3],
    [6,8,5],
    [2,6,7]

           ])
m1=matrix(arr1)
m2=matrix(arr2)
print(m1*m2)