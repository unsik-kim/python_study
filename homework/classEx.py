class Student():
    def __init__(self, name=None, kor=None, eng=None, mat=None):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        if (kor!=None) and (eng!=None) and (mat!=None):
            self.__total = kor+eng+mat
            self.__avg = self.__total/3
        else:
            self.__total = None
            self.__avg = None
    
    def __init__(self ):
        self.__name = 0
        self.__kor = 0
        self.__eng = 0
        self.__mat = 0



    def getName(self):
        return self.__name

    def getKor(self):
        return self.__kor

    def getEng(self):
        return self.__eng

    def getMat(self):
        return self.__mat

    def getTotal(self):
        if self.__total == None:
            self.__total = self.__kor+self.__eng+self.__mat
        return self.__total

    def getAvg(self):
        if self.__avg== None:
            self.__avg = self.__total/3
        return self.__avg

    def setName(self, name):
        self.__name = name
    def setKor(self, kor):
        self.__kor = kor
    def setEng(self, eng):
        self.__eng = eng
    def setMat(self, mat):
        self.__mat = mat


#james = Student('Superman', 10, 20, 30)
james = Student()

james.setName('superman')
james.setKor(10)
james.setEng(20)
james.setMat(30)

print(james.getName(), end=' ')
print(james.getKor(), end=' ')
print(james.getEng(), end=' ')
print(james.getMat(), end=' ')
print(james.getTotal(), end=' ')
print(james.getAvg(), end=' ')
