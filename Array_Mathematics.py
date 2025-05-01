import numpy as np
R,C=list(map(int,input().split()))



#arr1=list(map(int,input().split()))
#arr2=list(map(int,input().split()))

arr1=np.array([list(map(int,input().split())) for _ in range(R)],dtype=int)    
arr2=np.array([list(map(int,input().split())) for _ in range(R)],dtype=int)

print(np.add(arr1,arr2))                            #print(arr1+arr2)
print(np.subtract(arr1,arr2))                       #print(arr1-arr2)
print(np.multiply(arr1,arr2))                       #print(arr1*arr2)
print(np.floor_divide(arr1,arr2))                   #print(arr1//arr2)
print(np.mod(arr1,arr2))                            #print(arr1%arr2)
print(np.power(arr1,arr2))                            #print(arr1**arr2)
