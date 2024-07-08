""" 
00: read the text
06: try to understand contiguos segment i.e second statement
08: setted the goal trying strategy
15: come up with first strategy -> ascending sort and test diff between a and b be no greater then 1
20: don't understand one output 
30: strategy done -> coding 
32: got why 20 stuck, first n is a digit (read input carefully!)
35: stuck with input 
46: checking solution and strategy 1  
51: bugs in syntax and semantics LOL
1:05: bugs in algorithm 
1:18: updating the algorithm 
1:30: tested solution, works! yay!, more tests now, rereading the text
1:45+: wrong identities, I mean, for 0,1,2 cases, didn't count char in string but only string == 1

goal: return yes if string is diverse or not otherwise

diverse - contains consecutive adjacent letters and each occurs exactly once
contiguous segment - should come on after another and no duplicates 

input 1 <= n <= 100 inclusive, 
first n - number of strings, 
second - n lines, containing string one per line 

output
print n lines containt either yes or no, any case accept

strategy:
sort input ascending to compare it with the ascending order of alphanum map
alphanum [a,b,c,d] = 0,1,2,3
input [b,a,b,c] = 1,1,0,2 -> sort -> 0,1,1,2
abs 0 - 1 = 1
abs 1 - 1 = 0
abs 1 - 2 = 1

I have to better read and understand the task before doing it i.e goal 
"""

import string

letters = string.ascii_lowercase
d = int(input())
n = list()
alphanum_map = list()

for i in range(len(letters)):
    alphanum_map.append(letters[i])

def f():
    if len(n) == 1 and len(n[0]) == 1:
        return print("YES")
    else:
        for i in range(d):
            n.append(input().lower())

    for i in range(len(n)):
        ns = sorted(n[i])
        for j in range(len(ns)):
            if len(ns) - 1 == j:
                print("YES")
                break
            else:
                index1 = alphanum_map.index(ns[j])
                index2 = alphanum_map.index(ns[j + 1])
                if abs(index1 - index2) != 1:
                    print("NO")
                    break
              
f()
