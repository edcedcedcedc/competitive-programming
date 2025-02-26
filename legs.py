
import math


""" 

4
2

6 -> 2

2 -> 1

8 -> 2

 """
for i in range(int(input())):
    n = int(input())
    print(min(math.ceil(n/2), math.ceil(n/4)))
    