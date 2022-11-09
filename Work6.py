#В1.1
n = int(input())
a = list(map(int, input().split()))
m = max(a)
a.reverse()
print(m)
print(*a)
#В2.2
a = list(map(float, input().split()))
av = sum(a) / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = av
print(a[i], end=" ")