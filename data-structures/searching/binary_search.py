# ITERATIVE approach
def binary_search_iterative(arr,target):
    """To implement binary search array must be sorted"""
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid # return the index if target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # return -1 if target not found

# print(binary_search_iterative.__doc__)

# arr = [1,2,23,34,45,65,74,86,90,99,108]
# print(binary_search_iterative(arr,45))


# RECURSIVE approach
def binary_search_recursive(arr,target,low,high):
    """To implement binary search array must be sorted"""
    
    if low > high:
        return -1 # return -1 if target not found
    
    mid = (low+high)//2
    if arr[mid] == target:
        return mid # return the index if target is found
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid+1,high)
    else:
        return binary_search_recursive(arr,target,low,mid-1)

# print(binary_search_recursive.__doc__)

# arr = [1,2,23,34,45,65,74,86,90,99,108]
# print(binary_search_recursive(arr,45,0,len(arr)-1))