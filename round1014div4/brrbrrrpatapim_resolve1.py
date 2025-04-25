"""


solved in 35 minutes, init 150 minutes



resolve 25/04/2025
    150/35 = 4.3
    4.3 times faster then init solve

"""

t = int(input())
for _ in range(t):
    n = int(input())
    password = ""
    seen = set()

    for i in range(n):
        l = list(map(int, input().split()))
        for j in range(len(l)):
            if l[j] not in seen:
                seen.add(l[j])
                password += f"{l[j]}" + " "
    for i in range(1, n * 2 + 1):
        if i not in seen:
            password = f"{i}" + " " + password
            break
    print(password)
