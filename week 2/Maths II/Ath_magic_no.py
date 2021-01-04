# find the Ath magic number: a number who is either a power of 5 or sum of unique powers of 5.

def magic_no(n):
    res = [5]
    p = 2

    while len(res) <= n:
        x = 5 ** p
        res.append(x)
        l = len(res)
        for i in range(l-1):
            res.append(x + res[i])
        p += 1

    return res


if __name__ == "__main__":
    n = int(input())
    res = magic_no(n)
    print(res[n-1])


