""" 
A. Love Triangle

A -> B -> C -> A
 
def love_triangle(n, f):
    for i in range(n):
        a = i + 1 
        b = f[a - 1]  
        c = f[b - 1]  
 
        if f[c - 1] == a:  
            print("YES")
            return
    print("NO")
 
n = int(input())
f = list(map(int, input().split()))
 
love_triangle(n, f)
 """

n = int(input())
p = list(map(int, input().split()))

for i in range(n):
    a = i + 1
    b = p[a - 1]
    c = p[b - 1]
    if p[c - 1] == a:
        print("YES")
        break
    elif p[c - 1] != a and i == n - 1:
        print("NO")
    else:
        continue
