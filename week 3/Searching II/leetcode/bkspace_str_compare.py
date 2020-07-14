# https://leetcode.com/problems/backspace-string-compare/
# https://leetcode.com/problems/backspace-string-compare/discuss/570743/O(orSor%2BorTor)-time-or-O(1)-extra-space-or-eAsY-tO-uNdErStAnD

def backspaceCompare(S: str, T: str) -> bool:
    def next(s, i):
        d = 0
        while i >= 0 and (s[i] == '#' or d > 0):
            if s[i] == '#':
                d += 1
            else:
                d -= 1
            i -= 1
        return i

    i = next(S, len(S) - 1)
    j = next(T, len(T) - 1)
    while i >= 0 and j >= 0 and S[i] == T[j]:
        i = next(S, i - 1)
        j = next(T, j - 1)
    return i < 0 and j < 0

if __name__ == "__main__":
    S = input()
    T = input()

    res = backspaceCompare(S, T)
    print(res)