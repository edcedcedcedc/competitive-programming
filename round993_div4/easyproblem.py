"""

A. Easy Problem


understanding:

how many ordered pairs of (a,b) are there such that a + b = n or a = n - b

i am given n

2 <= n <= 100

n = 2

a + b = n

n = 4

n = 6

goal:
a + b = n // identity


strategy:

two loops and meet the identity



complexity:
    O(n^2)

"""

t = int(input())

for i in range(t):
    n = int(input())
    r = 0
    for a in range(1, n):
        for b in range(1, n):
            if a + b == n:
                r += 1

    print(r)


""" 

I could optimize it to O(n) but will do it later on
 """
