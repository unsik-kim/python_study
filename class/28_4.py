with open('words.txt', 'w') as file:
    file.write('apache\ndecal\ndid\nneep\nnoon\nrefer\nriver')

with open('words.txt', 'r') as file:
    data = file.read()

dataList = data.split('\n')

resultList = list()

for i in range(len(dataList)):
    word = dataList[i]
    is_palindrome = True
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            is_palindrome = False
            break
    if is_palindrome==True:
        resultList.append(word)

print(resultList)