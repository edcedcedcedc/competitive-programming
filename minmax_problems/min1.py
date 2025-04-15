a, b, c, d = list(map(int, input().split()))

a = min(a, b)
d = max(c, d)
r = max(a, d) - min(a, d)

print(r)
