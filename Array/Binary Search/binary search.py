def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found target at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Not found
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

# Iterative
index = binary_search_iterative(arr, target)
print("Found at index (iterative):", index)


