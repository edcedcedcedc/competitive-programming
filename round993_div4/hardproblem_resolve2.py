""" """

for i in range(int(input())):
    m, a, b, c = list(map(int, input().split()))
    r = 0
    r += min(m, a) + min(m, b)
    if m - a >= 1:
        r += min(m - a, c)
        c -= min(m - a, c)
    if m - b >= 1:
        r += min(m - b, c)
    print(r)
