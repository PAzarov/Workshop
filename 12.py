#A1
def f(x,n):
    def fac(n):
        if n<1:
            return 1
        else:
            return n * fac(n-1)
    return x**n/fac(n)
print(f(4,5))
#Б1
def write():
    a = int(input())
    if a == 0:
        return
    elif a % 2 == 1:
        print(a)
        write()
    else:
        write()
write()
