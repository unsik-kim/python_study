start, stop = map(int, input().split())

i = start

while True :
    if i == stop+1 :
        break
    if i%10 == 3 :
        i += 1
        continue

    print(i, end=' ')
    i += 1