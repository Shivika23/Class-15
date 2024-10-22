f1 = open("Codingal (1).txt", 'r')
f2 = open("CodingalUpdated.txt", 'w')

for line in f1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        f2.write(line)

f1.close()
f2.close()
