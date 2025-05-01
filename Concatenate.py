import numpy as np
nums=list(map(int,input().split()))
r=nums[0]+nums[1]
c=nums[2]

arr=list(map(int,input().split()))
for i in range(1,r):
    nums=list(map(int,input().split()))
    arr=np.concatenate((arr,nums))


arr=np.reshape(arr,(r,c))
print(arr)
