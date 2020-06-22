a, b = map(int, input().split())
if a<b :
    i = a
    while True :
        if i%5==0 and i%7==0 :
            print('FizzBuzz')
        elif i%7==0 :
            print('Buzz')
        elif i%5==0 :
            print('Fizz')
        else :
            print(i)
        if i == b :
            break
        i += 1

