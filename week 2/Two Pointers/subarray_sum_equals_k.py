def method1(arr, k):
    i = 0
    j = 0
    s = arr[0]
    cnt = 0

    while i<len(arr):

        if s == k:
            cnt += 1
            j += 1
            if j<len(arr):
                s += arr[j]
        elif s < k:
            j += 1
            if j<len(arr):
                if arr[j] > 0:
                    s += arr[j]
                else:
                    s -= arr[i]
                    i += 1
                    s += arr[j]
                    j += 1
        elif s > k:
            s -= arr[i]
            i += 1

    return cnt

def method2(arr, k):
    s = 0
    dic = {0:1}
    cnt = 0

    for n in arr:
        s += n
        if dic.get(s-k) != None:
            cnt += dic[s-k]
        if dic.get(s) != None:
            dic[s] += 1
        else:
            dic[s] = 1
    return cnt

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(method2(arr, k))
