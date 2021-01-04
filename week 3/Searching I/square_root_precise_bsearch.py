# Given a number N and a precision p, calculate the square root of the number upto p precision
# Time Complexity: O(log(number) + precision) = O(log(number))
# https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/

def method1(n, precision):
    start = 0
    end = n
    ans = 0

    while start <= end:

        mid = start + (end-start)//2

        if mid * mid == n:
            ans = mid
            break

        elif mid * mid > n:
            end = mid - 1

        elif mid * mid < n:
            start = mid + 1
            ans = mid

    increment = 0.1
    for i in range(0, precision):
        while (ans*ans <= n):
            ans += increment

        ans = ans - increment
        increment = increment / 10

    return ans

if __name__ == "__main__":
    n = int(input())
    precision = int(input())

    print(round(method1(n, precision), 4))