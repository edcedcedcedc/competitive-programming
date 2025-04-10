"""
A. Even Odds

"""

""" 
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
            


strategy:


(n + 1) // 2 

1 2 3 4 5 6 7 8 9 10 11
1   3   5   7        11

some sort of induction if it works for 10 then shall work for everyting
(10 + 1) // 2 -> 5
1 3 5 7 11 

each odd num increase by 2 each time starting at 1
1 + (k - 1) * 2 = 2k - 1

1 2 3 4 5
1 + (3 - 1) * 2

1 2 3 4 5 6 7 8 9 10

 """


n, k = map(int, input().split())

odds = (n + 1) // 2
print("odds", odds)

if k <= odds:
    print(2 * k - 1)
else:
    print(2 * (k - odds))
