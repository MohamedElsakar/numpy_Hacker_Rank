import numpy as np

R,C=list(map(int,input().split()))

arr=np.array([list(map(int,(input().split()))) for i in range(R)])


arr1=np.min(arr,axis=1)
#print(arr1)
arr2=np.max(arr1)
print(arr2)