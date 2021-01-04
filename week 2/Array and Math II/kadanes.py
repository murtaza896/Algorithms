import sys 
def solve(arr):
    sm = -sys.maxsize - 1
    mx = sm

    for x in arr:
        sm = max(sm + x, x)
        mx = max(mx, sm)

    return mx 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = solve(arr)
    print(res)