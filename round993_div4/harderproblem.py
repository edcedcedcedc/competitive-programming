"""
D. Harder Problem


understanding:

mode of a list is the element that appears the most frequently.
if there is a tie choose any between two integers

ai is mode of [b1 b2 bi] for all 1 <= i <= n

"""

from collections import Counter


t = int(input())
for i in range(t):
    _ = int(input())
    a = Counter(list(map(int, input().split())))
    print(a)
