# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 
numpy.set_printoptions(legacy='1.13')

nums=tuple(map(int,input().split()))
arr=numpy.eye(nums[0],nums[1],dtype=float)
print(arr)


