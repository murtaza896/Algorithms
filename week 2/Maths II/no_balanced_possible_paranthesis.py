# Recursive Method, Cn = Summation of Ci * Cn-i-1 , i: [0 - n-1]
# Time = O(N^2)

def Catalan_1(x):
    if x<=1:
        return 1
    res = 0
    for i in range(x):
        res += Catalan_1(i) * Catalan_1(x - i - 1)

    return res

# Binomial Co-efficient Method, Cn = 1/(n+1) * 2nCn
# Time = O(N)
def Catalan_2(x):
    n = 2*x
    k = x

    if k > n-k:
        k = n - k

    res = 1
    # Calculate the val of n * n-1 * n-2 * n-3 .... n-k
    for i in range(k):
        res = res * (n-i)

    # Calculating the val of i * i+1 * i+2 * i+3 * i+4 .... k
    for i in range(k):
        res = res // (i+1)

    c = res // (x+1)

    return c

def no_of_balanced_parenthesis(n):
    return Catalan_1(n)

if __name__ == "__main__":
    n = int(input())
    print(no_of_balanced_parenthesis(n))

