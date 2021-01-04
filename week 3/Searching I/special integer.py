def solve(A, B):

    prefix = [0]

    for i in range(len(A)):
        prefix.append(prefix[i] + A[i])

    def check_sum(x):
        p1 = 0
        p2 = x
        while(p2 <= len(A)):
            sm_x = prefix[p2] - prefix[p1]

            if sm_x > B:
                return False
            else:
                p1 += 1
                p2 += 1

        return True

    l = 1
    h = len(A)

    while(l <= h):
        m = (l + h) // 2

        if check_sum(m):
            l = m + 1
        else:
            h = m - 1

    return l-1

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())

    res = solve(A, B)

    print("ans: ",res)