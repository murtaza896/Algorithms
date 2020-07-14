# A: integer (no. of beggars)
# B: list of list of integers

# A = int(input())
# B = list(map(int, input().strip().split()))

B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
A = 5

# T: O(N^2), S: O(1) solution
# pots = [0 for i in range(A)]
# for elem in B:
#     i, j = elem[0], elem[1]
#     donation = elem[2]
#
#     for x in range(i-1, j):
#         pots[x] += donation
#
# print(pots)

# T: O(N), S: O(1) solution
# concept of prefix sum is used
# Assign index i with +donation, and index j with -donation
# Return prefix sum of the array.

pots = [0 for i in range(A+1)]

for elem in B:
    i, j, donation = elem[0] - 1 , elem[1] - 1, elem[2]
    pots[i] += donation
    pots[j] -= donation

for i in range(1, len(pots)):
    pots[i] += pots[i-1]

print(pots[:-1])