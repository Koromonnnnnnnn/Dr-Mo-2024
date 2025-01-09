import math

numOne = int(input("Input number 1: "))
numTwo = int(input("Input number 2: "))
numThree = int(input("Input number 3: "))


def average(num1, num2, num3):
    print((num1 + num2 + num3) / 3)

def circleArea(radius):
    A = math.pi * radius**2
    print(A)

def FtoC(temp):
    C = (temp - 32) * 5 / 9
    print(C)

average(numOne, numTwo, numThree)

circleArea(6)

FtoC(53)