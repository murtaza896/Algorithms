import math
N = int(input())

# Calculating SPF using sieve, Time = O(N.log(log(N))
p = [ 1 for _ in range(N+1)]
p[0] = 0
p[1] = 0

SPF = [0 for _ in range(N+1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if p[i] == 1:
        j = 2
        while i*j <= N:
            if p[i*j] == 1:
                SPF[i*j] = i
            p[i*j] = 0
            j += 1

for i in range(len(p)):
    if p[i] == 1:
        SPF[i] = i

# Calculating Factors and storing in a frequency map
res = {}
while N!=1:
    if SPF[N] in res:
        res[SPF[N]] += 1
    else:
        res[SPF[N]] = 1

    N = N // SPF[N]

# calculating product of powers of factors
prod = 1
for v in res.values():
    prod = prod * (v+1)

print(prod)