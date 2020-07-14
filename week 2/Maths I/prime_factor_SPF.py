# Prime Factorization using SPF

import math
N = int(input())

# use sieve to store the SPF. T = O(N.log(log(N)))
p = [1 for _ in range(N+1)]
p[0] = 0
p[1] = 0

SPF = [0 for _ in range(N+1)]
SPF[0] = 0
SPF[1] = 0

for i in range(2, int(math.sqrt(N))+1):
    if p[i] == 1:
        j = 2
        while i*j<=N:
            if p[i*j] == 1:
                SPF[i*j] = i
            p[i*j] = 0
            j += 1



for i in range(len(SPF)):
    if p[i] == 1:
        SPF[i] = i


# Get the prime factorization in Time = O(log(N))
res = []
while N!=1:
    res.append(SPF[N])
    N = N // SPF[N]

print(res)