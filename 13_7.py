cash = int(input())
couponName = input()
result = 0;

if couponName == 'Cash3000' :
    result = cash - 3000
elif couponName == 'Cash5000' :
    result = cash - 5000

print(result)