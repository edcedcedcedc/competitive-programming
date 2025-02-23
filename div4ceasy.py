""" 
understanding:
arrays a,b with n,m elements
j = m = 1
at most 1 operation with n[i] of n with the m[j]

states of the array
ascending
descending 
mixed

states between numbers
<=
>

goal:
is it possible to sort it in an increasing order
what is the smallest number >= previous number

strategy:



"""


t = int(input())

for i in range(t):
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = list(map(int, input().split()))
    b = int(input())
    a[0] = b - a[0]

    for i in range(1,n):
        if a[i] >= a[i - 1] and i == n - 1:
            print("YES")
        if a[i] < a[i - 1]:
            a[i] = b - a[i]
            if a[i] >= a[i - 1]:
                continue
            else:
                print("NO")
                break

           
            
            

        



        


