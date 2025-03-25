""" 
A. Love Triangle



5

2 4 5 1 3
1 2 3 4 5
0 1 2 3 4
 """

""" _ = input()
n = list(map(int, input().split()))

for j in range(len(n)):
    v0 = n[j]

    try:
        v = n[v0 - 1]

        for k in range(2):
            v = n[v - 1]
    except:
        print("NO")
        break

    if v0 == v:
        print("YES")
        break
    elif v != v0 and j == len(n) - 1:
        print("NO")
       
        
      
           
        

 """

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
