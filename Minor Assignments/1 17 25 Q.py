def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    Gus = fibonacci(num - 1)
    Gus.append(Gus[-1] + Gus[-2]) 
    return Gus

num = int(input("Enter the number"))

if num > 0:
    result = fibonacci(num)
    print(result)
else:
    print("gus does not approve!")
