def bublesort(nums):
    comprobar = True
    while comprobar:
        comprobar=False
        for i in range (len(nums)-1):
            if nums[i]> nums[i+1]:
                nums[i],nums[i+1]= nums[i+1],nums[i]
                comprobar=True
list=[1,5,4,3,8,45,95,25,14]
print(list)
bublesort(list)
print(list)
