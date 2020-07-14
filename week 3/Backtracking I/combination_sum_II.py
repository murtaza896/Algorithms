def combination_sum(candidates, target):

    res = []
    if len(candidates) == 0:
        return res

    candidates.sort()

    def solve(elems, t, x, comb):
        if t < 0:
            return
        elif t == 0:
            res.append(comb)
        else:
            for i in range(x, len(elems)):
                if i > x and elems[i] == elems[i-1]:
                    continue
                solve(elems, t-elems[i], i+1, comb+[elems[i]])
        return

    solve(candidates, target, 0, [])

    return res

if __name__ == "__main__":
    candidates = list(map(int, input().split()))
    target = int(input())

    res = combination_sum(candidates, target)
    print(res)
