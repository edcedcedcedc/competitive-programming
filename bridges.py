""" 

A. Destroying Bridges


understanding:
n = vertices 
e = edges 

e = n - 1 invariant, this connect any graph fully
k = number of edges you want to destroy 

strategy:

if k < e then n 
if k >= e then 1

 """

for i in range(int(input())):
    n, k = list(map(int, input().split()))
    e = n - 1
    if k >= e:
        print(1)
    else:
        print(n)
