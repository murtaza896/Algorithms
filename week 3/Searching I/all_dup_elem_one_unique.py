# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Bit manipulation
# Time complexity = O(N)
def method1(arr):

    elem = 0
    for i in range(len(arr)):
        elem = elem ^ arr[i]

    return elem

# Binary Search
# Time Complexity = O(log(N))
def method2(arr):
    if len(A) == 1:
        return A[0]
    if A[0] != A[1]:
        return A[0]
    if A[-1] != A[-2]:
        return A[-1]

    low, high = 0, len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
            return A[mid]
        if A[mid] == A[mid - 1]:
            mid = mid - 1

        left = mid - low
        if left % 2 == 0:
            low = mid + 2
        else:
            high = mid - 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = method2(arr)

    print(res)