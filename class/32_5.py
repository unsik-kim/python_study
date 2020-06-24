files = input().split()

print(list(map(lambda x: ('0'+x) if (3-x.find('.'))==1 else ('00'+x) if (3-x.find('.'))==2 else (x), files)))