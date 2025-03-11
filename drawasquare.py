

""" 

a square is 
a set of vertices where
each vertex has degree of 2
and
between any two edges 
there is 90 degrees or 1/2pi radians 


 """

for t in range(int(input())):
    l,r,d,u = list(map(int, input().split()))
    if l == r == d == u:
        print("YES")
    else:
        print("NO")