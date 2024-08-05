# Implement a function to convert a binary tree into a min-heap

from min_heap import MinHeap

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_array(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def array_to_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr):
            node.left = TreeNode(arr[i])
            queue.append(node.left)
            i += 1
        if i < len(arr):
            node.right = TreeNode(arr[i])
            queue.append(node.right)
            i += 1
    return root

def convert_to_min_heap(root):
    arr = tree_to_array(root)
    heap = MinHeap()
    heap.heapify(arr)
    return array_to_tree(heap.heap)