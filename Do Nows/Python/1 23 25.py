

arr =  [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")