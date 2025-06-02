def heapify(arr,n,i):
    largest = i  # Assume current node is largest
    left = 2*i + 1  # left child index
    right = 2*i + 2  # right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap with the largest and heapify again
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n//2-1, -1, -1):
        heapify(arr,n,i)

    # Step 2: Extract elements from heap one by one
    for i in range(n-1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore the max heap property
        heapify(arr, i, 0)

    return arr


arr = [23,35,452,234,235,12,2352,23,5,32,2]
print(heapSort(arr))