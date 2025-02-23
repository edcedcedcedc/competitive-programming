""" 
understanding:
t num test cases 
s len string 
s_i = s_i+1
s_i + 1 has to be deleted 
s_i has to be replaced with the adjacent letter if no adjacent change to whatever


goal: 
minimum possible len thru any poss operations

strategy:
if there are any two equal tokens return 1 
if no equal tokens return len of s 

 """

t = int(input())
for i in range(t):
    s = input()
    for j in range(len(s)):
        if j == len(s) - 1:
            print(len(s))
            break
        if s[j] == s[j + 1]:
            print(1)
            break
            
        