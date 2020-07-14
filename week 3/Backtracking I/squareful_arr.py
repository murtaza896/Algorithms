import math

def squareful_arr(arr):

    cnt = 0

    def isPerfectSquare(x):
        y = math.sqrt(x) // 1
        if x % y == 0:
            return True
        return False

    def check(elems):
        for i in range(len(nums)-1):
            if isPerfectSquare(elems[i] + elems[i+1]):
                cnt += 1


    def P(elems, x):
        if x == len(elems) - 1:
            check(elems)
        else:
            for i in range(x, len(nums)):

                if i > x and elems[i] == elems[i-1]:
                    continue

                elems[i], elems[x] = elems[x], elems[i]
                P(elems[:], x+1)
                elems[i], elems[x] = elems[x], elems[i]

    P(arr, 0)

    return cnt

if __name__ == "__main__":
    A = list(map(int, input().split()))
    res = squareful_arr(A)
    print(res)