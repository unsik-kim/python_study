inputData = "51900;83000;158000;367500;250000;59200;128500;1304000"

dataList = inputData.split(';')
#print(stringDataList)

dataList = [int(i) for i in dataList]
#print(resultData)

dataList.sort(reverse=True)

for i in range(len(dataList)) :
    print(dataList[i])