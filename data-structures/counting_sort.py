def countingSort(arr):
    if not arr:
        return

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

    return arr

# not good for these type of examples where the numbers in the array are really big
# print(countingSort([23,35,452,234,235,12,2352,23,5,32,2]))

# good for these type of examples
# print(countingSort([4, 2, 2, 8, 3, 3, 1]))