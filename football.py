"""

A. Football

Running time -> O(1) or O(n) in worst case

update:
O(1)

"""

s = input()
c0 = "0000000"
c1 = "1111111"
if c0 in s or c1 in s:
    print("YES")
else:
    print("NO")
