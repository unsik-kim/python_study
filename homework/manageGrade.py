import os
import pickle

def printDic(data, name=""):

    if name!="":
        value = data.get(name)
        if value!=None:
            print('|\t이름\t국어\t영어\t수학\t총점\t평균\t|')
            print('|\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t|'.format(name, value[0], value[1], value[2], value[3], value[4]))
            return True
        else :
            return False

    else :
        print('No|\t이  름\t\t국어\t영어\t수학\t총점\t평균\t|')
        cnt = 1
        for key, value in data.items():
            #print(key, value)
            print('{0} |\t{1}\t\t{2}\t{3}\t{4}\t{5}\t{6}\t|'.format(cnt, key, value[0], value[1], value[2], value[3], value[4]))
            cnt += 1
        return True


def insertData(data, option=0):
    name = input('이름을 입력하세요 : ')
    if printDic(data, name)==True:
        print('이미 존재하는 이름입니다.')
    else:
        korean = int(input('국어점수를 입력하세요 : '))
        math = int(input('수학점수를 입력하세요 : '))
        english = int(input('영어점수를 입력하세요 : '))

        sumScore = korean + math + english
        averScore = round(sumScore/3,1)
        userData = {name:[korean, math, english, sumScore, averScore]}
        data.setdefault(name, userData[name])
        fileSave(data)
        print('입력이 완료되었습니다.')
        printDic(data, name)

def printData(data):
    printDic(data)
    

def searchData(data):
    print('| 1.이름검색  2.평균검색 3.뒤로가기|')
    useFunction = int(input('사용할 기능을 선택하세요. : '))
    if useFunction==1:
        searchName(data)
    elif useFunction==2:
        searchAvg(data)

    return 0
    

def deleteData(data):
    while True:
        name = input('삭제할 이름을 입력하세요 :')
        if printDic(data, name)==True:
            data.pop(name)
            print('위 데이터가 정상적으로 삭제 되었습니다.')
            fileSave(data)
            break
        else:
            print('해당 데이터를 찾을 수 없습니다.')
            break

def updateData(data):
    while True:
        name = input('수정할 이름을 입력하세요 : ')
        print('| 현재 데이터 |')
        if printDic(data, name)==True:
            value = data.get(name)

            print('| 1.국어  2.영어  3.수학  0.모두 |')

            option = int(input('수정할 과목을 선택하세요 : '))

            korean = value[0]
            math = value[1]
            english = value[2]

            if option==1 or option==0:
                korean = int(input('국어점수를 입력하세요 : '))
            if option==2 or option==0:
                math = int(input('영어점수를 입력하세요 : '))
            if option==3 or option==0:
                english = int(input('수학점수를 입력하세요 : '))

            sumScore = korean + math + english
            averScore = round(sumScore/3,1)
            userData = {name:[korean, math, english, sumScore, averScore]}
            data[name]=userData[name]
            fileSave(data)

            print('| 현재 데이터 |')
            printDic(data, name)
            print('수정이 완료되었습니다.')
            break
        else:
            print('해당 데이터를 찾을 수 없습니다.')
            break

def searchName(data):
    name = input('검색할 이름을 입력하세요 : ')
    if printDic(data, name)==True:
        break
    else:
        print('해당 데이터를 찾을 수 없습니다.')
        break

def searchAvg(data):
    score = int(input('검색할 평균점수를 입력하세요 : '))
    resultDict = {}
    for key, value in data.items():
        if value[4]>=score:
            resultDict.setdefault(key, value)

    

    '''
    max = 0.0
    copyDict = resultDict
    for key, value in copyDict.items():
        if value[4] > max:
            resultDict.pop(key)
            resultDict.setdefault(key, value)
    '''
    printDic(resultDict)

def fileLoad():
    if os.path.isfile('gradeDB.p')==False:   # DB 파일 유무 확인
        with open('gradeDB.p', 'wb') as file:
            pass

    with open('gradeDB.p', 'rb') as file:
        data=pickle.load(file)
        # print(type(data), data)

    return data

def fileSave(data):
    with open('gradeDB.p', 'wb') as file:
        pickle.dump(data,file)
    

def main():
    mainDict = fileLoad()
    while True: 
        print('--------------------------------------------------------')
        print('| 1.입력  2.출력  3.검색  4.삭제  5.수정  6.종료 |')
        useFunction = int(input('사용할 기능을 선택하세요. : '))
        os.system('cls---')
        if useFunction==1:
            insertData(mainDict)
        elif useFunction==2:
            printData(mainDict)
        elif useFunction==3:
            searchData(mainDict)
        elif useFunction==4:
            deleteData(mainDict)
        elif useFunction==5:
            updateData(mainDict)
        elif useFunction==6:
            print('종료합니다.')
            exit()
        else:
            print('잘못된 입력입니다.')
        
        
main()

