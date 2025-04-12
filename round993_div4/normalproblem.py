"""

B. Normal Problem


understanding:

string is an inverse  of of X-AXIS
meaning its reversed

abc from the front
cba from the back


strategy:
reverse
substitute

qwq

pwp


ppppp

qqqqq


pppwwwqqq

pppwwwqqq



wqpqwpqwwqp
pqpqpqpq


complexity:
O(t * s)

"""

t = int(input())
for i in range(t):
    a = input()
    a = list(a[::-1])
    for j in range(len(a)):
        if a[j] == "p":
            a[j] = "q"
        elif a[j] == "q":
            a[j] = "p"
    print("".join(a))
