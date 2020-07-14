# Given an array, find the majority element in the array
# Majority element is any element which appears more than len(arr)/3 times in the array
# https://leetcode.com/problems/majority-element-ii

# Method 1: Time = O(N) | Space = O(1) BOYER-MOORE MAJORITY VOTE ALGORITHM
def majorityElement(self, arr: List[int]) -> List[int]:
    candidate1, candidate2 = 0, 0
    count1, count2 = 0, 0

    for i in range(len(arr)):

        if arr[i] == candidate1:
            count1 += 1
        elif arr[i] == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = arr[i]
            count1 += 1
        elif count2 == 0:
            candidate2 = arr[i]
            count2 += 1
        else:
            count1, count2 = count1 - 1, count2 - 1
        # print(count1, count2)

    count1, count2 = 0, 0
    print(candidate1, candidate2)

    for x in arr:
        if x == candidate1:
            count1 += 1
        if x == candidate2:
            count2 += 1
    print(count1, count2)

    res = set()
    n = len(arr)

    if count1 > n//3:
        res.add(candidate1)

    if count2 > n//3:
        res.add(candidate2)

    return list(res)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    majorityElement(arr)