t = int(input())
x0 = 0
y0 = 0
z0 = 0

for i in range(t):
    xc, yc, zc = list(map(int, input().split()))
    x0 += xc
    y0 += yc
    zc += zc
if x0 == y0 == z0:
    print("YES")
else:
    print("NO")
