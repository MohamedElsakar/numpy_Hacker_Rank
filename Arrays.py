import numpy 

def arrays(arr):
    # complete this function
    # use numpy.array
    a=numpy.array(arr,dtype=float)[::-1]
    return a
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)