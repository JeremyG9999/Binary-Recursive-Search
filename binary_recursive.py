def binary_search_recursive(arr, target):
    if not arr or target not in arr:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr[:mid], target)
    else:
        return mid + binary_search_recursive(arr[mid+1:], target)
arr = [1, 3, 4, 5, 7, 9, 11]
target = 5
index = binary_search_recursive(arr, target)
print(index) 