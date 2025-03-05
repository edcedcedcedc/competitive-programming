

t = int(input())
r = 0
x, y = [0] * t, [0] * t

for i in range(t):
    x[i], y[i] = list(map(int, input().split()))

for i in range(t):
    for j in range(t):
        if x[i] == y[j]:
            r += 1
print(r)


