def countdown(n):

    def downFunc():
        nonlocal n
        n -= 1
        return n+1

    return downFunc
        

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')