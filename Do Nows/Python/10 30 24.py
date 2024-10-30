import numpy as np
import matplot.pyplot as plt

matrix = np.random.randint(1, 101, size=(4, 4))
print("Generated Matric:\n", matrix)

max_value = np.max(matrix)
print("Maximum Value:", max_value)

min_value = np.min(matrix)
print("Minimum Value:", min_value)
