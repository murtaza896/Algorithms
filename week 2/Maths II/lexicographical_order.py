# Print all the possible permutations of given string, in lexicographical order



# Time = O(n!*n) | Space = O(1)
# https://www.geeksforgeeks.org/lexicographic-rank-of-a-string/
# https://www.geeksforgeeks.org/lexicographic-permutations-of-string/

import sys
def method1(str):
    A = list(str.upper())
    B = sorted(A, reverse = True)
    A.sort()

    print("".join(A))

    while A!=B:
        pos1 = pos2 = 0

        for i in range(len(A) - 1):
            if A[i] < A[i+1]:
                pos1 = i

        pos2 = pos1
        mpos2 = 'Z'

        for i in range(pos1+1, len(A)):
            if A[i] > A[pos1] and A[i] < mpos2:
                mpos2 = A[i]
                pos2 = i

        temp = A[pos1]
        A[pos1] = A[pos2]
        A[pos2] = temp

        # X = sorted(A[pos1+1:])
        X = reversed(A[pos1+1:])
        A = A[:pos1+1]
        A.extend(X)

        print("".join(A))


if __name__ == "__main__":
    str = input()
    method1(str)