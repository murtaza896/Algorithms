import math

N = int(input())
arr = []
M = N

# Effective Time complexity = O(sqrt(N))
for i in range(2, int(math.sqrt(M))+1):
    while N%i == 0:
        arr.append(i)
        N = N//i
if N!=1:
    arr.append(N)

print(arr)