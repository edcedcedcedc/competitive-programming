"""

D. Same Differences


Understanding:
aj - ai = j - i and i < j
aj - j = ai - i

val = aj - j
val = ai - i

brute force is going to be O(n^2)
Hashing is going to be O(n)
the i < j is redundant because of the identity which implies this


"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    res = 0

    for i in range(n):
        key = a[i] - i
        print("key", key)
        if key in d:
            res += d[key]
            d[key] += 1
        else:
            d[key] = 1

    print(res)
