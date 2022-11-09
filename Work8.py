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
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in range(N, M):
    if B[i][j] >= 0:
        print('Максимальный элемент:', B)
    if B[i][j] < 0:
        print('Минимальный элемент:', B)