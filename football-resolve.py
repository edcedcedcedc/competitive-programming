"""

A. Football


progress:
okay I solved it in 3 minutes without looking to previous solution

complexity O(1)

"""

s = input()

s1 = "1" * 7
s0 = "0" * 7

if s1 in s or s0 in s:
    print("YES")
else:
    print("NO")
