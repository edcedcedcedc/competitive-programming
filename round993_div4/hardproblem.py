"""

C. Hard Problem


understanding:

2 rows m seats each
a + b + c monkeys greedy asssign to a seat
a of them want to seat in row 1
b of them want to seat in row 2
c have no preference


goal:
what is the max number of monkeys that can seat in a given two rows m ?

strategy:
imagine m as an array, a,b,c are values that can be placed in this array
let x = a and x = b, but start greedy, first x is x = a, the second x is x = b
compare m >= x
increase the result if needed
adjust the difference m - x
adjust c
increase the result if needed
"""

""" 
first solution 
"""


""" t = int(input())
for i in range(t):
    m, a, b, c = list(map(int, input().split()))
    diff = 0
    r = 0

    if m >= a:
        r += a
        if m - a >= 1:
            diff = m - a
            if diff >= c:
                r += c
                c = 0
                diff = 0
            else:
                r += diff
                c = c - diff
                diff = 0
    else:
        r += m

    if m >= b:
        r += b
        if m - b >= 1:
            diff = m - b
            if diff >= c:
                r += c
            else:
                r += diff
    else:
        r += m

    print(r)
 """

""" 
generalization of the solution 
"""


""" def main():
    t = int(input())
    for _ in range(t):
        m, a, b, c = map(int, input().split())
        r = 0

        def apply(x):
            diff = 0
            nonlocal m, c, r
            if m >= x:
                r += x
                if m - x >= 1:
                    diff = m - x
                    if diff >= c:
                        r += c
                        c = 0
                    else:
                        r += diff
                        c -= diff
            else:
                r += m

        apply(a)
        apply(b)
        print(r)


if __name__ == "__main__":
    main() """


t = int(input())
for i in range(t):
    m, a, b, c = list(map(int, input().split()))
    diff = 0
    r = 0

    if m >= a:
        r += a
        if m - a >= 1:
            diff = m - a
            if diff >= c:
                r += c
                c = 0
                diff = 0
            else:
                r += diff
                c = c - diff
                diff = 0
    else:
        r += m

    if m >= b:
        r += b
        if m - b >= 1:
            diff = m - b
            if diff >= c:
                r += c
            else:
                r += diff
    else:
        r += m

    print(r)
