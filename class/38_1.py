y = [10, 20, 30]

def test():
    try:
        index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
        print(y[index] / x)


    except ZeroDivisionError as e:
        print('0으로 나눌 수 없습니다.', e)

    except IndexError:
        print('잘못된 인덱스입니다.')
    
    except Exception as e:
        print('예외가 발생했습니다.', e)
    
    else:
        print('오류 없음')

    finally:
        print('코드 종료')
    return 0

test()
