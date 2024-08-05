
# Design an algorithm to find the median of a stream of integers using two heaps (one max-heap and one min-heap) use the heapq module.

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  
        self.min_heap = []  

    def add_num(self, num):
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]