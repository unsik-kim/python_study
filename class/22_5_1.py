# a = {i for i in range(10)}
# a

# b = []

# for i in range(10) :
#     b.append(i)

# print(a)
# print(b)

a = [i for i in range(10) if i% 2 == 0]
print(a)

b = []

for i in range(10) :
    if i%2==0 :
        b.append(i)

print(b)