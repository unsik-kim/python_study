import os


## 파일관리 클래스
class ManageFile():

    def save(self, data):
        import pickle
        with open('gradeDB.p', 'wb') as file:
            pickle.dump(data,file)

    def load(self, data):
        import pickle
        if os.path.isfile('gradeDB.p')==False:   # DB 파일 유무 확인
            with open('gradeDB.p', 'wb') as file:
                pass

            with open('gradeDB.p', 'rb') as file:
                data=pickle.load(file)
                # print(type(data), data



## 학생관리 클래스
class ManageStudent(ManageFile):
    def __init__(self):

        data = {}
        pass

    def create(self):
        
        pass

    
    def read(self):
        pass

    
    def update(self):
        pass

    
    def delete(self):
        pass


## 기능 클래스
class Function():
    @staticmethod
    def inputData():
        pass

    @staticmethod
    def searchName():
        pass

    @staticmethod
    def searchScore():
        pass

    @staticmethod
    def printData(data):
        pass


# 스타트 클래스
class start():

    @staticmethod
    def selectFunction(people):
        pass

    @staticmethod
    def createData():
        pass
    
    @staticmethod
    def printAllData():
        pass
    
    @staticmethod
    def searchData():
        pass

    @staticmethod
    def updateData():
        pass

    @staticmethod
    def deleteData():
        pass



def main():
    people = ManageStudent()
    start.selectFunction(people)
    pass