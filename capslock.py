"""
A. cAPS lOCK
time limit per test0.5 second
memory limit per test256 megabytes

"""

s = input()
if len(s) == 1 and s.isupper():
    print(s.lower())
elif len(s) == 1 and s.islower():
    print(s.upper())
elif s.isupper():
    print(s.lower())
elif s[1:].isupper():
    print(s[0:1].upper() + s[1:].lower())
else:
    print(s)
