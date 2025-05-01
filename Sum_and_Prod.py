# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

R,C=list(map(int,input().split()))

arr=np.array([list(map(int,input().split())) for i in range(R)])


#print(arr)


sum=np.sum(arr,axis=0)
#print(sum)
pro=np.prod(sum)
print(pro)
#arr1=np.array([list(map(int,input().split())) for _ in range(R)],int)    
