"""
C. Game of Mathletes
time limit per test2 seconds
memory limit per test256 megabytes


understanding:
n(even) - integers on blackboard x1,x2,x3
k - integer
s - integer score = 0

n/2 - the game lasts and goes sequencially
    select and erase ai
    select and erase bi
    ai + bi = k -> score += 1


goal:
for each game output the score



strategy:


4 4

1 2 3 6
sort
6 3 2 1
max1
6
max2
3
9

1)
sort
pick first element
compare with other elements
if the elements match increase score and remove them
    a
    1 2 3
    0 1 2
    pop(a[0])
    2 3
    0 1

this should be O(n^2)

4 3
1 1 0 2


edge cases
2 1

1 2

nothing wrong



2)


"""

""" 
t = int(input())
for _ in range(t):
    _, k = list(map(int, input().split()))
    a = sorted(map(int, input().split()), reverse=True)
    s = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] + a[j] == k and i != j:
                s += 1
                a.pop(a.index(a[i]))
                a.pop(a.index(a[j - 1]))
    print(s)
 """


""" from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = Counter(a)
    score = 0
    used = set()

    for a in list(count):
        if a in used:
            continue
        b = k - a
        if a == b:
            score += count[a] // 2
        else:
            score += min(count[a], count.get(b, 0))
        used.add(a)
        used.add(b)

    print(score) """

""" from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = Counter(a)
    score = 0
    used = set()

    for a in count:
        if a in used:
            continue
        b = k - a
        if a == b:
            score += count[a] // 2
        else:
            score += min(count[a], count.get(b, 0))
        used.add(a)
        used.add(b)

    print(score) """


from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = Counter(a)
    score = 0

    for a in count:
        b = k - a
        if a == b:
            score += count[a] // 2
        elif b > a:
            score += min(count[a], count[b])

    print(score)
