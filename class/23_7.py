col, row = map(int, input().split())

matrix1 = []
matrix2 = []


print('insert bomb!')
while True :
    for i in range(row) :
        matrix1.append(list(input()))
        matrix2.append([0 for _ in range(col)])
        if len(matrix1[i])!=col :
            print('re insert bomb!')
            matrix1.clear()
            break
    if len(matrix1)==row :
        break

print(matrix1)


for i in range(row) :
    for j in range(col) :
        if matrix1[i][j] == '.' :
            for n in range(3) : # 행
                for m in range(3) : # 열
                    y = int((i-1)+n) # 행
                    x = int((j-1)+m) # 열
                    
                    if (x>=0 and y>=0) and (x<row and y<col) :
                        if matrix1[y][x]=='*' :
                            matrix2[i][j] += 1
        else :
            matrix2[i][j] = '*'

for i in range(row) :
    for j in range(col) :
        print(matrix2[i][j], end=" ")
    print()