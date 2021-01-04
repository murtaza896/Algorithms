# Given an array, find the majority element in the array
# Majority element is any element which appears more than len(arr)/2 times in the array
# https://leetcode.com/problems/majority-element/
# https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

# Method 1: Time = O(N log N) | Space = O(1) Sort the array, majority elem should be in middle.

# Method 2: Time = O(N) | Space = O(1) BOYER-MOORE MAJORITY VOTE ALGORITHM
def method1(arr):
    me = arr[0]
    c = 0

    for i in range(len(arr)):
        if c==0:
            me = arr[i]

        if arr[i] == me:
            c += 1
        else:
            c -= 1

    c=0
    for i in range(len(arr)):
        if arr[i] == me:
            c += 1

    if c > len(arr)//2:
        return me
    else:
        return -1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(method1(arr))