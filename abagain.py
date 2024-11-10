t = int(input())
n = list()
for _ in range(t):
    n.append(list(input()))

for i in range(len(n)):
    print(int(n[i][0])+int(n[i][1]))
        