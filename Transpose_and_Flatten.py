# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
nums=tuple(map(int,input().split()))
r=nums[0]
c=nums[1]

flatten=list(map(int,input().split()))
for i in range(1,r):
    nums=list(map(int,input().split()))
    flatten=np.concatenate((flatten,nums))

arr=flatten.reshape(r,c)
transpose =np.transpose(arr)

print(transpose)
print(flatten)