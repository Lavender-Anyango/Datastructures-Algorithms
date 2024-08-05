# Implement a min-heap class from scratch with the following methods:

# insert(value)
# extract_min()
# peek()
# heapify(list)



class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def heapify(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)

    def _sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)