def fileLoad():
    pass

def fileSave():
    pass

def printDic(**data):
    for i in range(len(data)):
        pass
        #print('|\t{0}\t{1}\t{2}\t{3}\t{04\t|'.format(data[0]))


def insertData():
    name = input('이름을 입력하세요 : ')
    korean = int(input('국어점수를 입력하세요 : '))
    math = int(input('수학점수를 입력하세요 : '))
    english = int(input('영어점수를 입력하세요 : '))
    sumScore = korean + math + english
    averScore = sumScore/3
    data = {name:[korean, math, english, sumScore, averScore]}
    str(key), list(score) = data.items()
    print('|\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t|'.format(name, score[0], score[1], score[2], score[3], score[4]))
    print('입력이 완료되었습니다.')

def printData():
    pass

def searchData():
    pass

def deleteData():
    pass

def updateData():
    pass


def main():
    #fileload()
    while True:
        print('\n')
        print('| 1.입력  2.출력  3.검색  4.삭제  5.수정  6.종료 |')
        useFunction = int(input('사용할 기능을 선택하세요. : '))
        if useFunction==1:
            insertData()
        elif useFunction==2:
            pass
        elif useFunction==3:
            pass
        elif useFunction==4:
            pass
        elif useFunction==5:
            pass
        elif useFunction==6:
            print('종료합니다.')
            exit()
        else:
            print('잘못된 입력입니다.')
        
main()