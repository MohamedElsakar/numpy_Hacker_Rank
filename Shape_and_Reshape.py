# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
arr=input().split()
a=np.array(arr,dtype=int)
print(a.reshape(3,3))
