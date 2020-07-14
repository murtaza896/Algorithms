# Given an array, print all the triplets whose sum is equal to 'k'
# https://www.geeksforgeeks.org/print-all-triplets-with-given-sum/

# Using Set, Time = O(N^2) | Space = O(N)
def method1(A, k):
    res = []
    for i in range(0, len(A) - 1):
        s = set()
        curr_sum = k - A[i]

        for j in range(i+1, len(A)):
            target = curr_sum - A[j]
            if target in s:
                res.append((A[i], A[j], target))
            s.add(A[j])

    return res

# Using Sorting, Time = O(N^2) | Space = O(1)
def method2(A, k):
    # Use set for storing unique triplets, else use list.
    res = set()
    A.sort()
    n = len(A)

    for i in range(0, n-1):
        l = i + 1
        r = n - 1
        x = A[i]

        while (l < r):
            if x + A[l] + A[r] == k:
                res.add((x, A[l], A[r]))
                l += 1
                r -= 1
            elif x + A[l] + A[r] < k:
                l += 1
            else:
                r -= 1
    return res

if __name__ == "__main__":
    A = list(map(int, input().split()))
    k = int(input())

    # print(method1(A, k))
    print(method2(A, k))