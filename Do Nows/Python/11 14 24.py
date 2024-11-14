enoch = [1,2,3,4,5]
temp = 0
listSize = len(enoch)

for i in range(listSize):
    if i > enoch[i+1]:
        temp = enoch[i]
        enoch[i] = enoch[i + 1]
        enoch[i + 1] = temp

print(enoch)
