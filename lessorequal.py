""" 

understanding:
input
int n, k
int a....a[i] 


7 4
3 7 5 1 10 3 20
1 3 3 5 7 10 20
1 <= 1 
3 <= 1 !=
1 <= 2
3 <= 2 !=
....
1 <= 6
3 <= 6 
3 <= 6
5 <= 6
k == 4
6


7 2
3 7 5 1 10 3 20
-1

goal:
output
print any x [1,10^9] such that, exactly 
k el of a....a[i] <= x

strategy:
sort
edge cases 
if k == 0 zero elements are less or equal to x, so x should be smaller than the smallest
    a[0] - 1
elif k > 0 
    a[k - 1] - exactly <= x 
validation
how many elements in the sequence are less then equal to a[k - 1] 
if a[i] <= a[k - 1]
    count += 1
    if count > k or a[k - 1] < 1
        -1
    else
        a[k - 1]
examples 
Input: 7 4
Sequence: 3 7 5 1 10 3 20
Sorted sequence: [1, 3, 3, 5, 7, 10, 20]
k = 4, x = 5 i.e a[k - 1]
exactly 4 elements == k  
=> a[k - 1]

Input: 7 4
Sorted sequence: [1, 3, 3, 5, 5, 10, 20]
k = 4, x = 5 i.e a[k - 1]
not exactly 4 elements are <= x there are 5, k!= 5
=> -1 


implimentation:



evaluation:
read carefully each sentence 
write down each variables and constrains
write down edge cases for 0,1,2,infinity for all variables 
fully assure that understood the problem
impliment strategy
----
0.1
forgot the break statement 
0.2
1 <= n <= 2*10^5
0 <= k <= n
1 <= a[i] <= 10^9
1 <= x <= 10^9
 
conclusion:
hard one
- - - - - - - - a[i - 1] a[i]
test for k, if k = 0 this implies that 


"""
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
x = 0 
count = 0

if k == 0:
    x = a[0] - 1
else:
    x = a[k - 1]

for i in range(n):
    if a[i] <= x:
        count += 1
    else:
        break

if count > k or x < 1:
    print(-1)
else:
    print(x)
