def diff_k(arr, k):
    # arr is sorted
 
    i = 0
    j = 1

    res = []

    while i<j and i<len(arr) and j<len(arr):
        diff = arr[j] - arr[i]
        if diff < k:
            j += 1
        elif diff > k:
            i += 1
            if i == j:
                j += 1
        else:
            res.append([i, j])
            i += 1
            j += 1

    return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(diff_k(arr, k))
