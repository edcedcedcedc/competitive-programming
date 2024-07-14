""" 
understanding:
s =1 + 2 + 3...k
s = k + (k - 2) + (k - 1)
2s = (k + 1) + (k + 1) + (k + 1)
s = k(k+1)/2 

kx <= n 
k <= n/x
k = n/x
s = n/x(n/x + 1)/2

example 
n = 15
15/2
7.5 * 2 <= n
x = 2

n = 3 
3/2
1.5 <= n 
3/3 <= n
x = 3

goal: find and integer x and print it such that 2 <= x <=n and kx <= n


strategy:
if n > 2
x = 3
else
x = 2

implimentation:


evaluation:
read the output and input carefully!!!! 
"""


t = int(input())
n = list()

for i in range(t):
    n.append(int(input()))

for i in range(len(n)):
    if n[i] == 3:
        x = 3
        print(int(x))
    else:
        x = 2
        print(int(x))


        

    