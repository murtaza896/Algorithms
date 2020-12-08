# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/0/?track=md-arrays&batchId=144#

def sort012(arr):
    def swap(x, y):
        arr[x], arr[y] = arr[y], arr[x] 
        
    p1, p2 = 0, len(arr) - 1
    i = 0 
    
    while i<=p2:
        # print(arr)
        if arr[i] == 0:
            swap(p1, i)
            p1 += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            swap(p2, i)
            p2 -= 1

if __name__ == "__main__":
    arr = list(map(input().split())) #Enter an array of 0, 1, 2 only
    sort012(arr)
    print(arr)