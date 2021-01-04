def gcd(A, B):
    if A == 0:
        return B
    else:
        return gcd(B%A, A)

def solution():
    N = list(map(int, input().split()))

    if len(N) == 1:
        if N[0] == 1:
            return 1
        else:
            return 0

    if len(N) == 2:
        if gcd(N[0], N[1]) == 1:
            return 1
        else:
            return 0


    g = gcd(N[0], N[1])
    for i in range(2, len(N)):
        g = gcd(g, N[i])
        if g==1:
            return 1
    return g

if __name__ == "__main__":
    print(solution())