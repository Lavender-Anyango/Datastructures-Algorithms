# Heap Interview Questions: Detailed Explanations

## 1. [Min-heap Implementation](./min_heap.py)

This class implements a binary min-heap using a list. Key methods include:

- `insert`: Adds a new element to the end of the list and then "sifts up" to maintain the heap property.
- `extract_min`: Removes and returns the minimum element (root), replaces it with the last element, and then "sifts down" to maintain the heap property.
- `heapify`: Converts an arbitrary list into a valid heap by sifting down from the last non-leaf node to the root.

The `_sift_up` and `_sift_down` methods are crucial for maintaining the heap property after insertions and deletions.

## 2. [Kth Largest Element](./kth_largest.py)


This approach uses a min-heap of size k for efficiency:

1. Create an empty min-heap.
2. Iterate through the array:
   - If heap size < k: add number to heap.
   - If heap size = k and number > heap minimum: replace heap minimum with number.
3. The heap minimum is the kth largest number.


### Complexity:
- Time: O(n * log(k)), where n is array length.


## 3. [Priority Queue](./priority_queue.py)

This implementation is similar to the min-heap but stores tuples of (priority, item) instead of just values. The priority is used for ordering, allowing items with lower priority values to be dequeued first.

## 4. [Merging k Sorted Arrays](./merge_k_sorted.py)

This solution uses a min-heap to efficiently merge multiple sorted arrays. It works by:

1. Initially inserting the first element from each array into the heap.
2. Repeatedly extracting the minimum element, adding it to the result, and inserting the next element from the same array (if any).

This approach ensures we always have the current minimum among all arrays in O(log k) time, where k is the number of arrays.

## 5. [Converting a Binary Tree to a Min-heap](./tree_to_heap.py)

This solution works in three steps:

1. Convert the binary tree to an array using level-order traversal.
2. Heapify the array to create a min-heap.
3. Convert the heapified array back into a binary tree.

This approach preserves the structure of the original tree while ensuring the heap property.

## 6. [Median of a Stream](./median.py)

## MedianFinder Class

The `MedianFinder` class uses two heaps to maintain the median of a stream of numbers:

- `max_heap` stores the smaller half of the numbers.
- `min_heap` stores the larger half of the numbers.

## Implementation

We use the `heapq` module to implement the heaps. In this case, we use a min-heap for both `max_heap` and `min_heap`.

To store the larger numbers in `max_heap`, we negate the numbers before pushing them into the heap. This effectively makes `max_heap` a max-heap.

## Method: add_num

In the `add_num` method:

1. If the number is smaller than the top element of `max_heap`, we push it into `max_heap` using `heapq.heappush`. Otherwise, we push it into `min_heap.
2. We use `heapq.heappushpop` to push the number into one heap and pop the top element from the other heap in a single operation.
3. We balance the heaps by ensuring that the size difference between `max_heap` and `min_heap` is at most 1.

## Method: find_median

In the `find_median` method:

- If the sizes of `max_heap` and `min_heap` are equal, we calculate the median by taking the average of the top elements of both heaps.
- If the sizes are not equal, the median is the top element of `max_heap`, which is the largest number in the smaller half.