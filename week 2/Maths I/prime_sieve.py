import math

N = int(input())

prime = [1] * (N+1)

prime[0] = 0
prime[1] = 0

for i in range(2, int(math.sqrt(N))+1):
    if prime[i] == 1:
        j = 2
        while j*i <= N:
            prime[j*i] = 0
            j += 1

for i in range(len(prime)):
    if prime[i] == 1:
        print(i, end=" ")