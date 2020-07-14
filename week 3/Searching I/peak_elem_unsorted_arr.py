# https://leetcode.com/problems/find-peak-element/
def method1(arr):
    start = 0
    end = len(arr)-1

    if len(arr) == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return len(arr)-1

    while start<=end:
        mid = start + (end-start) // 2

        if arr[mid-1] <= arr[mid] >= arr[mid+1]:
            return mid
        elif arr[mid-1] > arr[mid] > arr[mid+1]:
            end = mid - 1
        else:
            start = mid + 1


    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(method1(arr))


