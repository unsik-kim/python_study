inputValue = int(input())

for i in range(inputValue) :
    n = 1+(2*(inputValue-1))

    for j in range(int((n-1)/2)-(i)) :
        print(' ', end='')
    for j in range(1+(2*(i))) :
        print('*', end='')
    for j in range(int((n-1)/2)-(i)) :
        print(' ', end='')
    
    print()