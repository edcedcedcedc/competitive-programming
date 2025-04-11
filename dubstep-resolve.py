"""
A. Dubstep


progress:
solve it in 4 minutes

complesity O(n) in worst case, O(n/2) is the average


"""

s = input().split("WUB")

for i in range(len(s)):
    if s[i] != "":
        print(s[i] + " ", end="")
