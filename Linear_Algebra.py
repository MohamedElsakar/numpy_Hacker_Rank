import numpy as np


A=int(input())
arr=np.array([list(map(float,input().split())) for _ in range(A)],dtype=float)    
print("{:0.2}".format(np.linalg.det(arr)))