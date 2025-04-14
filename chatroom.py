"""


understanding/goal:
no permutation is allowed

goal:
check if you can make 'hello' out of s

strategy:
pick up letters starting left to right till you get to 'hello'
create a priority array of True and as you go switch True to False, to know where you at



"""

""" 
if (
    "h" in s
    and "e" in s
    and s.count("l") >= 2
    and "o" in s
    and (s.index("h") < s.index("e") < s.index("l") < s.index("o"))
):
    print("YES")
else:
    print("NO") """


""" 
helool

 """


""" i = s.find("l")
if i != -1:
    fp = s[: i + 1]
    sp = s[i + 1 :]
    if (
        "h" in fp
        and "e" in fp
        and "l" in fp
        and (fp.index("h") < fp.index("e") < fp.index("l"))
    ):
        if "l" in sp and "o" in sp and (sp.index("l") < sp.index("o")):
            print("YES")
    else:
        print("NO")
else:
    print("NO")



atlevhhalrohairnolsvocafgueelrqmlqlleello
 """


s = list(input())
r = [None] * 5
t = ["h", "e", "l", "l", "o"]
priority = [True, True, True, True, True]

for i in range(len(s)):

    if (
        s[i] == "h"
        and priority[0]
        and priority[1]
        and priority[2]
        and priority[3]
        and priority[4]
    ):
        r[0] = "h"
        priority[0] = False

    elif (
        s[i] == "e"
        and not priority[0]
        and priority[1]
        and priority[2]
        and priority[3]
        and priority[4]
    ):
        r[1] = "e"
        priority[1] = False
    elif (
        s[i] == "l"
        and not priority[0]
        and not priority[1]
        and priority[2]
        and priority[3]
        and priority[4]
    ):
        r[2] = "l"
        priority[2] = False
    elif (
        s[i] == "l"
        and not priority[0]
        and not priority[1]
        and not priority[2]
        and priority[3]
        and priority[4]
    ):
        r[3] = "l"
        priority[3] = False

    elif (
        s[i] == "o"
        and not priority[0]
        and not priority[1]
        and not priority[2]
        and not priority[3]
        and priority[4]
    ):
        r[4] = "o"
        priority[4] = False

    if not None in r:
        print("YES")
        break

    elif i == len(s) - 1:
        print("NO")
