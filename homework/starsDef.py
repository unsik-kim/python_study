

def star1():
    print('1번')
    for i in range(3) :
        for j in range(4) :
            print('*', end=' ')

        print()

def star2():
    print('2번')
    for i in range(3) :
        for j in range(i+1) :
            print('*', end=' ')
        print()

def star3():
    print('3번')
    for i in range(3) :
        for j in range(2-i) :
            print(' ', end=' ')
        for j in range(i+1) :
            print('*', end=' ')
        print()

def star4():
    print('4번')
    for i in range(3) :
        for j in range(2-i) :
            print(' ', end=' ')
        for j in range(1+(i*2)) :
            print('*', end=' ')
        for j in range(2-i) :
            print(' ', end=' ')    
        print()

def star5():
    print('5번')
    for i in range(5) :
        if i<3 :
            for j in range(2-i) :
                print(' ', end=' ')
            for j in range(1+(i*2)) :
                print('*', end=' ')
            for j in range(2-i) :
                print(' ', end=' ')
        else :
            for j in range(i-2) :
                print(' ', end=' ')
            for j in range(((5-i)*2)-1) :
                print('*', end=' ')
            for j in range(i-2) :
                print(' ', end=' ')
        print()

def star6():
    print('6번')
    x = 0

    while(1) :
        x = int(input('홀수 값 입력 : '))

        if x%2 != 0 :
            break
        else :
            print('짝수 값 입니다.')

    for i in range(x) :
        n = int((x+1)/2)

        if i<n :
            for j in range((x-n)-i) :
                print(' ', end=' ')
            for j in range(1+(i*2)) :
                print('*', end=' ')
            for j in range((x-n)-i) :
                print(' ', end=' ')
        else :
            for j in range(i-n+1) :
                print(' ', end=' ')
            for j in range(x-(2*(i-n+1))) :
                print('*', end=' ')
            for j in range(i-n+1) :
                print(' ', end=' ')
        print()

def drawStar(inputData):
    if inputData==1:
        star1()
    elif inputData==2:
        star2()
    elif inputData==3:
        star3()
    elif inputData==4:
        star4()
    elif inputData==5:
        star5()
    elif inputData==6:
        star6()
    else:
        return False
    
    return True
    
def inputDataFunction():
        inputData = int(input('실행시킬 번호를 입력하세요.(범위 1~6, 범위를 벗어나면 종료됩니다.)  : '))
        if inputData>0 and inputData<7:
            return inputData
        else:
            print('범위를 벗어남, 종료됩니다.')
            return inputData

while True:
    if drawStar(inputDataFunction())==False:
        break


