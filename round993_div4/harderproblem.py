"""
D. Harder Problem


understanding:

mode of a list is the element that appears the most frequently. 
if there is a tie choose any between two integers 

"""

from collections import Counter


t = int(input())
for i in range(t):
    _ = int(input())
    a = Counter(list(map(int, input().split())))
    print(a)
