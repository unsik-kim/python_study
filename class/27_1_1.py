file = open('hello.txt', 'w')
file.write('Hello, world!')
file.close()

file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

with open('hello.txt', 'w') as file:
    file.write('Hello')