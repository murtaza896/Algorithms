import sys
import math

N = int(input())

for i in range(2, int(math.sqrt(N))+1):
    if N%i == 0:
        print("Not a prime")
        sys.exit()
print("Prime")