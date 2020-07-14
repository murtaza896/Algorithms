# https://leetcode.com/problems/smallest-good-base/

import math
def smallestGoodBase(n: str) -> str:
    n = int(n)
    mx = int(math.log(n, 2))

    def ans(num, ones):
        l = 2
        h = num

        while(l<=h):
            m = (l+h)//2

            s=0
            for i in range(ones):
                s += int(m ** i)

            if s==num:
                return m
            elif s < num:
                l = m + 1
            elif s > num:
                h = m - 1

        return -1


    for i in range(mx+1, 1, -1):
        res = ans(n, i)
        if res > 0:
            return str(res)

if __name__ == "__main__":
    n = input()
    res = smallestGoodBase(n)
    print(res)
