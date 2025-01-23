def binarySearch(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binarySearch2(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch2(arr, low, mid - 1, x)
        else:
            return binarySearch2(arr, mid + 1, high, x)
    return -1


arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

result2 = binarySearch2(arr, 0, len(arr) - 1, 3)

if result2 != -1:
    print("Element is present at index", result2)
else:
    print("Element is not present in array")
