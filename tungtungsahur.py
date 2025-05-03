""" """

for i in range(int(input())):
    s1 = input()
    s2 = input()
    s1R = [x for x in s1.split("L") if x]
    s1L = [x for x in s1.split("R") if x]
    s2R = [x for x in s2.split("L") if x]
    s2L = [x for x in s2.split("R") if x]
    r1 = 1
    r2 = 1
    for j in range(len(s1R)):
        if s1R[j].count("R") == s2R[j].count("R") or s1R[j].count("R") * 2 == s2R[
            j
        ].count("R"):
            if j == len(s1R) - 1:
                r1 = 0
        else:
            break
    for j in range(len(s1L)):
        if s1L[j].count("L") == s2L[j].count("L") or s1L[j].count("L") * 2 == s2L[
            j
        ].count("L"):
            if j == len(s1R) - 1:
                r2 = 0
        else:
            break

    if len(s1R) == 0:
        r1 = 0
    if len(s1L) == 0:
        r2 = 0

    if r1 == 0 and r2 == 0:
        print("YES")
    else:
        print("NO")


""" 
wrong solution

 """
