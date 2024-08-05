
# Q4: Write a function to merge k sorted arrays using a min-heap.

from min_heap import MinHeap

def merge_k_sorted_arrays(arrays):
    result = []
    heap = MinHeap()
    
    for i, arr in enumerate(arrays):
        if arr:
            heap.insert((arr[0], i, 0))
    
    while heap.heap:
        val, arr_index, elem_index = heap.extract_min()
        result.append(val)
        
        if elem_index + 1 < len(arrays[arr_index]):
            next_elem = arrays[arr_index][elem_index + 1]
            heap.insert((next_elem, arr_index, elem_index + 1))
    
    return result