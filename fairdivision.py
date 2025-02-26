

t = int(input())
for i in range(t):
    _ = int(input())
    n = list(map(int, input().split()))
    c1 = n.count(1)
    c2 = n.count(2)
    if (c1 + c2 * 2) % 2 != 0:
        print("NO")
    else:
        s = c1 + (c2 * 2) / 2
        if s % 2 == 0 or s % 2 == 1 and c1 != 0:
            print("YES")
        else:
            print("NO")