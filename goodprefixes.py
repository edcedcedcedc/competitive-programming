""" 
understanding:

list = 0 1 2 1 4 
0
sum - max == max

0 1 
sum - max != max 

0 1 2 
sum - max = max

0 1 2 1
sum - max = max 

0 1 2 1 4
sum - max = max 

good prefixes implies that the sum
of list elements from a[0]+a[i + 1]+a[i + 2]....+a[n] at each particular a[i]
including all the previous a[i - 1]...a[i - 2]
ex i = 3
a[i]
a[i-1]+a[i-2]
a[i-1]+a[i-2]+a[i-3]
should consist of a max value, and all other elements besides the max value need to add up to max value
ex - a particular iteration
0 1 2 3
3 is the max value 
0 + 1 + 2 = 3 
the sum of values besides max 
3 == 3 all good 
to check this 
sum - max = max 

goal: print the sum of the good prefixes

strategy:
sum - max = max 

implimentation:

evaluation:
read, read, read, understand..!
"""
t = int(input())
l = []
r = []

for _ in range(t):
    _ = input()
    l.append(list(map(int, input().split())))

for i in l:
    tmp_sum = 0
    tmp_max = 0
    tmp_r = 0
    for j in range(len(i)):
        tmp_sum += i[j]
        tmp_max = max(tmp_max, i[j])
        if tmp_sum - tmp_max == tmp_max:
            tmp_r += 1
    r.append(tmp_r)

for i in r:
    print(i)
