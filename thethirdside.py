""" 

priority que
triangle inequality a + b > c
inequality holds for any x = a + b - 1
a + b > x if  x = a + b - 1

strategy:
sum n
x = sum(n) - (len(n) - 1)

O(t * n)
 """
for i in range(int(input())):
    _ = int(input())
    n = sorted(map(int, input().split()))
    if len(n) == 1:
        print(n[0])
    else:
        x = sum(n) - (len(n) - 1)
        print(x)