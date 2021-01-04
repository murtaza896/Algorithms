# Given an unsorted array of integers, find the first missing positive integer
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
# https://leetcode.com/problems/first-missing-positive/

# Most efficient method: Time=O(N) | Space=O(1)
# segregate all non-positive elements to the left
# operate on the remaining size of the array, marking the visited nodes as negative
# now the node consisting of positive value is the one which didnt get visited, which is because of the absence of its index value + 1 in the array

def segregate(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            j += 1
    return j

def missingPositive(arr):

    shift = segregate(arr)

    size = len(arr) - shift
    arr = arr[shift:]

    for i in range(size):
        if abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i])-1] *= -1

    for i in range(size):
        if arr[i] > 0:
            return i + 1
    return size + 1

if __name__== "__main__":
    arr = list(map(int, input().split()))
    print(missingPositive(arr))