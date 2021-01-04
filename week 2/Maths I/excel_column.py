N = int(input())

res = []

while N > 0:
    rem = N % 26
    if rem == 0:
         res.append('Z')
         N = N//26 - 1
    else:
        res.append(chr((rem-1) + ord('A')))
        N = N//26

res = res[::-1]
print("".join(res))

