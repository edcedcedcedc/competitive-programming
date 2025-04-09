"""


understanding:
cost of n i s the result of dividing number n by the sum of its digits

cost = n/digitsOfn

cost of 104 is 104/1+0+4 -> 20.8 cost of 111 -> 111/1+1+1 = 37

n doest contain leading zeros
you can remove any nums of digits from n including None
    so that the remaining n is strictly greater than zero
the remaining digits cannot be rearranged
as a result you may have a number with leading zeros

For example, you are given the number 103554
. If you decide to remove the digits 1
, 4
, and one digit 5
, you will end up with the number 035
, whose cost is 0350+3+5=4.375
.

goal:
what is the minimum number of digits you need to remove so the cost becomes
    the minimum possible ?


strategy:

666

6/6 = 1 -> 2


13700

13700/137 = 100 -> 0

3/3 = 1 -> 4
7/7 = 1 -> 4
0/0 = undefined





102030

030/3 = 10



7


107      70

1        0



000000001
1/1 = 1

100000000
1
1/1 = 1

1230000
123 ; 4
1 ; 2
2 ; 2
3 ; 2

s = 12321
count s -> 5
pick any si >= 1 pop it
remove the rest
count s again count s -> 4
this is what I have to remove

s = 10002
1 or 2



"""
