a, b = map(int, input().split())

c = [2**i for i in range(a,b+1)]

c.pop(1)
c.pop(-2)

print(c)