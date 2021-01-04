# Maximize the following expression for a given array.
#     |A[i] - A[j]| + |i - j|

# total 4 case arises, turns out the 4 cases can be generated with a combination of max1, min1, max2, min2
# max1 = max val of A[i] + i, min1 = min val of A[i] + i
# max2 = max val of A[i] - i, min2 = min val of A[i] - i

import sys

arr = list(map(int, input().strip().split()))

max1, min1 = 0, sys.maxsize - 1
max2, min2 = 0, sys.maxsize - 1

for i in range(len(arr)):
    exp = arr[i] + i
    if exp > max1:
        max1 = exp
    if exp < min1:
        min1 = exp

for i in range(len(arr)):
    exp = arr[i] - i
    if exp > max2:
        max2 = exp
    if exp < min2:
        min2 = exp

res = max(abs(max1 - min1), abs(max2 - min2))
print(res)
