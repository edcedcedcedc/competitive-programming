"""

C. Sum in Binary Tree

Complexity O(log(n))

"""

for i in range(int(input())):
    n0 = int(input())
    n = n0
    r = 0
    while n >= 2:
        n = n // 2
        r += n
    print(r + n0)
