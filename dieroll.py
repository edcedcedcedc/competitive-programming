from math import gcd


def reduce(a,b):
    return f"{a // gcd(a,b)}/{b // gcd(a,b)}"
w,y = list(map(int, input().split()))
print(reduce(6 - max(w,y) + 1, 6))

