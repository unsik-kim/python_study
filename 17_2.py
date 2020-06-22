import random

i = 0
while i != 1 :
    i = random.randint(1,45);
    print(i)

for i in range(5) :
    for i in range(6) :
        print(random.randint(1,45), end='\t')
    print()

