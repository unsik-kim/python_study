class Person:
    def __init__(self):
        print('1')
        self.__hello = '안녕하세요.'
        self.hello = "안뇽"

    def greeting(self):
        print('2')
        print(self.__hello)
        self.__greeting()

    def __greeting(self):
        print('20')
        print(self.hello)

print('3')
james = Person()
print('4')
james.greeting()
print('5')
print(james.hello)
print('6')
james.__greeting()

