class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')



class D(C, B):
    pass

print(D.mro())

x = D()
x.greeting() 