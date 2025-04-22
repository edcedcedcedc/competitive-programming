"""
A. String Task
time limit per test2 seconds
memory limit per test256 megabytes

"""

s = input()
s = list(s.lower())
t = set(list("aoyeui"))

for i in range(len(s)):
    if s[i] not in t:
        s[i] = "." + s[i]
    else:
        s[i] = ""
print("".join(s))
