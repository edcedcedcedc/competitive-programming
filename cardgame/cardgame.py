""" 
goal/understanding:
I need suneet score, he ears 1 point if wins each each round in a game

strategy:
2 x 2 x 2 x 2 = 16
16 possible permutations

 """
t = int(input())
r = list()
n = list()

for _ in range(t):
    n.append(list(map(int, input().split())))

for i in range(len(n)):
    a = 0
    a1 = n[i][0]
    a2 = n[i][1]
    b1 = n[i][2]
    b2 = n[i][3]
    if a1 > b1 and a2 > b2:
        a += 1
    if a1 > b2 and a2 > b1:
        a += 1
    if a2 > b1 and a1 > b2:
        a += 1
    if a2 > b2 and a1 > b1:
        a += 1
    r.append(a)

for i in range(len(r)):
    print(r[i])



    

