enoch = [3, 2, 1, 4, 5]
temp = 0
listSize = len(enoch)

for j in range(listSize - 1):
    for i in range(listSize - 1):
        if enoch[i] > enoch[i + 1]:
            temp = enoch[i]
            enoch[i] = enoch[i + 1]
            enoch[i + 1] = temp

print(enoch)
