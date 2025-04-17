"""

D. Odd Queries


"""

""" 

complexity 
O(t * n * q)
not good fod large n and q
q = 10^5
n = 10^5
t = 10^4
 """


""" for x in range(int(input())):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for y in range(q):
        l, r, k = list(map(int, input().split()))
        a_copy = a.copy()
        for z in range(l - 1, r):
            a_copy[z] = k
        if sum(a_copy) % 2 == 0:
            print("NO")
        else:
            print("YES")
 """


""" 
understanding/goal:
find out if substituting some interval in the array its sum is odd 

strategy:
compute prefix sum array based on array a





complexity
O(t (n + q))
good for lage inputs 
 """





""" 



for curious out there, this types of problems arent hard for me anymore
I read them easily :)





 """
for t in range(int(input())):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    for i in range(q):
        l, r, k = list(map(int, input().split()))
        total = prefix[n]
        segment_sum = prefix[r] - prefix[l - 1]
        new_sum = total - segment_sum + (r - l + 1) * k
        print("YES" if new_sum % 2 == 1 else "NO")
