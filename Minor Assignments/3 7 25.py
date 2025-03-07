def calculate_circumference(r):
    C = 2.0 * (3.14 * r)
    return C

print(calculate_circumference(5))

def zigzag_pattern(n):
  for i in range(1, n, 2):
    print(i, end=" ")
  
  for i in range(i - 2, 0, -2): 
    print(i, end=" ")

zigzag_pattern(10)

def sumtreefive(n):
  sum = 0
  for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
      print(i)
  return sum
  
print(sumtreefive(10))
print(sumtreefive(20))
print(sumtreefive(100))