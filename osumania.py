t = int(input())

for i in range(t):
    rows = int(input())
    r = ""
    for j in range(rows):
        s = input()
        n = 0
        for i in range(len(s)):
            if s[i] == '#':
               n = i + 1
               break
        r += " " + f"{n}"
    print("".join(reversed(r)))    


       
        





