class Person:
    def __init__(self):
        print('Person init')
        pass

    def greeting(self):
        print('6')
        print('안녕하세요.')

class University:
    def __init__(self):
        print('University init')
        pass
    def manage_credit(self):
        print('7')
        print('학점 관리.')

class Undergraduate(University, Person):
    def __init__(self):
        super().__init__()
        print('Undergraduate init')
        pass
    def study(self):
        print('8')
        print('공부하기')

print('1')
james = Undergraduate()
print('2')
james.greeting()
print('3')
james.manage_credit()
print('4')
james.study()
print('5')