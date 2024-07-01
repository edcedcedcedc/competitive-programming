import math
n = int(input())
g = list(map(int, input().split()))
t = 0
if 1 in g:
    o = sum(filter(lambda x: x == 1, g))/4
    f = len(list(filter(lambda x: x == 3, g)))/4
    if o > f:
        t = (
            sum(filter(lambda x: x == 3, g))/3 + 
            sum(filter(lambda x: x != 3 and x != 1, g))/4 + 
            (o - f)
        )
    else:
        t = (
            sum(filter(lambda x: x == 3, g))/3 + 
            sum(filter(lambda x: x != 3 and x != 1, g))/4 
        )
else: 
    t = (
        sum(filter(lambda x: x == 3, g))/3 + 
        sum(filter(lambda x: x != 3, g))/4
    ) 
print(math.ceil(t))
