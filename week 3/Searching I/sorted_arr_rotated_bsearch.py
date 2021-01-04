# Given a sorted array(N) rotated by some number, find element x in the array using binary search
# Time Complexity = O(log(N))

def method1(arr, x):
    # finding the point of rotation
    cnt = 0
    if len(arr) == 0:
        return -1

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            cnt = i + 1
            break

    start = 0
    end = len(arr)

    while start <= end:
        mid = start + (end-start)//2

        pos = (mid + cnt)%len(arr)
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            start = mid + 1
        elif arr[pos] > x:
            end = mid - 1

    return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())

    print(method1(arr, x))
