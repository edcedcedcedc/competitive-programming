#strategy
#divide the maximum of a or b by d
#ceil it 
#add the same amount to it 

import math

r = []

for i in range(int(input())):
    x, y, k = map(int, input().split())
    ans = 0
  
    if x > y:
        ans = math.ceil(x / k)
        ans += max(ans - 1,math.ceil(y / k))
    else:
        ans = math.ceil(y / k)
        ans += max(ans, math.ceil(x / k))
    r.append(ans)

for i in range(len(r)):
    print(r[i])
    
    

    
