# https://www.spoj.com/problems/AGGRCOW/
# https://www.youtube.com/watch?v=TC6snf6KPdE

# method 1 T: O(nlogn) | S: O(n)
def method1(A,B):
    A.sort()

    def is_ans(x):
        cows = B - 1
        i = 0

        print("mid=", x, end=": ")
        while(cows > 0 and i < len(A)):
            for j in range(i, len(A)):
                if (A[j] - A[i] >= x):
                    print(j, end = " ")
                    cows -= 1
                    i = j
                    break
                if j == len(A) - 1:
                    i = len(A)
        print()
        if cows <= 0:
            return True
        else:
            return False


    l = 1
    h = A[-1]

    while(l<=h):
        m = (l+h)//2

        print(l, m, h)

        x = is_ans(m)
        y = is_ans(m+1)

        print(x, y)
        print()
        if (x == True and y == False):
            return m
        elif x == True:
            l = m + 1
        elif x == False:
            h = m - 1


if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())

    res = method1(A, B)
    print(res)