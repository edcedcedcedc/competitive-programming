"""
A. Even Odds

"""

""" 


understanding:
------------------------------------------------
def generator_odd(limit=10**12):
    i = 1
    while i <= limit:
        yield i
        i += 2


def generator_even(limit=10**12):
    i = 2
    while i <= limit:
        yield i
        i += 2


n, k = list(map(int, input().split()))

sequence_odd = generator_odd()
sequence_even = generator_even()

for i in range(n):
    if i <= n // 2:
        odd_value = next(sequence_odd)
        if i == k - 1:
            print(odd_value)
            break
    elif i > n // 2:
        even_value = next(sequence_even)
        if i == k - 1:
            print(even_value)
            break
            
-----------------------------------------------------------------

1 2 3 4 5 6 7 8 9 10

 2 4 6 8 10 12 14 16 18 20
1 3 5 7 9 11 13 15 17 19

1 3 5 7 9 2 4 6 8 10

then 

from 20 numbers 

10 even 
10 odd 

half of them 


0 1 2 3 4 5 6 7 8 9 10

10 / 2 = 5
8 / 2 = 4
7 / 2 = 3.5
7 // 2 = 3





any even number 

2 * (k - half)

any odd number 

1 + (k - 1) * 2 for any k > 1

k = 1 -> 1 + (1 - 1) * 2 = 1 
k = 2 -> 1 + (2 - 1) * 2 = 3

1 + (k - 1) * 2 = 1 + 2k - 2 = 2k - 1

n = 10
k = 10



















Strategy:

Generator strategy
Precompute and yield a huge sequence 
find out the value k 

Math strategy
Compute n odds 
If k <= odds 
	print num odd
Else 
	print num even

    

 """

n, k = map(int, input().split())

m = (n + 1) // 2


if k <= m:
    print(2 * k - 1)
else:
    print(2 * (k - m))
