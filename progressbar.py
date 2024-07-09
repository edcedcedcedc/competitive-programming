""" 

0 - 35mins - thinkin setting the goal 
45mins - started coding the problem 


goal/understanding:

a bar is n squares
square -  
1 - - - - - - - - - -  n - 1
each - has a saturation 0 - k for the a_ith - 

ex
a bar 1 <= i <= n
- 1,2, i - 1, have saturation k
- i + 1, i + 2, n have saturation 0
- i has saturation k from 0 to k measured in % t

strategy:
    total abstract saturation of the bar in % = n * k * t / 100  
    total of objects at max k = total saturation / k and floor 
    total of objects at max k as saturated =  total of objects at max k * k 
    total saturation object - total objects as saturated = any saturation 

    ex
    10 10 54
    abstract part of saturated bar 10 * 10 * 54 / 100
    0.1 from 54 are max saturated so 5
    5 as satured again * k  50
    54 - 50 = 4 of any saturation 

"""
import math 

n,k,t = map(int, input().split())
a = list()

total_saturation = math.floor((n * k * t)/100)
max_saturated = math.floor(total_saturation/k)
any_saturated = max_saturated + 1
any_saturation = total_saturation - (max_saturated * k)

for i in range(1,n+1):
    if i <= max_saturated:
        a.append(k)
    elif i == any_saturated:
        a.append(any_saturation)
    else:
        a.append(0)

for i in range(len(a)):
    print(int(a[i]), end=" ")
 

    


    