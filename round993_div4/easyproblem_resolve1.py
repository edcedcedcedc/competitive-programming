for i in range(int(input())):
    r = 0
    n = int(input())
    for a in range(n):
        for b in range(n):
            if a + b == n:
                r += 1
    print(r)
