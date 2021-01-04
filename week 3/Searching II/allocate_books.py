# https://www.geeksforgeeks.org/allocate-minimum-number-pages/
# https://www.interviewbit.com/problems/allocate-books/

import sys

# T: O(nlogn) | S: O(1)
def books(A, B):
    l = A[-1]
    h = sum(A)

    prefix = [0]
    for f in range(len(A)):
        prefix.append(prefix[f] + A[f])

    def is_ans(x):
        std = 1
        i = 0
        sm = 0
        while i<len(A):
            if sm + A[i] > x:
                std += 1
                sm = A[i]
                if std > B:
                    return False
            else:
                sm += A[i]

            i += 1

        return True

    res = sys.maxsize

    while(l<=h):
        m = (l + h)//2
        print(l, m, h)

        x = is_ans(m)

        print(x)

        if x == True:
            res = m
            h = m - 1
        elif x == False:
            l = m + 1

    return res

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())

    res = books(A, B)

    print(res)