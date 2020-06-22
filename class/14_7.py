a, b, c, d = map(int, input().split())

if a<0 or a>100 :
    print('잘못된 점수')
elif b<0 or b>100 :
    print('잘못된 점수')
elif c<0 or c>100 :
    print('잘못된 점수')
elif d<0 or d>100 :
    print('잘못된 점수')
else :
    result = (a+b+c+d)/4

    if result>=80 :
        print('합격')
    else :
        print('불합격')