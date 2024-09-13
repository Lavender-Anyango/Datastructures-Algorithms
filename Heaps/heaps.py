import heapq

def create_and_access_heap(values):
    # Convert the list into a heap
    heapq.heapify(values)
    
    # Print the heap
    print("Heap:", values)
    
    # Add a new value to the heap
    new_value = 15
    heapq.heappush(values, new_value)
    
    # Print the updated heap
    print("Heap after push:", values)
    
    # Access the smallest element
    smallest = values[0]
    print("Smallest element:", smallest)

    # Remove the smallest element
    print("Heap before pop:", values)
    delete_smallest = heapq.heappop(values)
    print("Heap after pop:", values)

    #Access the largest element
    largest = heapq.nlargest(1, values)[0]
    print("Largest element:", largest)


    # Replace the smallest element
    prev_smallest = heapq.heapreplace(values, 0)
    print("Previous smallest element:", prev_smallest)
    print("Heap after replace:", values)
    

    
    return values

# Example
values = [9, 1, 6, 7, 12, 20]
new_heap = create_and_access_heap(values)