def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    len1 = mid - left + 1
    len2 = right - mid
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)
    RUN = 32  # A small fixed size; CPython dynamically adjusts this

    # Step 1: Sort individual runs using Insertion Sort
    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge runs
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

# Example usage
arr = [5, 21, 7, 23, 19]
tim_sort(arr)
print("Sorted array:", arr)
