""" 
a - seq of int
s - seq of strings


replace a_i with A
or
replace m + 1 - a_i with A 
can replace the char at any position multiple times

goal:
find the lexicographically smallest string you can get afte this operations 

a strin x is smaller then y if first letter in x is alphabetically before y 




 """


t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    s = list('B' * m)
    a = list(map(int, input().split()))
    for j in range(n):
        #new index
        a[j] = a[j] - 1
        a[j] = min(a[j], m - a[j] - 1)
        if s[a[j]] == "B":
            s[a[j]] = "A"
        else:
            s[m - a[j] - 1] = "A"
    print("".join(s))
