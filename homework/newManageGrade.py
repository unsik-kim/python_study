
## 파일관리 클래스
class ManageFile():

    def save(self, data):
        import pickle
        with open('gradeDB.p', 'wb') as file:
            pickle.dump(data,file)

    def load(self):
        import pickle
        import os
        if os.path.isfile('gradeDB.p')==False:   # DB 파일 유무 확인
            with open('gradeDB.p', 'wb') as file:
                data = {}
                pickle.dump(data,file)

        with open('gradeDB.p', 'rb') as file:
            data=pickle.load(file)
            return data



## 학생관리 클래스
class ManageStudent(ManageFile):
    def __init__(self):
        self.data = super().load()
        pass

    def create(self, name, korean, english, math):

        sumScore = korean + math + english
        avgScore = round(sumScore/3,1)
        userData = {name:[korean, math, english, sumScore, avgScore]}
        self.data.setdefault(name, userData[name])

        super().save(self.data)
        print('데이터 추가 완료되었습니다.')


    
    def read(self):
        self.data = super().load()

        pass

    
    def update(self, name, korean, english, math):
        sumScore = korean + math + english
        avgScore = round(sumScore/3,1)
        userData = {name:[korean, math, english, sumScore, avgScore]}
        self.data[name] = userData[name]

        super().save(self.data)
        print('데이터 수정 완료되었습니다.')

    
    def delete(self):

        super().save(self.data)
        pass


## 기능 클래스
class Function():

    @staticmethod
    def inputData(object):
        name = input('이름을 입력하세요 : ')
        if Function.findName(object.data, name)==True:
            print('이미 존재하는 이름입니다.')
        else:
            korean = int(input('국어점수를 입력하세요 : '))
            math = int(input('수학점수를 입력하세요 : '))
            english = int(input('영어점수를 입력하세요 : '))

            object.create(name, korean, math, english)

            Function.printData(Function.searchName(object.data, name))

    @staticmethod
    def findName(dict, name):
        value = dict.get(name)
        if value!=None:
            return True
        else :
            return False

    @staticmethod
    def searchName(dict, name):
        value = dict.get(name)
        if value!=None:
            return {name:[value[0], value[1], value[2], value[3], value[4]]}
        else :
            return None
        

    @staticmethod
    def searchScore(dict):
        score = int(input('검색할 평균점수를 입력하세요 : '))
        resultDict = {}
        for key, value in dict.items():
            if value[4]>=score:
                resultDict.setdefault(key, value)
        pass

        return resultDict

    @staticmethod
    def printData(dict):
        print('No|\t이  름\t\t국어\t영어\t수학\t총점\t평균\t|')
        cnt = 1
        for key, value in dict.items():
            #print(key, value)
            print('{0} |\t{1}\t\t{2}\t{3}\t{4}\t{5}\t{6}\t|'.format(cnt, key, value[0], value[1], value[2], value[3], value[4]))
            cnt += 1
        return True
        


# 스타트 클래스
class start():
    
    @staticmethod
    def selectFunction(object):
        import os
        while True: 
            print('--------------------------------------------------------')
            print('| 1.입력  2.출력  3.검색  4.삭제  5.수정  6.종료 |')
            useFunction = int(input('사용할 기능을 선택하세요. : '))
            os.system('cls')
            if useFunction==1:
                start.createData(object)
            elif useFunction==2:
                start.printAllData(object)
            elif useFunction==3:
                start.searchData(object)
            elif useFunction==4:
                start.deleteData(object)
            elif useFunction==5:
                start.updateData(object)
            elif useFunction==6:
                print('종료합니다.')
                exit()
            else:
                print('잘못된 입력입니다.')

    @staticmethod
    def createData(object):
        Function.inputData(object)
        pass
    
    @staticmethod
    def printAllData(object):
        Function.printData(object.data)
        pass
    
    @staticmethod
    def searchData(object):
        print('| 1.이름검색  2.평균검색 3.뒤로가기|')
        useFunction = int(input('사용할 기능을 선택하세요. : '))
        
        if useFunction==1:
            name = input('검색할 이름을 입력하세요 : ')
            if Function.findName(object.data, name)==True:
                print('| 현재 데이터 |')
                Function.printData(Function.searchName(object.data, name))
            else:
                print('해당 데이터를 찾을 수 없습니다.')
        elif useFunction==2:
            print('| 현재 데이터 |')
            Function.printData(Function.searchScore(object.data))


            

    @staticmethod
    def updateData(object):
        name = input('수정할 이름을 입력하세요 : ')
        if Function.findName(object.data, name)==True:
            print('| 현재 데이터 |')
            Function.printData(Function.searchName(object.data, name))

            value = object.data.get(name)

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

            object.update(name, korean, math, english)

            print('| 현재 데이터 |')
            Function.printData(Function.searchName(object.data, name))
        else:
            print('해당 데이터를 찾을 수 없습니다.')



    @staticmethod
    def deleteData(object):
        pass



def main():
    object = ManageStudent()
    start.selectFunction(object)
    pass

main()