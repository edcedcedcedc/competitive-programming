s, n = list(map(int, input().split()))
a = []

for i in range(n):
    x, y = list(map(int, input().split()))
    a.append([x, y])

a = sorted(a)

for i in range(len(a)):
    if s > a[i][0]:
        s += a[i][1]
        if i == len(a) - 1:
            print("YES")
    else:
        print("NO")
        break
