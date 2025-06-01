def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Because digits are 0 to 9

    # Count digit occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count to positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]

    return arr

def radixSort(arr):
    if not arr:
        return

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

# Example
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radixSort(arr))
