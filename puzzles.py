n, m = list(map(int, input().split()))
f = sorted(map(int, input().split()))
best = float("inf")
for i in range(m - n + 1):
    best = min(best, f[i + n - 1] - f[i])
print(best)
