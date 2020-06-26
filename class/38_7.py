class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    wordLength = len(word)
    if wordLength%2 == 0:
        length = int(wordLength/2)
    else:
        length = int((wordLength/2)-1)

    for i in range(length):
        if word[i] != word[(wordLength-1)-i]:
            raise NotPalindromeError
    
    print(word)


    

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)