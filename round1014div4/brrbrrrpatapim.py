for _ in range(int(input())):
    n = int(input())
    sn = set()
    r = list()

    for i in range(n):
        s = input().split()
        for j in range(len(s)):
            if s[j] not in sn:
                r.append(s[j])
                sn.add(s[j])

    for i in range(1, 2 * n + 1):
        s = str(i)
        if s not in sn:
            r.insert(0, s)
            break

    print(" ".join(r))
