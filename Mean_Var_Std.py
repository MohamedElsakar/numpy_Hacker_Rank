import numpy as np

n,m=list(map(int,input().split()))

arr=np.array([list(map(int,input().split())) for _ in range(n)],dtype=int)    


print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
arr1=np.std(arr)
print(arr1.round(12))
