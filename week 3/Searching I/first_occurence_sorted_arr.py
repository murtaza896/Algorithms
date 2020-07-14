# Given an array(N) find the first occurence of x in the array
# Time complexity = O(log(N))

def method1(arr, x):
    start = 0
    end = len(arr)
    mid = -1

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] == x:
            if mid - 1 >=0 and arr[mid-1] == x:
                end = mid - 1
            else:
                return mid

        elif arr[mid] > x:
            end = mid - 1

        elif arr[mid] < x:
            start = mid + 1

    return -1

if __name__== "__main__":
    arr = list(map(int, input().split()))
    x = int(input())

    print(method1(arr, x))