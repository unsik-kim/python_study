import random

x = int(input('개수입력 : '))

for i in range(x) :  # x만큼 반복하여 로또번호 추첨
    result = []     # 6개의 번호를 넣을 빈 리스트 생성

    while(len(result)!=6) :     # result 리스트의 길이가 6이 아니면 반복, 숫자가 6개 채워질 때 까지 반복
        resultLength = len(result)      # 현재 reslut 리스트의 길이를 변수에 저장
        duplicationCheck = False        # 랜덤으로 생성된 번호가 result 리스트 내 번호들과 중복되는지 체크할 변수 생성
        randomNumber = random.randint(1,45)     # 1부터 45 범위의 랜덤번호 생성
        
        for j in result :       # result 리스트의 개수만큼 반복하여 리스트 내 중복번호 확인
            if j == randomNumber :      # result 리스트에서 가져온 값 j와 랜덤으로 추출한 번호가 같은지 확인
                duplicationCheck = True     # 같다면 duplicationCheck를 True로 변경
                print('find a duplicate number : ', j, '\trow : ', resultLength)      # resultLength번째의 번호를 생성할 때 중복되는 번호 j가 있다고 알림
        
        if duplicationCheck == False :      # 중복되는 번호가 없다면 False
            result.append(randomNumber)     # append 함수로 result 리스트 뒷단에 randomNumber의 값 추가
    # result 리스트의 길이가 6개가 되면 while문에서 빠져나옴

    print(i,'번 : ', result)    # i번째 추첨번호 출력
    
    print('\n')

        
    