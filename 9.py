#В1.1
import random


A=[]
N = open('C:\Азаров\Vvod.txt', 'r', encoding='utf-8-sig')
for line in N:
    A.append([int(n) for n in line.split()])
for row in A:
    print(*map('{:2d}'.format, row))
print()

M=open('C:\Азаров\Vivod.txt','w+', encoding='utf-8-sig')
pol = 0
s = 0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i][j] <= 0:
           continue
        if A[i][j] > 0:
            pol += 1
            s += A[i][j]
M.write(str(s))
M.write('\n')
M.write(str(pol))

N.close()
M.close()
#В1.2
import random
N = int(input('N: '))
M = int(input('M: '))
B = [[random.randrange(10) for i in range(M)] for j in range(N)] 
C=open('C:\Азаров\Vivod2.txt','w+', encoding='utf-8-sig')
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
C.write(str(B))
C.close()
