import matplotlib.pyplot as plt
import numpy as np

# caculate and regline functions not made by me !
def calculateB(x, y, n):
    sx = sum(x)
    sy = sum(y)
    sxsy = 0
    sx2 = 0
    for i in range(n):
        sxsy += x[i] * y[i]
        sx2 += x[i] * x[i]
    b = (n * sxsy - sx * sy) / (n * sx2 - sx * sx)
    return b

def leastRegLine(X, Y, n):
    b = calculateB(X, Y, n)
    meanX = sum(X) / n
    meanY = sum(Y) / n
    a = meanY - b * meanX
    print("Regression line:")
    print("Y = ", '%.3f' % a, " + ", '%.3f' % b, "*X", sep="")
    return a, b

# Scatter plot data
X = [95, 85, 80, 70, 60]
Y = [90, 80, 70, 65, 60]
n = len(X)

# caculate and regline functions not made by me !

plt.scatter(X, Y, color='red', label='point')
plt.plot([60, 95], [60, 90], color='purple', label='line') # min max

plt.xlabel('x')
plt.ylabel('y')
plt.title('line')
plt.legend()

plt.show()
