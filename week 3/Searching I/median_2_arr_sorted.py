# https://www.youtube.com/watch?v=LPFhl65R7ww
# Given 2 sorted arrays, find the median of the final array without merging the two.

# Method1: Binary Search. T: O(log(min(m,n)) | S: O(1)
def method1(arr1, arr2):
    m, n = len(arr1), len(arr2)
    l, h = 0, min(m, n)

    if m <= n:
        X = arr1
        Y = arr2
    else:
        X = arr2
        Y = arr1

    while (l <= h):

        mid = (l+h) // 2
        y = (m+n+1)//2 - mid

        if mid == 0: maxLeftX = -99999
        else: maxLeftX = X[mid - 1]

        if mid == len(X): minRightX = 99999
        else: minRightX = X[mid]

        if y == 0: maxLeftY = -99999
        else: maxLeftY = Y[y-1]

        if y == len(X): minRightY = 99999
        else: minRightY = Y[y]

        print(l, mid,y, h)

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m+n)%2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)

        elif maxLeftX > minRightY:
            h = mid - 1
        else:
            l = mid + 1

if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    res = method1(arr1, arr2)

    print(res)