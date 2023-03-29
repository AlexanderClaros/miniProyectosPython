import math
def bubbleSort(nums):

    intercambio = True
    while intercambio:
            intercambio=False
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    intercambio =True


lista = [8,5,4,1,9,56,21,65,15]
print(len(lista))
bubbleSort(lista)
print(lista)
print(49**(0.5))
