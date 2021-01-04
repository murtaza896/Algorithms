# Given a sorted matrix, such that all its row are sorted in asc, and columns are sorted in asc too, find the given Target value in the matrix.
# https://leetcode.com/problems/search-a-2d-matrix-ii/

def matrixSearch(arr, target) -> bool:

    if not arr or not arr[0]:
        return False

    m = len(arr)
    n = len(arr[0])

    i, j, k = 0, n-1, target

    while i < m and j >= 0:
        if arr[i][j] == k:
            return True
        elif arr[i][j] > k:
            j -= 1
        elif arr[i][j] < k:
            i += 1

    return False

if __name__ == "__main__":
    m, n = int(input()), int(input())
    arr = []

    for i in range(m):
        arr.append(list(map(int, input().split())))

    print(arr)

    target = int(input("enter the target value:"))
    if matrixSearch(arr, target):
        print("true")
    else:
        print("false")