#В1.1
import random
pol = 0
s = 0
N = int(input('Ввод: '))
A = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if A[i][j] <= 0:
           continue
        if A[i][j] > 0:
            pol += 1
            s += A[i][j]

print('Сумма:', s)
print('Число:', pol)
#В1.2
N = int(input('N: '))
M = int(input('M: '))
B = [[random.randrange(10) for i in range(M)] for j in range(N)] 
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(B)
