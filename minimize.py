n = int(input())
r = []
for i in range(n):
    (a, b) = map(int, input().split())
    r.append(abs(b - a))
for i in range(len(r)):
    print(r[i])