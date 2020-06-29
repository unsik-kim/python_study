
## 파일관리 클래스
class ManageFile():

    def save(self, data):
        import pickle
        with open('gradeDB.p', 'wb') as file:
            pickle.dump(data,file)

    def load(self, data):
        import pickle
        import os
        if os.path.isfile('gradeDB.p')==False:   # DB 파일 유무 확인
            with open('gradeDB.p', 'wb') as file:
                data = {}
                pickle.dump(data,file)
                pass

        with open('gradeDB.p', 'rb') as file:
            data=pickle.load(file)
            # print(type(data), data



## 학생관리 클래스
class ManageStudent(ManageFile):
    def __init__(self):
        self.data = super.load()
        pass

    def create(self):
        
        super.save(self.data)
        pass

    
    def read(self):
        self.data = super.load()

        pass

    
    def update(self):

        super.save(self.data)
        pass

    
    def delete(self):

        super.save(self.data)
        pass


## 기능 클래스
class Function():
    @staticmethod
    def inputData(data):
        pass

    @staticmethod
    def searchName(data):
        pass

    @staticmethod
    def searchScore(data):
        pass

    @staticmethod
    def printData(data):
        pass


# 스타트 클래스
class start():

    @staticmethod
    def selectFunction(data):
        pass

    @staticmethod
    def createData(data):
        pass
    
    @staticmethod
    def printAllData(data):
        pass
    
    @staticmethod
    def searchData(data):
        pass

    @staticmethod
    def updateData(data):
        pass

    @staticmethod
    def deleteData(data):
        pass



def main():
    data = ManageStudent()
    start.selectFunction(data)
    pass