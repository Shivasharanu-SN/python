def quickSort(arr, low, high):

    if low < high:

        pi = partition(arr,low,high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

    return arr


def partition(arr,low,high):
    pivot = arr[high]
    i = low-1

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# arr = [23,35,452,234,235,12,2352,23,5,32,2]
# print(quickSort(arr, 0, len(arr)-1))