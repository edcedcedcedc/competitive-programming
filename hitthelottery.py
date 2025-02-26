



d = [100,20,10,5,1]

def myfunc(n):
    c = 0
    for i in range(len(d)):
        c += n // d[i]
        n %= d[i]
    return c

t = int(input())
print(myfunc(t))

        