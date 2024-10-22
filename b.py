file = open('Codingal (1).txt', 'r')
print("Reading first line")
print(file.readline())
file.close()

file = open('Codingal (1).txt', 'r')
print("Reading multiple lines")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal (1).txt', 'r')
print("Looping through lines")
for line in file:
    print(line)
file.close()

file = open('Codingal (1).txt', 'r')
print("Reading the whole document")
print(file.readlines())
file.close()