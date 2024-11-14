enoch = [1, 2, 3, 4, 5]
temp = 0
listSize = len(enoch)

# Bubble Sort
for i in range(listSize - 1):      # Outer loop for each pass
    for j in range(listSize - 1):  # Inner loop to compare adjacent elements
        if enoch[j] > enoch[j + 1]:
            # Swap using temp variable
            temp = enoch[j]
            enoch[j] = enoch[j + 1]
            enoch[j + 1] = temp

print("Sorted list:", enoch)
