with open('words.txt', 'w') as file:
    file.write('''Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.''')

with open('words.txt', 'r') as file:
    data = file.read()

dataList = data.split(' ')

resultList = list()

for i in range(len(dataList)):
    a = dataList[i].strip(',.')
    if a.find('c')!=-1:
        resultList.append(a)

print(resultList)

