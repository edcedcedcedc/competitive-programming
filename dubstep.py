"""

A. Dubstep

complexity
O(n)

"""

s = input()
s = s.split("WUB")
r = ""

for i in range(len(s)):
    if s[i] != "":
        r += s[i] + " "
print(r)
