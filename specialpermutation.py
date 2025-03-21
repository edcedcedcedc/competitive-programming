""" 



 """

import random;


for i in range(int(input())):
    n = int(input())
    l = list(range(1,n + 1))
    l_new = []
    for j in range(len(l)):
        if j != len(l) - 1:
            l_new.append(l[j + 1])
        else:
            l_new.append(l[0])
    s = ""
    for j in range(len(l)):
        s += f"{l_new[j]} "
    print(s)