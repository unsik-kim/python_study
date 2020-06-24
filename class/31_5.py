def fib(count, value1=0, value2=1):
    print(int(count),'loop')
    if count==0:
        return  value1
    
    value0 = value1
    value1 = value2
    value2 = value0 + value1

    print (value0, value1, value2)
    count -= 1

    return(fib(count, value1, value2))

n = int(input())
print(fib(n))