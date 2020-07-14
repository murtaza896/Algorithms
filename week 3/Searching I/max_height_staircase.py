# https://www.interviewbit.com/problems/maximum-height-of-the-staircase/
# Time Complexity = O(N)
def method1(n):
    b = 1
    sm = 0
    cnt = -1

    while sm <= n:
        sm += b
        b += 1
        cnt += 1

    return cnt

# Binary Search
# Time Complexity = O(log(N))
def method2(n):
    def func(m):
        return m*(m+1) // 2

    start, end = 1, n
    while start <= end:
        mid = start + (end-start)//2

        if func(mid) <= n and func(mid+1) > n:
            return mid
        elif func(mid) > n:
            end = mid - 1
        else:
            start = mid + 1

    return 0

# Binary Search
# My method
def method3(n):
    x = h = 1
    while(x <= n):
        x = h*(h+1) // 2

        if x == n:
            return h
        elif x < n:
            h += 1
        elif x > n:
            return h-1

if __name__ == "__main__":
    n = int(input())
    res = method2(n)
    res2 = method3(n)
    print(res, res2)