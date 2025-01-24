#Python Quiz 1/24/2025

def sumDigits(x):
    if x == 0:
        return 0

    n = x - (x // 10) * 10
    return n + sumDigits(x // 10)


num = 345
printer = sumDigits(num)
print(printer)
