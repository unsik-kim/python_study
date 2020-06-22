age = int(input())
balance = 9000


if age>=7 and age<=12 :
    balance -= 650
elif age>=13 and age<=18 :
    balance -= 650
elif age>=19 :
    balance -= 1250

print(balance)