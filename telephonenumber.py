""" 
understanding:

goal: can a string become a telephone number ? 


string n 
70011223388 and 80000011223388 are not valid

the string is true with it contain 8 and its len is 11
it other words
x = n[i] = 8
n - x >= 10 then true otherwise false 
 """
""" strategy: """
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if s.__contains__("8"):
        f = s.find("8",0)
        s = s[f:]
        if len(s) >= 11:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

    



