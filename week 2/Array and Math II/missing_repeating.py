# Given an array of size N, having elements in the range of 1 to N, except for any one element missing and one element repeated
# find the missing and repeated number
# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

# Method 3: T = O(2N) | S = O(1) | input array is altered
def method3(arr):
    # traverse the array using elem as index, and mark as negative for indicating status=visited

    r, m = 0, 0     # r = repeating elem, m = missing elem

    for i in range(len(arr)):
        if arr[i] > 0:
            arr[arr[i] - 1] *= -1
        else:
            r = i + 1

    # traverse the array looking for only positive elem, i.e. the element who could not be visited because its index is not in the array, thus missing elem
    for i in range(len(arr)):
        if arr[i] > 0:
            m = i + 1

    print(r, m)

def method5(arr):
    xor1 = 0
    for i in range(len(arr)):
        xor1 = xor1 ^ arr[i] ^ i

    

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    method3(arr)