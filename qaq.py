      
""" 
understanding:
number of "QAQ" substrings in any string, where QA can be separated from each other 

strategy:
count q's
from left to right, before and after "A"
in the end multiply by 0, because all the "A"s have been counted

 """

s = input()
curr_q_cnt = 0
tot_q_cnt = s.count("Q")
ans = 0
for x in s:
    if x == 'A':
        ans += curr_q_cnt * (tot_q_cnt - curr_q_cnt)
        print("cq", curr_q_cnt, "tq", tot_q_cnt, "ans", ans)
    elif x == 'Q':
    	curr_q_cnt += 1
print(ans)#
