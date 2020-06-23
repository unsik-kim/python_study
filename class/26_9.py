x, y = map(int, input().split())

a = set()
b = set()

for i in range(x):
    if x%(i+1)==0:
        a.add(i+1)

for i in range(y):
    if y%(i+1)==0:
        b.add(i+1)

print(a, b, sep=' ')

divisor = a & b 

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)