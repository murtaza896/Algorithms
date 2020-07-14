# https://www.interviewbit.com/problems/painters-partition-problem/

# T: O(nlogn) | S: O(1)
def solution(A, B, C):
    l = max(C)
    h = sum(C)

    def is_ans(board_sum, A):
        sm = 0
        for i in range(len(C)):

            if C[i] > board_sum:
                return False

            if sm + C[i] > board_sum:
                sm = C[i]
                A -= 1
                if A <= 0:
                    return False
            else:
                sm += C[i]

        return True

    res = 10**9
    while(l<=h):
        m = (l+h)//2
        board_sum = m

        if is_ans(board_sum, A):
            res = min(res, m)
            h  = m - 1
        else:
            l = m + 1

    return B*res%10000003



if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = list(map(int, input().split()))

    res = solution(A, B, C)
    print(res)