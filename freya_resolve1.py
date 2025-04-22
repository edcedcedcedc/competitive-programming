"""
C. The Legend of Freya the Frog
"""

import math

for _ in range(int(input())):
    x, y, k = list(map(int, input().split()))
    r = 0
    if x > y:
        r = math.ceil(x / k) + max(math.ceil(x / k) - 1, math.ceil(y / k))
    else:
        r = math.ceil(y / k) * 2
    print(r)
