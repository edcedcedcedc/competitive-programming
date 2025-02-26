""" 
understanding:
int[] a = {0,0,0,0,...n = 0}, len n
int k 
int p

invariant:
i, x, 1 <= i <= n and -p <= x <=p 
assing a_i = x 

goal:
For each test case, output the minimum number of operations to achieve the final sum k in the array, or -1 
if it is impossible to achieve the sum k

in other words:
you have an array a, where a_i should be replaced with x that is between -p and p and equal to k

n, k , p
21 100 10
9 -420 42
5 -7 2

round(k/p) <= n and -p <= x <= p
res = abs(res)

21 * x = 100

 """
import math

t = int(input())
for i in range(t):
    n, k, p = list(map(int, input().split()))
    x = math.ceil(abs(k/p))
    if x <= n:
        print(x)
    else:
        print(-1)
