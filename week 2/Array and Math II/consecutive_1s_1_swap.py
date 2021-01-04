# Calculate the maximum length of consecutive 1s, after atmost 1 swap operations in the given Binary string
# https://www.geeksforgeeks.org/length-of-longest-consecutive-ones-by-at-most-one-swap-in-a-binary-string/
# https://leetcode.com/problems/max-consecutive-ones-ii/

# method 1: Time = O(N) | Space = O(2N)
def method1(arr):
    tot_1 = arr[0]

    # compute the prefix length sum arr
    maxL = [0 for _ in range(len(arr))]
    maxL[0] = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == 0:
            maxL[i] = 0
        else:
            tot_1 += 1
            maxL[i] = maxL[i-1] + 1

    # compute the suffix length sum arr
    maxR = [0 for _ in range(len(arr))]
    maxR[-1] = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] == 0:
            maxR[i] = 0
        else:
            maxR[i] = maxR[i+1] + 1
    # print(maxL)
    # print(maxR)
    # print(tot_1)

    # compute the result max(L+R+1) or max(L+R) based on the availability of extra 1s for swapping
    length = -1
    for i in range(1, len(arr)-1):
        L, R = maxL[i-1], maxR[i+1]
        if arr[i] == 0:
            if (L+R) != tot_1:
                length = max(length, L+R+1)
            else:
                length = max(length, L+R)
    
    if length == -1:
        print(tot_1)
    else:
        print(length)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    method1(arr)