# Calculate the maximum length of consecutive 1s, after atmost 1 swap operations in the given Binary string

def method1(arr):
    tot_1 = 0
    maxL = [0 for i in range(len(arr))]
    maxR = [0 for i in range(len(arr))]

    maxL[0] = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == 0:
            maxL[i] = 0
        else:
            maxL[i] = maxL[i-1] + 1

    maxR[-1] = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] == 0:
            maxR[i] = 0
        else:
            maxR[i] = maxR[i+1] + 1

    

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    method1(arr)