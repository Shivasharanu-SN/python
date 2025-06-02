def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # return the index if target is found
    return -1 # return -1 if target not found


# arr = [23,234,5,4,56,67,234,21,214,25,4,65,77,7]
# print(linear_search(arr,65))