"""

C. Yet Another Card Deck

a[i] = value by index


"""

_, _ = list(map(int, input().split()))
a = list(map(int, input().split()))
q = list(map(int, input().split()))

r = []

for i in range(len(q)):
    v = a.index(q[i])
    v += 1
    print(v, "v")
    r.append(v)

print(r)
