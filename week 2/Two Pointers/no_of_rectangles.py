A = list(map(int, input().split()))
B = int(input())

i = 0
j = 0
cnt = 0

while i<=j and i<len(A) and j<len(A):
    area = A[i]*A[j]
    print(i, j, area)
    if area < B:
        cnt += 2
        if i == j:
            cnt -= 1
    j += 1
    if j==len(A):
        i += 1
        j = i

print(cnt)