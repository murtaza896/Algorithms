res = []
def P(elems, x):

    if x == len(elems) - 1:
        res.append(elems)

    else:
        for i in range(x, len(elems)):
            if i > x and elems[i] == elems[i-1]:
                continue

            elems[i], elems[x] = elems[x], elems[i]
            P(elems[:], x+1)
            elems[i], elems[x] = elems[x], elems[i]

if __name__ == "__main__":
    ip = list(map(int, input().split()))

    P(ip, 0)

    res.sort()
    print(res)