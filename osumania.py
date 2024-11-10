t = int(input())
o = []
for i in range(t):
    rows = int(input())
    r = ""
    for j in range(rows):
        s = input()
        n = 0
        for i in range(len(s)):
            if s[i] == '#':
               n = i+1
        r += " " + f"{n}"
    o.append("".join(list(reversed(r))))    

for i in range(len(o)):
    print(o[i])

       
        





