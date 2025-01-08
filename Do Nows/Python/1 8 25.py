file = open('example.txt', 'w')
file.write("Hello, this is a text file.\n")
file.write("This is the second line.\n")
file.close()

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('example.txt', 'a')
file.write("This is an appended line.\n")
file.close()

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()