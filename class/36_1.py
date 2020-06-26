class Person:
    def __init__(self):
        print('Person init')      
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def __init__(self):
        super().__init__()
        print('Student init')
    def study(self):
        print('공부하기')
    
    def greeting(self):
        super().greeting()
        print('안녕하세요.2')

james = Student()
james.greeting()
james.study()

print(issubclass(Student, Person))

