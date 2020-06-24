def print_numbers(*args):
    for arg in args:
        print(arg)
    print()

a = [0, 1, 2, 3]

b = (4, 5)

c = {1}

print_numbers(*a)
print_numbers(*b)
print_numbers(*c)

