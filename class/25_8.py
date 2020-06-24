keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

print(x)

x.pop('delta')

x = {key:value for key, value in x.items() if value != 30}


print(x)