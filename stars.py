print('1번')
for i in range(3) :
    for j in range(4) :
        print('*', end=' ')

    print()

print('\n')
#----------------------------------
print('2번')
for i in range(3) :
    for j in range(i+1) :
        print('*', end=' ')
    print()

print('\n')
#-----------------------------------
print('3번')
for i in range(3) :
    for j in range(2-i) :
        print(' ', end=' ')
    for j in range(i+1) :
        print('*', end=' ')
    print()

print('\n')
#-----------------------------------
print('4번')
for i in range(3) :
    for j in range(2-i) :
        print(' ', end=' ')
    for j in range(1+(i*2)) :
        print('*', end=' ')
    for j in range(2-i) :
        print(' ', end=' ')    
    print()

print('\n')
#-----------------------------------
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

print('\n')
#-----------------------------------
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
    m = n+1
    if i<m :
        for j in range((x-n)-i) :
            print('_', end=' ')
        for j in range(1+(i*2)) :
            print('*', end=' ')
        for j in range((x-n)-i) :
            print('_', end=' ')
    else :
        for j in range() :
            print(' ', end=' ')
        for j in range() :
            print('*', end=' ')
        for j in range() :
            print(' ', end=' ')
    print()