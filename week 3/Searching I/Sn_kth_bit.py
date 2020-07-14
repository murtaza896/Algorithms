# Sn = Sn-1 0 (Sn-1)'
def method1(n, k):
    start = 0
    end = pow(2, n+1) - 1
    bit = 0
    if k >= end:
        return -1

    while start <= end:
        mid = start + (end-start) // 2
        # print(bit, end="")

        if k == mid:
            return bit
        elif k < mid:
            end = mid - 1
        else:
            start = mid + 1
            if bit == 0:
                bit = 1
            else:
                bit = 0


    return -1

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    res = method1(n, k)
    print(res)