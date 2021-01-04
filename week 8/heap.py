def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i] 

def maxHeapify(arr, i, n):
    # print(arr)
    if i > n//2:
        return
    
    mx = i 

    if arr[2*i] > arr[mx]: 
        mx = 2*i 
    if (2*i + 1) < n and arr[2*i + 1] > arr[mx]:
        mx = 2*i + 1 
    
    if mx != i:
        swap(arr, i, mx)
        maxHeapify(arr, mx, n)

def buildMaxHeap(arr):
    n = len(arr) - 1
    for i in range(n//2, 0, -1):
        maxHeapify(arr, i, n)

def heapSort(arr):
    i =  0
    n = len(arr) - 1
    buildMaxHeap(arr)

    while i < n:
        swap(arr, 1, n - i)
        i += 1 
        maxHeapify(arr, 1, n - i)
        
        
if __name__ == "__main__":
    arr = list(map(int, input().split())) #1 based indexing
    # heapSort(arr)
    maxHeapify(arr, 1, len(arr)-1)
    print(arr)