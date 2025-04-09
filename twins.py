"""
A. Twins
time limit per test2 seconds
memory limit per test256 megabytes

complexity

O(n^2) at worst case
O(n) on average

"""

n = int(input())
a = list(map(int, input().split()))
r = 0
test = 0
while True:
    test += a.pop(a.index(max(a)))
    r += 1
    if test > sum(a):
        print(r)
        break
