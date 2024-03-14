#WAP which takes a sequence of numbers and check if all numbers are unique
import numpy as np

def unique_element(my_list):
    if(len(my_list))==len(set(my_list)):
        return True
    else:
        return False
    
arr1 = np.array([1,6,5,8])
arr2 = np.array([2,2,5,5,7,8])

print(unique_element(arr1))
print(unique_element(arr2))

