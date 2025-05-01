import numpy as np

N=int(input())
arr1=np.array([list(map(int,input().split())) for _ in range(N)],dtype=int)    
arr2=np.array([list(map(int,input().split())) for _ in range(N)],dtype=int)   


print(np.dot(arr1,arr2))

#result_1 = np.dot(matrix_a, matrix_b)
