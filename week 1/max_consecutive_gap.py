# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

import sys
arr = list(map(int, input().split()))

mx, mn = -sys.maxsize-1, sys.maxsize
pos = 0

for x in arr:
    mx = max(mx, x)
    mn = min(mn, x)

r = mx - mn + 1
holes = [0 for _ in range(r)]

for i in range(len(arr)):
    holes[arr[i] - mn] += 1

i = 0
for count in range(r):
    while holes[count] > 0:
        holes[count] -= 1
        arr[i] = count + mn
        i += 1

print(arr)