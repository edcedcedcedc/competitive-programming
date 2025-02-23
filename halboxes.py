""" 


understanding:
array a_1...a_i-1,a_i
he wants sort them increasing order, he can only reverse any subarray of len at most k

the possible states of the a_1...a_i-1,a_i, k, n
sorted ascending ->

sorted descending -> 
    n > k and k >=2
    n < k and k >=2

mixed ->
    n > k and k >=2

equal -> true

n == k -> true 

10 3 830 14


goal:
is ti possible to sort the boxes using any number or reverses ?
 """


t = int(input())
for i in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if n == k:
        print("YES")
    elif sorted(a) == a or ((n > k or n < k) and k >=2):
        print("YES")
    else:
        print("NO")
    

        
