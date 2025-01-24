#Python Quiz 1/24/2025

def sumDigits(x):
    if x == 0: #Because zero is zero
        return 0

    n = x - (x // 10) * 10 #Get last digit of the number
    return n + sumDigits(x // 10)


num = 345
printer = sumDigits(num)
print(printer)
