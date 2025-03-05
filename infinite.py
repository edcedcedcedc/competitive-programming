""" 




 """
from functools import reduce
import math 

t = int(input())
for i in range(t):
    n, l, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    test = a.copy()
    if n == 1 and l == 1:
        if a[0] == 1:
            print(1)
        else:
            print(0)
    elif a.count(1) == 0 or a.count(0) == 0:
        print(0)
    else:
        x = math.floor(l / n)
        a = a * x
        for i in range(n):
            if len(a) != (l - 1):
                a.append(test[i])
        #print(len(a), a, l)
        print(reduce(lambda x, y: x ^ y, a))
