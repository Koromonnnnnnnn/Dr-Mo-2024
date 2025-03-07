import math

def calculate_circumference(radius):
  circumference = 2 * math.pi * radius
  return circumference

radius = 5
circumference = calculate_circumference(radius)
print(f"The circumference of a circle with radius {radius} is: {circumference}") 


def zigzag_pattern(n):
  for i in range(1, n, 2):
    print(i, end=", ")
  
  for i in range(i - 2, 0, -2): 
    print(i, end=", ")
  print(1) 

zigzag_pattern(10)
zigzag_pattern(15)


def sum_of_3s_and_5s(n):
  total_sum = 0
  for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
      total_sum += i
  return total_sum

print(sum_of_3s_and_5s(10))
print(sum_of_3s_and_5s(20))
print(sum_of_3s_and_5s(100))
