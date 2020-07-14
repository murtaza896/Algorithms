# Given an array, print count of all the triplets whose sum is divisible by 'k'
# https://www.interviewbit.com/problems/size-three-subsequences-divisible-by-b/



# using remainder count array, then traversing based on conditions
# Time = o(N^2) | Space = O(m)

def method1(arr, m):
    dic = [0] * m
    mod = int(1e+9 + 7)

    for elem in arr:
        dic[elem % m] += 1

    # print(dic)

    ans = 0
    for i in range(0, m):
        for j in range(i, m):
            r1 = (i+j) % m
            k = (m - r1) % m

            # since j begins from i, and k<j,
            # it means we have covered all cases for j, previously,
            # so need not to compute again.
            if k<j:
                continue

            # case 1: a + a + a
            elif i==j and j==k:
                ans += dic[i] * (dic[i]-1) * (dic[i] - 2) // 6

            # case 2: a + a + b
            elif i==j:
                ans += (dic[i] * (dic[i]-1) // 2) * dic[k]
            elif i==k:
                ans += (dic[i] * (dic[i]-1) // 2) * dic[j]
            elif j==k:
                ans += (dic[j] * (dic[j]-1) // 2) * dic[i]

            # case 3: a + b + c
            else:
                ans += dic[i] * dic[j] * dic[k]

    return ans % mod

# Using sorting and two pointer approach.
# Time = O(N^2) | Space = O(1)
# [Not possible because after modulo a sorted input need not remain sorted]

# def method2(arr, m):
#     arr.sort()
#     n = len(arr)
#     cnt = 0
#     mod = int(1e+9 + 7)
#     for i in range(0, n):
#         x = arr[i]
#         l = i
#         r = n-1
#         while l<=r:
#             sm = x%m + arr[l]%m + arr[r]%m
#             if sm % m == 0:
#                 cnt += 1
#                 l += 1
#                 r -= 1
#             elif sm % m > 0:
#                 r -= 1
#             else:
#                 l += 1
#     return cnt % mod

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    m = int(input())

    print(method1(arr, m))
    # print(method2(arr, m)) [Not possible]

