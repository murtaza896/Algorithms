# Given an array, count the no. of pairs having their sum divisible by 'm'
# https://www.interviewbit.com/problems/count-pairs-in-array-whose-sum-is-divisible-by-the-given-number/
# https://www.geeksforgeeks.org/count-number-of-pairs-in-array-having-sum-divisible-by-k-set-2/

# Time = O(N) Space = O(1)
arr = list(map(int, input().split()))
m = int(input())

dic = [0]*m

for elem in arr:
    dic[elem % m] += 1

res = 0
res += dic[0] * (dic[0] - 1) // 2

for x in range(1, m//2):
    res += dic[x] * dic[m - x]

if m%2 == 0:
    res += dic[m//2] * (dic[m//2] - 1) // 2
else:
    res += dic[m//2] * dic[m//2 + 1]

print(res)
