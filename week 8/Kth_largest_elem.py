# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
def usingHeap(k, nums): #O(n.logk)
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])
        if len(heap) > k:
            print(heap)
            heapq.heappop(heap)
    return heap[0]

# def usingPartition(nums): #O(n)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input()) 

    print(usingHeap(k, arr))