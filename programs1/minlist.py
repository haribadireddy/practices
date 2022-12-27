nums=[1,20,30,4,5,6,90,103,4,5,6,7]
min=nums[0]
max=nums[0]
for num in nums:
    if num < min:
        min=num
    if num>max:
            max=num
print(min)
print(max)