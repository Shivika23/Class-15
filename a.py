file = open('Codingal (1).txt', 'r')
print(file.read())
file.close()

file = open('Codingal (1).txt', 'r')
print(file.read(15))
file.close()

file = open('Codingal (1).txt', 'a')
file.write("Hi am a penguin and i'm 1 year old")
file.close()