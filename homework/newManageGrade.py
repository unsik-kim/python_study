
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

        pass

    
    def read(self):
        self.data = super().load()

        pass

    
    def update(self):

        super().save(self.data)
        pass

    
    def delete(self):

        super().save(self.data)
        pass


## 기능 클래스
class Function():

    @staticmethod
    def inputData(object):
        name = input('이름을 입력하세요 : ')
        if Function.searchName(object.data, name)!=None:
            print('이미 존재하는 이름입니다.')
        else:
            korean = int(input('국어점수를 입력하세요 : '))
            math = int(input('수학점수를 입력하세요 : '))
            english = int(input('영어점수를 입력하세요 : '))

            object.create(name, korean, math, english)

            Function.printData(Function.searchName(object.data, name))

    @staticmethod
    def searchName(dict, name):
        value = dict.get(name)
        if value!=None:
            return {name:[value[0], value[1], value[2], value[3], value[4]]}
        else :
            return None
        pass

    @staticmethod
    def searchScore(data):
        pass

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
        
        pass
    
    @staticmethod
    def searchData(object):
        pass

    @staticmethod
    def updateData(object):
        pass

    @staticmethod
    def deleteData(object):
        pass



def main():
    object = ManageStudent()
    start.selectFunction(object)
    pass

main()