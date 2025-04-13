""" """

for i in range(int(input())):
    s = input().split(" ")
    for j in range(len(s)):
        print(s[j][:1], end="")
    print("")
