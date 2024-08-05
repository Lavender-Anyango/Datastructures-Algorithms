# Given an array of integers, write a function to find the kth largest element.

from heapq import heappush, heappushpop

def find_kth_largest(arr, k):
    heap = []
    for num in arr:
        if len(heap) < k:
            heappush(heap, num)
        elif num > heap[0]:
            heappushpop(heap, num)
    
    return heap[0]